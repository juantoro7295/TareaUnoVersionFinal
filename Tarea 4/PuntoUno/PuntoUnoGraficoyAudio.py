import math
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# Cargar el archivo de entrenamiento localmente
file_name_train = "train.csv"  
train_data = pd.read_csv(file_name_train)

# Cargar el archivo de test localmente
file_name_test = "test.csv"  
test_data = pd.read_csv(file_name_test)

# Definir la función de predicción
def y_predict(a, b, c, x):
    return a * np.cos(b * x + c)

# Hiperparámetros
lr = 0.05
batch = 100
epochs = 3000

# Extraer los datos de entrenamiento
X_train = train_data['x'].values
Y_train = train_data['TARGET'].values

# Inicializar parámetros
a = random.random()
b = random.random()
c = random.random()
d = 0

# Gradiente descendente
rsl = []  # Lista para guardar los resultados de cada epoch
for epoch in range(epochs):
    a_gradiente = 0
    b_gradiente = 0
    c_gradiente = 0
    e = 0

    for _ in range(batch):
        ix = int(random.uniform(0, len(X_train)))
        y_hat = y_predict(a, b, c, X_train[ix])
        error = Y_train[ix] - y_hat
        e += error ** 2

        a_gradiente += -2 * error * np.cos(b * X_train[ix] + c)
        b_gradiente += 2 * error * a * X_train[ix] * np.sin(b * X_train[ix] + c)
        c_gradiente += 2 * error * a * np.sin(b * X_train[ix] + c)

    a -= lr * a_gradiente / batch
    b -= lr * b_gradiente / batch
    c -= lr * c_gradiente / batch

    e = e / batch
    rsl.append([a, b, c, e])  # Guardar los parámetros y el error en cada epoch

# Resultados finales
print(f"Final parameters: a = {a}, b = {b}, c = {c}")

# Visualización de los resultados
epochs_to_plot = [10, 400, 1000, 2000]
for epoch in epochs_to_plot:
    if epoch < len(rsl): 
        a, b, c, _ = rsl[epoch]
        y_pred = y_predict(a, b, c, X_train)
        plt.figure()
        plt.scatter(X_train, Y_train, label='Datos originales')
        plt.plot(X_train, y_pred, color='blue', label='Predicción')
        plt.title(f'Epoch {epoch}')
        plt.legend()
        plt.show()
    else:
        print(f"Epoch {epoch} no disponible. Número máximo de epochs completados: {len(rsl) - 1}")  # Mensaje 



# Guardar la señal como un archivo de audio WAV
x_min = min(X_train)
long_s = [y_predict(a, b, c, xi) for xi in np.arange(x_min, 20 * math.pi, 0.001).astype(np.float32)]
sf.write('output.wav', long_s, 44100)  # Guardar el archivo de audio
print("La señal ha sido guardada en 'output.wav'")
