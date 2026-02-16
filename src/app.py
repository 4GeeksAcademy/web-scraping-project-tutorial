import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import io
import pandas as pd


 # Paso 2 Descargar el HTML
url = "https://en.wikipedia.org/wiki/List_of_Spotify_streaming_records"
response = requests.get(url)
# Verificar la respuesta
print("Estado:", response.status_code)

# Paso 3: Transforma el HTML al Extraer las tablas con pandas
html = io.StringIO(response.text)
tables = pd.read_html(html)
print(f"Se encontraron {len(tables)} tablas.")

#Paso 4: Procesar el DataFrame
# Limpieza de datos

df.columns = ["Rank", "Song", "Artist", "Streams (billions)", "Date released", "Reference"]

# Se eliminan notas entre corchetes
df["Song"] = df["Song"].str.replace(r"\[.*?\]", "", regex=True)
df["Artist"] = df["Artist"].str.replace(r"\[.*?\]", "", regex=True)

df = df[df["Streams (billions)"].astype(str).str.contains(r"^\d+(?:\.\d+)?$", na=False)].copy()

# Se convierten Streams a números flotantes
df["Streams (billions)"] = df["Streams (billions)"].astype(float)

# Se convierten fechas a datetime
df["Date released"] = pd.to_datetime(df["Date released"], errors="coerce")

df

#Paso 5: Se almacenan los datos en sqlite

# Create the database
conn = sqlite3.connect("spotify_top_songs.db")
# Create table in SQLite
df.to_sql("most_streamed", conn, if_exists="replace", index=False)
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM most_streamed")
print("Rows inserted:", cursor.fetchone()[0])

conn.commit()
conn.close()

#Paso 6: Visualizar los datos

# Gráfico 1: Las 10 canciones más reproducidas
top10 = df.nlargest(10, "Streams (billions)")
plt.figure(figsize=(12, 6))
sns.barplot(data=top10, x="Streams (billions)", y="Song", hue="Song", palette="viridis", legend=False)
plt.title("Las 10 canciones más reproducidas en Spotify")
plt.xlabel("Reproducciones (en miles de millones)")
plt.ylabel("Canción")
plt.tight_layout()
plt.show()
