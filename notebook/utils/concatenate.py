import os
import pandas as pd

# Directorio donde se encuentran los archivos CSV
directory = r"f:\projects\data_analitics\clusterdata\cluster-trace-gpu-v2023\csv"

# Lista para almacenar los DataFrames
dataframes = []

# Iterar sobre los archivos en el directorio
for filename in os.listdir(directory):
    if filename.startswith("openb_pod_list_") and "gpushare" not in filename and filename.endswith(".csv"):
        filepath = os.path.join(directory, filename)
        print(f"Leyendo archivo: {filename}")
        # Leer el archivo CSV
        df = pd.read_csv(filepath)
        # Agregar una columna con el nombre del archivo
        df['source_file'] = filename
        # Agregar el DataFrame a la lista
        dataframes.append(df)

# Concatenar todos los DataFrames
concatenated_df = pd.concat(dataframes, ignore_index=True)

# Guardar el archivo concatenado
output_file = os.path.join(directory, "concatenated_openb_pod_list.csv")
concatenated_df.to_csv(output_file, index=False)
print(f"Archivos concatenados guardados en: {output_file}")