import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, SpatialDropout1D, Bidirectional
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.callbacks import EarlyStopping

# Leer los datos de entrenamiento y prueba
df_train = pd.read_csv("train1.csv")
df_test = pd.read_csv("test1.csv")

# Normalizar el texto y eliminar stopwords
nltk.download('stopwords')
spanish_stopwords = set(stopwords.words('spanish'))
df_train['titulo'] = df_train['titulo'].apply(lambda x: x.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u"))
df_test['titulo'] = df_test['titulo'].apply(lambda x: x.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u"))

# Convertir el conjunto de stopwords en una lista
spanish_stopwords = list(spanish_stopwords)

# Vectorizar los títulos de entrenamiento y prueba
vectorizer = CountVectorizer(stop_words=spanish_stopwords)
X_train_counts = vectorizer.fit_transform(df_train['titulo'])
X_test_counts = vectorizer.transform(df_test['titulo'])

# Transformar la columna 'categoria' en valores numéricos
df_train['categoria'] = df_train['categoria'].map({
    'Entretenimiento': 0,
    'Deportes': 1,
    'Película y Animación': 2,
    'Educación': 3,
    'Otros': 4
})

# Eliminar filas con valores NaN en 'categoria'
df_train = df_train.dropna(subset=['categoria'])

# Asegurarse de que las filas de X_train y y_train coincidan
X_train = X_train_counts[df_train.index]
y_train = df_train['categoria'].values

# Modelo de Regresión Logística
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)
y_pred_logreg = logreg.predict(X_test_counts)

# Modelo Random Forest
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test_counts)

# Tokenizar y convertir títulos a secuencias para el modelo LSTM
tokenizer = Tokenizer(num_words=5000, lower=True)
tokenizer.fit_on_texts(df_train['titulo'])
X_train_seq = tokenizer.texts_to_sequences(df_train['titulo'])
X_test_seq = tokenizer.texts_to_sequences(df_test['titulo'])
X_train_seq = pad_sequences(X_train_seq, maxlen=100)
X_test_seq = pad_sequences(X_test_seq, maxlen=100)

# Codificar las etiquetas
labelencoder = LabelEncoder()
y_train_seq = labelencoder.fit_transform(df_train['categoria'])

# Crear el modelo LSTM
model = Sequential()
model.add(Embedding(input_dim=5000, output_dim=100, input_length=100))
model.add(SpatialDropout1D(0.2))
model.add(Bidirectional(LSTM(64, return_sequences=False)))
model.add(Dense(32, activation='relu'))
model.add(Dense(5, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Añadir early stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

# Entrenar el modelo
model.fit(X_train_seq, y_train_seq, epochs=20, batch_size=64, verbose=2, validation_split=0.2, callbacks=[early_stopping])

# Predecir y evaluar
y_pred_lstm = model.predict(X_test_seq, verbose=0)
y_pred_lstm_labels = y_pred_lstm.argmax(axis=1)

# Convertir las predicciones a enteros
y_pred_logreg = y_pred_logreg.astype(int)
y_pred_rf = y_pred_rf.astype(int)
y_pred_lstm_labels = y_pred_lstm_labels.astype(int)

# Mapear los resultados a las categorías originales
mapping = {
    0: 'Entretenimiento',
    1: 'Deportes',
    2: 'Película y Animación',
    3: 'Educación',
    4: 'Otros'
}

# Mapear las predicciones a las categorías originales
y_pred_logreg = np.vectorize(mapping.get)(y_pred_logreg)
y_pred_rf = np.vectorize(mapping.get)(y_pred_rf)
y_pred_lstm_labels = np.vectorize(mapping.get)(y_pred_lstm_labels)

# Guardar las predicciones en un archivo CSV con columnas ID y Categoria
submission_logreg = pd.DataFrame({'ID': df_test['index'], 'Categoria': y_pred_logreg})
submission_rf = pd.DataFrame({'ID': df_test['index'], 'Categoria': y_pred_rf})
submission_lstm = pd.DataFrame({'ID': df_test['index'], 'Categoria': y_pred_lstm_labels})

submission_logreg.to_csv('submission_logreg.csv', index=False)
submission_rf.to_csv('submission_rf.csv', index=False)
submission_lstm.to_csv('submission_lstm.csv', index=False)

# Imprimir algunas predicciones de prueba
print("Predicciones de prueba (Logistic Regression):")
print(submission_logreg.head())
print("Predicciones de prueba (Random Forest):")
print(submission_rf.head())
print("Predicciones de prueba (LSTM):")
print(submission_lstm.head())

