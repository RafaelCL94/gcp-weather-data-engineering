import os

print("Iniciando pipeline...")

os.system("python ingestion/extract_weather.py")
os.system("python processing/transform_weather.py")
os.system("python load/load_bigquery.py")

print("Pipeline finalizado com sucesso!")