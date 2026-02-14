# John fredy beltran cuellar
# Date:08/31/2025
# Goal: realizar el proyecto web scraping

import pandas  as pd
import matplotlib.pyplot as plt
import requests
import os
import seaborn as sns
import time
import sqlite3
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Spotify_streaming_records"
headers = {"User-Agent": "Mozilla/5.0"} # header simple para poder acceder
response = requests.get(url, headers=headers) # obtener HTML con requests

tables = pd.read_html(response.text) # pasar el HTML a pandas

print(f"tablas encontradas: {len(tables)}") # ver cuantas tablas hay

df = tables[0] # mostrar la primera tabla
print(df.head())

# preprocesing
df = df.drop(columns=['Ref.'], errors="ignore") # elimina columna no deseada
df.columns = df.columns.str.strip() # quita espacios
df = df.rename(columns={    # renombra las columnas
    "Streams (billions)": "streams_billions",
    "Artist(s)": "artists",
    "Release date": "release_date",
    "Rank": "rank",
    "Song": "song"
})
df.head()
df["streams_billions"] = df["streams_billions"].astype(
    str).str.replace(",", "", regex=False) # quita las comas y convierte a float y pone nan donde no se pueda
df["streams_billions"] = pd.to_numeric(df["streams_billions"], errors="coerce")
df["rank"] = pd.to_numeric(df["rank"], errors="coerce") # conviente a rank a int
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce") # convertir fecha a datatime
df["song"] = df["song"].str.strip('"\'') # quita las comillas en el titulo de las canciones

conn = sqlite3.connect("spotify_records.db") # abrir coneccion
df.to_sql("most_streamed", conn, if_exists="replace", index=False)
cursor = conn.cursor()
df_sql = pd.read_sql_query("SELECT * FROM most_streamed LIMIT 5", conn)
print(df_sql)
conn.commit() # guardar cambios
conn.close()


 # Extraer el año de lanzamiento
df["release_year"] = df["release_date"].dt.year
# Contar cuántas canciones hay por año
songs_by_year = df.groupby("release_year")["song"].count().reset_index()

# grafica el resultado de canciones en el ranking por año
plt.bar(songs_by_year["release_year"], songs_by_year["song"])
plt.xlabel("release_year")
plt.ylabel("song")
plt.title("Number of Songs in the Ranking by Release Year")
plt.show()

# Ordenar por streams y quedarnos con las 10 más altas
top10 = df.sort_values(by="streams_billions", ascending=False).head(10)
# Hacer la gráfica de barras
plt.figure(figsize=(10,6))
plt.barh(top10["song"], top10["streams_billions"], color="skyblue")
plt.xlabel("streams (billions)")
plt.ylabel("song")
plt.title("Top 10 Most Streamed Songs")
plt.gca().invert_yaxis()  # Para que la más reproducida quede arriba
plt.show()


# Contar cuántas canciones tiene cada artista en el ranking
artist_counts = df["artists"].value_counts()

# Mostrar los 10 artistas con más canciones
print(artist_counts.head(10))

# Gráfica de barras horizontales
plt.figure(figsize=(10,6))
plt.barh(artist_counts.index[:10], artist_counts.values[:10], color="coral")
plt.xlabel("Número de Canciones")
plt.ylabel("artists")
plt.title("Artistas con más canciones en el ranking")
plt.gca().invert_yaxis() # para que el top quede arriba
plt.show()


