import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

# Cargar el conjunto de datos
ruta_archivo = r'C:\Users\juanp\Downloads\TareaDos\Src\pruebas_saber_2023.xlsx'
df = pd.read_excel(ruta_archivo)

# Reemplazar NaN en las columnas 'ESTU_INSE_INDIVIDUAL' y 'ESTU_NSE_INDIVIDUAL' con la mediana
median_inse = df['ESTU_INSE_INDIVIDUAL'].median()
median_nse = df['ESTU_NSE_INDIVIDUAL'].median()
df.fillna({'ESTU_INSE_INDIVIDUAL': median_inse, 'ESTU_NSE_INDIVIDUAL': median_nse}, inplace=True)

# Eliminar columnas no numéricas
df_numeric = df[['PERIODO', 'MOD_LECTURA_CRITICA_PUNT', 'ESTU_INSE_INDIVIDUAL', 'ESTU_NSE_INDIVIDUAL']]

# Dividir los datos en características (X) y etiquetas (y)
X = df_numeric.drop(columns=['MOD_LECTURA_CRITICA_PUNT'])  # características
y = df_numeric['MOD_LECTURA_CRITICA_PUNT']  # etiquetas

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelos KNN con diferentes números de vecinos
for n_neighbors in [5, 10, 20, 30]:
    # Crear y entrenar el modelo de KNN
    knn_model = KNeighborsRegressor(n_neighbors=n_neighbors)
    knn_model.fit(X_train, y_train)
    
    # Predecir en el conjunto de entrenamiento y calcular el MSE
    y_train_pred = knn_model.predict(X_train)
    mse_train = mean_squared_error(y_train, y_train_pred)
    
    # Predecir en el conjunto de prueba y calcular el MSE
    y_test_pred = knn_model.predict(X_test)
    mse_test = mean_squared_error(y_test, y_test_pred)
    
    # Imprimir resultados
    print(f"Número de vecinos: {n_neighbors}")
    print(f"MSE Entrenamiento: {mse_train}")
    print(f"MSE Prueba: {mse_test}")
    print("---")
