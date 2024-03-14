import numpy as np

# Datos
datos = np.array([
    [1067855.672, 76589],
    [212514957.4, 6407102],
    [8548114.653, 262174],
    [63764770.77, 2535517],
    [357258620.8, 7412566],
    [51404352.37, 2070110],
    [38858162.12, 1217376],
    [23953112.45, 998255],
    [5461366.78, 401849],
    [23660657.37, 420504],
    [25758151.71, 1464488],
    [37523918.98, 1200574],
    [6001844.915, 534826],
    [24991953.76, 1784783],
    [91945942.28, 2919060],
    [497704.0127, 48114],
    [1123857.696, 82767],
    [24011616.06, 1100386],
    [22262575.88, 880560],
    [19738417.36, 1341746],
    [58439500.07, 1039722],
    [21775426.15, 1630592],
    [23056874.23, 1491689],
    [5616558.269, 348182],
    [11941644.16, 539904],
    [23786362.42, 943401],
    [2125410.333, 61280],
    [92276678.16, 2184837],
    [11516270.76, 904863],
    [30438180.15, 1330187],
    [139863153.5, 4475886],
    [381851.6785, 40797],
    [956576.6785, 107808]
])

# 2.1. Cual es la matriz de covarianza

cov_mat = np.cov(datos, rowvar=False)

# 2.2. Cuales son los eigenvalues y 2.4. Cual es el valor del eigenvector
eigenvalues, eigenvectors = np.linalg.eig(cov_mat)

# 2.3. Cuál es la varianza explicada por el eigenvalue 
principal_component = eigenvectors[:, np.argmax(eigenvalues)]

# 2.5. Cuál es la matriz proyectada.

projected_data = np.dot(datos, principal_component)

#2.6. Cual es el error o diferencia entre la matriz proyectada
error = np.mean(np.abs(np.dot(projected_data[:, np.newaxis], principal_component[:, np.newaxis].T) - datos))

#resultados
print("Matriz de Covarianza:")
print(cov_mat)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)
print("\nComponente Principal:")
print(principal_component)
print("\nMatriz Proyectada:")
print(projected_data)
print("\nError:")
print(error)
