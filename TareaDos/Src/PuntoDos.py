import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar el conjunto de datos
ruta_archivo = r'C:\Users\juanp\Downloads\TareaDos\Src\pruebas_saber_2023.xlsx'
df = pd.read_excel(ruta_archivo)

# Reemplazar NaN en las columnas 'ESTU_INSE_INDIVIDUAL' y 'ESTU_NSE_INDIVIDUAL' con la mediana
median_inse = df['ESTU_INSE_INDIVIDUAL'].median()
median_nse = df['ESTU_NSE_INDIVIDUAL'].median()
df.fillna({'ESTU_INSE_INDIVIDUAL': median_inse, 'ESTU_NSE_INDIVIDUAL': median_nse}, inplace=True)

# Identificar variables categóricas
categoricas = ['ESTU_COD_RESIDE_DEPTO', 'ESTU_COD_RESIDE_MCPIO', 'INST_COD_INSTITUCION', 'ESTU_SNIES_PRGMACADEMICO', 'ESTU_PRGM_CODMUNICIPIO', 
               'ESTU_INST_CODMUNICIPIO', 'ESTU_COD_MCPIO_PRESENTACION', 'ESTU_COD_DEPTO_PRESENTACION', 'ESTU_NSE_IES']

# Convertir variables categóricas en variables dummy
df = pd.get_dummies(df, columns=categoricas)

# Eliminar columnas no numéricas
df_numeric = df.select_dtypes(include=['number'])

# Mostrar las primeras filas y obtener información del DataFrame
print(df_numeric.head())
print(df_numeric.info())

# Estadísticas descriptivas
print(df_numeric.describe())

# Visualización de la distribución de la variable objetivo
plt.figure(figsize=(8, 6))
sns.histplot(df_numeric['MOD_LECTURA_CRITICA_PUNT'], bins=30, kde=True, color='blue')
plt.title('Distribución de Puntajes de Lectura Crítica')
plt.xlabel('Puntaje')
plt.ylabel('Frecuencia')
plt.show()

# Correlación entre variables
correlation_matrix = df_numeric.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlación')
plt.show()

# Dividir los datos en características (X) y etiquetas (y)
X = df_numeric.drop(columns=['MOD_LECTURA_CRITICA_PUNT'])  # características
y = df_numeric['MOD_LECTURA_CRITICA_PUNT']  # etiquetas

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verificar las formas de los conjuntos de datos
print("Forma de X_train:", X_train.shape)
print("Forma de X_test:", X_test.shape)
print("Forma de y_train:", y_train.shape)
print("Forma de y_test:", y_test.shape)

# Entrenar el modelo de regresión lineal
modelo_regresion_lineal = LinearRegression()
modelo_regresion_lineal.fit(X_train, y_train)

# Predecir en el conjunto de entrenamiento y calcular el error cuadrático medio
y_train_pred = modelo_regresion_lineal.predict(X_train)
mse_train = mean_squared_error(y_train, y_train_pred)
print("Error cuadrático medio en conjunto de entrenamiento:", mse_train)

# Predecir en el conjunto de prueba y calcular el error cuadrático medio
y_test_pred = modelo_regresion_lineal.predict(X_test)
mse_test = mean_squared_error(y_test, y_test_pred)
print("Error cuadrático medio en conjunto de prueba:", mse_test)
