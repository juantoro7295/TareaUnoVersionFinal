# Datos
datos = [
    [1067855.672, 76589, 13.94267678],
    [212514957.4, 6407102, 33.16865524],
    [8548114.653, 262174, 32.60473828],
    [63764770.77, 2535517, 25.1486268],
    [357258620.8, 7412566, 48.19634938],
    [51404352.37, 2070110, 24.83170091],
    [38858162.12, 1217376, 31.91960588],
    [23953112.45, 998255, 23.9949837],
    [5461366.78, 401849, 13.59059443],
    [23660657.37, 420504, 56.26737766],
    [25758151.71, 1464488, 17.58850309],
    [37523918.98, 1200574, 31.25498218],
    [6001844.915, 534826, 11.2220515],
    [24991953.76, 1784783, 14.00279685],
    [91945942.28, 2919060, 31.49847632],
    [497704.0127, 48114, 10.34426597],
    [1123857.696, 82767, 13.57857232],
    [24011616.06, 1100386, 21.82108466],
    [22262575.88, 880560, 25.28229295],
    [19738417.36, 1341746, 14.710994],
    [58439500.07, 1039722, 56.20685151],
    [21775426.15, 1630592, 13.35430699],
    [23056874.23, 1491689, 15.45689097],
    [5616558.269, 348182, 16.13109888],
    [11941644.16, 539904, 22.11808795],
    [23786362.42, 943401, 25.21341659],
    [2125410.333, 61280, 34.68358898],
    [92276678.16, 2184837, 42.23504003],
    [11516270.76, 904863, 12.7270877],
    [30438180.15, 1330187, 22.8826324],
    [139863153.5, 4475886, 31.2481492],
    [381851.6785, 40797, 9.359797989],
    [956576.6785, 107808, 8.872965629]
]

# Número de clusters (K)
k = 4

# en los  centroides seleccionamos puntos aleatorios del conjunto de datos
centroides = datos[:k]

# Iteraciones
for _ in range(10):  # Número  de iteraciones 
    # Inicializar clusters
    clusters = [[] for _ in range(k)]

    # Asignación a clusters
    for punto in datos:
        distancias = [sum((p - c)**2 for p, c in zip(punto, centroide))**0.5 for centroide in centroides]
        cluster_asignado = distancias.index(min(distancias))
        clusters[cluster_asignado].append(punto)

    # Actualización de centroides
    nuevos_centroides = [[sum(p[i] for p in cluster) / len(cluster) for i in range(3)] for cluster in clusters]

    # Verificar si los centroides no cambian significativamente
    if nuevos_centroides == centroides:
        break

    # Actualizar centroides para la siguiente iteración
    centroides = nuevos_centroides

# Imprimir los resultados
for i, cluster in enumerate(clusters):
    print(f"Cluster {i + 1}: {cluster}")
