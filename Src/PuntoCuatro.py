import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import norm
import numpy as np

# Cargar el dataset
cars_df = pd.read_csv('C:\\Users\\juanp\\Downloads\\TareaUnoVersionFinal\\Src\\CARS.csv')

# 4.1. Distribución de cada variable

# 4.1.1. Gráfico de barras para variables categóricas
categorical_vars = ['Make', 'Model', 'Type', 'Origin']
for var in categorical_vars:
    fig = px.bar(cars_df[var].value_counts(), title=f'Distribución de {var}')
    fig.show()

# 4.1.2. Histogramas para variables numéricas
numeric_vars = ['MPG_City', 'MPG_Highway', 'Weight', 'Wheelbase', 'Length', 'Price']
for var in numeric_vars:
    fig = px.histogram(cars_df, x=var, title=f'Histograma de {var}')
    fig.show()

# Detectar outliers en las variables numéricas
outliers = {}
for var in numeric_vars:
    mean = cars_df[var].mean()
    std = cars_df[var].std()
    threshold = 5 * std
    var_outliers = cars_df[(cars_df[var] > mean + threshold) | (cars_df[var] < mean - threshold)]['Model']
    outliers[var] = var_outliers.tolist()
    print(f"Modelos de carros que están más lejos de 5 desviaciones estándar en {var}:")
    print(var_outliers)

# Test de normalidad para variables numéricas
for var in numeric_vars:
    p_value = norm.sf(abs(cars_df[var].skew()))
    print(f"El p-value para la prueba de normalidad de {var} es: {p_value}")

# 4.2. Gráfico de la relación de cada variable con respecto a MPG_City

# 4.2.1. Boxplot para variables categóricas
for var in categorical_vars:
    fig = px.box(cars_df, x=var, y='MPG_City', title=f'Relación entre {var} y MPG_City')
    fig.show()

# 4.2.2. Scatter plot para variables numéricas
for var in numeric_vars:
    fig = px.scatter(cars_df, x=var, y='MPG_City', title=f'Relación entre {var} y MPG_City')
    fig.show()

# 4.3. Matriz de correlación

# 4.3.1. Matriz de correlación
correlation_matrix = cars_df.corr()
print("Matriz de correlación:")
print(correlation_matrix)

# 4.3.2. Dummy variables y matriz de correlación
dummy_df = pd.get_dummies(cars_df[categorical_vars])
correlation_matrix_with_dummy = pd.concat([cars_df[numeric_vars], dummy_df], axis=1).corr()
print("Matriz de correlación con dummy variables:")
print(correlation_matrix_with_dummy)

# 4.3.3. Matriz de correlación sin outliers
outlier_models = []
for outliers_list in outliers.values():
    outlier_models.extend(outliers_list)
outlier_models = list(set(outlier_models))

cars_df_no_outliers = cars_df[~cars_df['Model'].isin(outlier_models)]
correlation_matrix_no_outliers = cars_df_no_outliers.corr()
print("Matriz de correlación sin outliers:")
print(correlation_matrix_no_outliers)
