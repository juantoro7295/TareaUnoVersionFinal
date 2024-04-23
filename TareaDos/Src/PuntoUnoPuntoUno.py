import pandas as pd

# Establecer la opción para mostrar todas las filas
pd.set_option('display.max_rows', None)

# Cargar y procesar el DataFrame
ruta_archivo = r'C:\Users\juanp\Downloads\TareaDos\Src\InstitucionesPuntajes.xlsx'
df = pd.read_excel(ruta_archivo)

# Calcular el promedio por institución educativa de los puntajes por cada competencia
promedio_por_institucion = df.groupby('INST_NOMBRE_INSTITUCION').agg({
    'MOD_LECTURA_CRITICA_PUNT': 'mean',
    'MOD_COMPETEN_CIUDADA_PUNT': 'mean',
    'MOD_INGLES_PUNT': 'mean',
    'MOD_COMUNI_ESCRITA_PUNT': 'mean',
    'PUNT_GLOBAL': 'mean'
}).reset_index()

# Guardar el resultado en un archivo Excel
ruta_salida = r'C:\Users\juanp\Downloads\TareaDos\Doc\PuntoUnoPuntoUno.xlsx'
promedio_por_institucion.to_excel(ruta_salida, index=False)

print("Archivo guardado exitosamente como PuntoUnoPuntoUno.xlsx")
