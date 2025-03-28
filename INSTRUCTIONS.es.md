# Web scraping

En este proyecto, vamos a recolectar, procesar y visualizar datos desde una página web real. Tienes la libertad de elegir el sitio web que más te interese (siempre que sea apto para scraping básico), o utilizar la propuesta sugerida.

### ¿Qué sitio web puedes usar?

**Opción A:** Sitio web de tu elección

Puedes elegir cualquier página que contenga datos visibles en el HTML y que sean de tu interes.

> 💡 **IMPORTANTE:** Para que la practica pueda ser llevada a cabo de una forma viable, ten en cuenta lo siguiente:

- Los datos deben ser visibles al ver el código fuente (clic derecho → "Ver código fuente").

- El sitio no debe requerir inicio de sesión ni usar JavaScript para cargar el contenido.

- La estructura debe ser simple y repetitiva (tablas o listas).

**Opción B:** Propuesta sugerida – Wikipedia: Canciones más reproducidas en Spotify 🎧

Si prefieres no buscar un sitio por tu cuenta, puedes usar esta tabla de Wikipedia: [Canciones más reproducidas en Spotify](https://en.wikipedia.org/wiki/List_of_most-streamed_songs_on_Spotify)

Contiene información sobre:

- Título de la canción

- Artista

- Reproducciones

- Año de lanzamiento

Es una excelente opción para practicar scraping con tablas.

## Paso 1: Instalación de dependencias

Asegúrate de que tienes instalados los paquetes `pandas` y `requests` de Python para poder trabajar en el proyecto. En el caso de que no tengas las librerías instaladas, ejecuta en la consola:

```bash
pip install pandas requests lxml
```

## Paso 2: Descargar HTML

La descarga del HTML de la página web se realizará con la librería `requests`, como vimos en la teoría del módulo.

La página web que queremos scrapear es la siguiente: [https://en.wikipedia.org/wiki/List_of_most-streamed_songs_on_Spotify](https://en.wikipedia.org/wiki/List_of_most-streamed_songs_on_Spotify). Recopila y almacena información y guarda el texto scrapeado de la web en alguna variable.


## Paso 3: Transforma el HTML


Con `BeautifulSoup`, analizá el HTML para encontrar la estructura que contiene los datos (por ejemplo: `<table>`, `<li>`, `<div>`, etc.).

Si usás Wikipedia y contiene una tabla, podés usar directamente `pandas.read_html()` para cargarla como DataFrame.


## Paso 4: Procesa el DataFrame

A continuación, limpia las filas para obtener los valores limpios eliminando `$` y `B`. Elimina también aquellas que estén vacías o no tengan información.


## Paso 5: Almacena los datos en sqlite

Crea una instancia vacía de la base de datos e incluye en ella los datos limpios, como vimos en el módulo de bases de datos. Una vez tengas una base de datos vacía:

1. Crea la tabla.
2. Inserta los valores.
3. Almacena (`commit`) los cambios.


## Paso 6: Visualiza los datos (opcional, pero muy recomendado)

Si aún no has revisado los conceptos y prácticas de visualización, no te preocupes. Intenta hacer que esto funcione, y exploraremos la visualización en detalle en los próximos proyectos.

¿Qué tipos de visualizaciones podemos realizar? Propón al menos 3 y muéstralos.


## ¿Te sientes confiado/a? 😎

### Monitoreo diario del ranking musical - Versión extendida para estudiantes con confianza

Si te sientes confiado/a y quieres profundizar en el uso de scraping y análisis temporal de datos, te proponemos realizar esta version extendida y opcional del proyecto, que te ayudará a conectar scraping, análisis de datos reales y visibilidad profesional, lo cual será ideal para mostrar en LinkedIn o un portafolio.

La idea es obtener información diaria del ranking musical (como el top 100 de canciones en Spotify desde Wikipedia) y estudiar tendencias reales a lo largo del tiempo.


### Propuesta 🚀

1. **Scraper diario:** Usa el scraper del proyecto original. Programalo para que se ejecute a diario (puede usarse cron en Linux/Mac o Task Scheduler en Windows).

    Almacena los datos en una base SQLite, agregando una columna `date` con el día de ejecución.

2. **Base de datos:** Crea una tabla llamada `daily_rankings` que contenga las siguientes columnas:

    - scraping_date
    - rank
    - song
    - artist
    - streams
    - release_year


3. **Visualizaciones sugeridas:**

    - Evolución de una canción a lo largo de los días
    - Tiempo promedio en el top 10, top 50 o top 100
    - Artistas con más entradas y mayor duración promedio

4. **Haz visible tu trabajo:** Publica en LinkedIn tu trabajo. Haz el seguimiento por al menos 2 semanas y publica una visualización o hallazgo diariamente o cada 2-3 días; usa notebooks, dashboards o posts gráficos para compartir lo aprendido.

A continuación te sugerimos una posible publicación, para tu LinkedIn:


> Entre mis primeros proyectos como Data Scientist, hoy empecé a monitorear diariamente el 
> ranking de las canciones más escuchadas en Spotify. Revisar estos rankings es clave para 
> entender muchísimo sobre cómo se mueve el dinero, el marketing y las tendencias en la industria
> musical.
>
> Ire compartiendo mis visualizaciones e insights en los próximos días.
>
> ¡La música también se puede estudiar con datos! 🎶📊
>
> **#DataScience #Spotify #WebScraping #TendenciasMusicales**
