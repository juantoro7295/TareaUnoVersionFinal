# Datos
pib_millones = [1067855.672, 212514957.4, 8548114.653, 63764770.77, 357258620.8, 51404352.37, 38858162.12, 23953112.45,
                5461366.78, 23660657.37, 25758151.71, 37523918.98, 6001844.915, 24991953.76, 91945942.28, 497704.0127,
                1123857.696, 24011616.06, 22262575.88, 19738417.36, 58439500.07, 21775426.15, 23056874.23, 5616558.269,
                11941644.16, 23786362.42, 2125410.333, 92276678.16, 11516270.76, 30438180.15, 139863153.5, 381851.6785,
                956576.6785]

poblacion = [76589, 6407102, 262174, 2535517, 7412566, 2070110, 1217376, 998255, 401849, 420504, 1464488, 1200574, 534826,
             1784783, 2919060, 48114, 82767, 1100386, 880560, 1341746, 1039722, 1630592, 1491689, 348182, 539904, 943401,
             61280, 2184837, 904863, 1330187, 4475886, 40797, 107808]

# Calcular medias
media_pib = sum(pib_millones) / len(pib_millones)
media_poblacion = sum(poblacion) / len(poblacion)

# Calcular covarianza
covarianza = sum((pib - media_pib) * (pobl - media_poblacion) for pib, pobl in zip(pib_millones, poblacion)) / len(pib_millones)

# Calcular desviaciones estándar
std_pib = (sum((pib - media_pib)**2 for pib in pib_millones) / len(pib_millones))**0.5
std_poblacion = (sum((pobl - media_poblacion)**2 for pobl in poblacion) / len(poblacion))**0.5

# Calcular correlación
correlacion = covarianza / (std_pib * std_poblacion)

# Imprimir resultados
print(f"Correlación entre PIB Millones y Población: {correlacion}")
