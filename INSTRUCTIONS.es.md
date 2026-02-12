# Web scraping

En este proyecto, vamos a recolectar, procesar y visualizar datos desde una página web real. Tienes la libertad de elegir el sitio web que más te interese (siempre que sea apto para scraping básico), o utilizar la propuesta sugerida.

### ¿Qué sitio web puedes usar?

**Opción A:** Sitio web de tu elección

Puedes elegir cualquier página que contenga datos visibles en el HTML y que sean de tu interes.

> 💡 **IMPORTANTE:** Para que la practica pueda ser llevada a cabo de una forma viable, ten en cuenta lo siguiente:

- Los datos deben ser visibles al ver el código fuente (clic derecho → "Ver código fuente").

- El sitio no debe requerir inicio de sesión ni usar JavaScript para cargar el contenido.

- La estructura debe ser simple y repetitiva (tablas o listas).

**Opción B:** Propuesta sugerida – Scrapthissite.com

Si prefieres no buscar un sitio por tu cuenta, puedes usar web hecha específicamente para ello:
(https://www.scrapethissite.com/)

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

A continuación, limpia las filas para obtener los valores que necesites. Elimina también aquellas que estén vacías o no tengan información.


## Paso 5: Almacena los datos en sqlite

Crea una instancia vacía de la base de datos e incluye en ella los datos limpios, como vimos en el módulo de bases de datos. Una vez tengas una base de datos vacía:

1. Crea la tabla.
2. Inserta los valores.
3. Almacena (`commit`) los cambios.


## Paso 6: Visualiza los datos (opcional, pero muy recomendado)

Si aún no has revisado los conceptos y prácticas de visualización, no te preocupes. Intenta hacer que esto funcione, y exploraremos la visualización en detalle en los próximos proyectos.

¿Qué tipos de visualizaciones podemos realizar? Propón al menos 3 y muéstralos.
