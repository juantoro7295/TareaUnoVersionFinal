# Datos 
departamentos = ['Amazonas', 'Antioquia', 'Arauca', 'Atlántico', 'Bogotá D.C.', 'Bolívar', 'Boyacá', 'Caldas',
                  'Caquetá', 'Casanare', 'Cauca', 'Cesar', 'Chocó', 'Córdoba', 'Cundinamarca', 'Guainía', 'Guaviare',
                  'Huila', 'La Guajira', 'Magdalena', 'Meta', 'Nariño', 'Norte de Santander', 'Putumayo', 'Quindío',
                  'Risaralda', 'San Andrés, Providencia y Santa Catalina', 'Santander', 'Sucre', 'Tolima',
                  'Valle del Cauca', 'Vaupés', 'Vichada']

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

# Cálculos
def calcular_media(datos):
    return sum(datos) / len(datos)

def calcular_mediana(datos):
    datos_ordenados = sorted(datos)
    n = len(datos)
    
    if n % 2 == 0:
        return (datos_ordenados[n // 2 - 1] + datos_ordenados[n // 2]) / 2
    else:
        return datos_ordenados[n // 2]

def calcular_desviacion_estandar(datos):
    media = calcular_media(datos)
    n = len(datos)
    suma_cuadrados = sum((x - media) ** 2 for x in datos)
    
    return (suma_cuadrados / (n - 1)) ** 0.5

# Aplicar funciones a los datos
media_pib = calcular_media(pib_millones)
mediana_pib = calcular_mediana(pib_millones)
desviacion_estandar_pib = calcular_desviacion_estandar(pib_millones)

media_poblacion = calcular_media(poblacion)
mediana_poblacion = calcular_mediana(poblacion)
desviacion_estandar_poblacion = calcular_desviacion_estandar(poblacion)

media_pib_percapita = calcular_media(pib_percapita)
mediana_pib_percapita = calcular_mediana(pib_percapita)
desviacion_estandar_pib_percapita = calcular_desviacion_estandar(pib_percapita)

# Imprimir resultados

#x1
print("Resultados para PIB:")
print(f"Media: {media_pib}")
print(f"Mediana: {mediana_pib}")
print(f"Desviación Estándar: {desviacion_estandar_pib}")

#x2
print("\nResultados para Población:")
print(f"Media: {media_poblacion}")
print(f"Mediana: {mediana_poblacion}")
print(f"Desviación Estándar: {desviacion_estandar_poblacion}")

#x3
print("\nResultados para PIB per cápita:")
print(f"Media: {media_pib_percapita}")
print(f"Mediana: {mediana_pib_percapita}")
print(f"Desviación Estándar: {desviacion_estandar_pib_percapita}")
