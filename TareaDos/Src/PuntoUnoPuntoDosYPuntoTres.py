# Utilizo pandas para leer los datos de un archivo Excel.
import numpy as np
import pandas as pd

class KMeans:
    def __init__(self, n_clusters=2, max_iter=300):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def fit(self, X):
        # Inicializar centroides aleatorios
        self.centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]

        # Iterar hasta convergencia o alcanzar el número máximo de iteraciones
        for _ in range(self.max_iter):
            # Asignar puntos al cluster más cercano
            labels = self.predict(X)

            # Actualizar centroides
            new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(self.n_clusters)])

            # Comprobar si los centroides han convergido
            if np.allclose(self.centroids, new_centroids):
                break

            self.centroids = new_centroids

    def predict(self, X):
        # Calcular la distancia de valor absoluto entre cada punto y cada centroide
        distances = np.abs(X[:, np.newaxis] - self.centroids)

        # Calcular la distancia mínima para cada punto
        min_distances = distances.sum(axis=2).argmin(axis=1)

        return min_distances

# Cargar datos desde el archivo Excel utilizando pandas
ruta_archivo = r'C:\Users\juanp\Downloads\TareaDos\Doc\PuntoUnoPuntoUno.xlsx'
df = pd.read_excel(ruta_archivo)

# Eliminar la columna de nombres de instituciones para obtener solo los puntajes
X = df.drop(columns=['INST_NOMBRE_INSTITUCION']).to_numpy()

# Crear y ajustar el modelo KMeans con 5 clusters
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)

# Asignar significados a los clusters
nombres_clusters = {
    0: "Alto Rendimiento Académico",
    1: "Rendimiento Académico Bueno",
    2: "Rendimiento Académico Medio",
    3: "Rendimiento Académico Bajo",
    4: "Rendimiento Académico Muy Bajo"
}

# Imprimir los resultados
for i, centroid in enumerate(kmeans.centroids):
    print(f"Cluster {i+1} Centroide:")
    print(centroid)
    print("Primera Institución:", df.iloc[i]['INST_NOMBRE_INSTITUCION'])
    print("Segunda Institución:", df.iloc[i+1]['INST_NOMBRE_INSTITUCION'])
    print("Significado del Cluster:", nombres_clusters[i])
    print()
