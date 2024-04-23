import matplotlib.pyplot as plt

# Datos
pib_millones = [1067855.672, 212514957.4, 8548114.653, 63764770.77, 357258620.8, 51404352.37, 38858162.12, 23953112.45,
                5461366.78, 23660657.37, 25758151.71, 37523918.98, 6001844.915, 24991953.76, 91945942.28, 497704.0127,
                1123857.696, 24011616.06, 22262575.88, 19738417.36, 58439500.07, 21775426.15, 23056874.23, 5616558.269,
                11941644.16, 23786362.42, 2125410.333, 92276678.16, 11516270.76, 30438180.15, 139863153.5, 381851.6785,
                956576.6785]

poblacion = [76589, 6407102, 262174, 2535517, 7412566, 2070110, 1217376, 998255, 401849, 420504, 1464488, 1200574, 534826,
             1784783, 2919060, 48114, 82767, 1100386, 880560, 1341746, 1039722, 1630592, 1491689, 348182, 539904, 943401,
             61280, 2184837, 904863, 1330187, 4475886, 40797, 107808]

pib_percapita = [13.94267678, 33.16865524, 32.60473828, 25.1486268, 48.19634938, 24.83170091, 31.91960588, 23.9949837,
                 13.59059443, 56.26737766, 17.58850309, 31.25498218, 11.2220515, 14.00279685, 31.49847632, 10.34426597,
                 13.57857232, 21.82108466, 25.28229295, 14.710994, 56.20685151, 13.35430699, 15.45689097, 16.13109888,
                 22.11808795, 25.21341659, 34.68358898, 42.23504003, 12.7270877, 22.8826324, 31.2481492, 9.359797989,
                 8.872965629]

# Función para calcular cuartiles y whiskers
def calcular_cuartiles(datos):
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    
    q1_index = (n + 1) // 4
    q2_index = 2 * q1_index
    q3_index = 3 * q1_index
    
    q1 = (datos_ordenados[q1_index - 1] + datos_ordenados[q1_index]) / 2
    q2 = (datos_ordenados[q2_index - 1] + datos_ordenados[q2_index]) / 2
    q3 = (datos_ordenados[q3_index - 1] + datos_ordenados[q3_index]) / 2
    
    iqr = q3 - q1
    whisker_superior = q3 + 1.5 * iqr
    whisker_inferior = q1 - 1.5 * iqr
    
    return q1, q2, q3, iqr, whisker_superior, whisker_inferior

# Calcular cuartiles y whiskers para PIB
q1_pib, q2_pib, q3_pib, iqr_pib, whisker_superior_pib, whisker_inferior_pib = calcular_cuartiles(pib_millones)

# Crear boxplot para PIB
plt.figure(figsize=(8, 6))
plt.boxplot(pib_millones, labels=['PIB'])
plt.title("Boxplot para PIB")
plt.show()

# Calcular cuartiles y whiskers para Población
q1_poblacion, q2_poblacion, q3_poblacion, iqr_poblacion, whisker_superior_poblacion, whisker_inferior_poblacion = calcular_cuartiles(poblacion)

# Crear boxplot para Población
plt.figure(figsize=(8, 6))
plt.boxplot(poblacion, labels=['Poblacion'])
plt.title("Boxplot para Poblacion")
plt.show()

# Calcular cuartiles y whiskers para PIB per cápita
q1_pib_percapita, q2_pib_percapita, q3_pib_percapita, iqr_pib_percapita, whisker_superior_pib_percapita, whisker_inferior_pib_percapita = calcular_cuartiles(pib_percapita)

# Crear boxplot para PIB per cápita
plt.figure(figsize=(8, 6))
plt.boxplot(pib_percapita, labels=['PIB per cápita'])
plt.title("Boxplot para PIB per cápita")
plt.show()
