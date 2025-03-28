# Web Scraping

In this project, we will collect, process, and visualize data from a real web page. You are free to choose the website that interests you the most (as long as it is suitable for basic scraping) or use the suggested option.

### Which website can you use?

**Option A:** Website of your choice

You can choose any page that contains visible data in the HTML and is of interest to you.

> 💡 **IMPORTANT:** To ensure the practice can be carried out effectively, keep the following in mind:

- The data must be visible when viewing the source code (right-click → "View page source").

- The site should not require login or use JavaScript to load the content.

- The structure should be simple and repetitive (tables or lists).

**Option B:** Suggested option – Wikipedia: Most-Streamed Songs on Spotify 🎧

If you prefer not to search for a site on your own, you can use this Wikipedia table: [Most-Streamed Songs on Spotify](https://en.wikipedia.org/wiki/List_of_most-streamed_songs_on_Spotify)

It contains information about:

- Song title

- Artist

- Streams

- Release year

This is an excellent option for practicing table scraping.

## Step 1: Install dependencies

Make sure you have the Python packages `pandas` and `requests` installed to work on the project. If you don't have these libraries installed, run the following in the console:

```bash
pip install pandas requests lxml
```

## Step 2: Download HTML

The HTML of the web page will be downloaded using the `requests` library, as we saw in the module's theory.

The web page we want to scrape is the following: [https://en.wikipedia.org/wiki/List_of_most-streamed_songs_on_Spotify](https://en.wikipedia.org/wiki/List_of_most-streamed_songs_on_Spotify). Collect and store the scraped text from the web in a variable.

## Step 3: Transform the HTML

Using `BeautifulSoup`, analyze the HTML to find the structure containing the data (e.g., `<table>`, `<li>`, `<div>`, etc.).

If you are using Wikipedia and it contains a table, you can directly use `pandas.read_html()` to load it as a DataFrame.

## Step 4: Process the DataFrame

Next, clean the rows to obtain clean values by removing `$` and `B`. Also, remove any rows that are empty or lack information.

## Step 5: Store the data in SQLite

Create an empty database instance and include the cleaned data in it, as we saw in the database module. Once you have an empty database:

1. Create the table.
2. Insert the values.
3. Commit the changes.

## Step 6: Visualize the data (optional, but highly recommended)

If you haven’t gone through the visualization concepts and practices yet, don’t worry. Try making this work, and we’ll explore visualization in depth in the next few projects.

What types of visualizations can we make? Suggest at least 3 and plot them.


## Do You Feel Confident? 😎

### Daily Monitoring of Music Rankings - Extended Version for Confident Students

If you feel confident and want to deepen your skills in web scraping and temporal data analysis, we propose this extended and optional version of the project. It will help you connect scraping, real data analysis, and professional visibility, making it ideal to showcase on LinkedIn or in a portfolio.

The idea is to collect daily information about music rankings (such as Spotify's top 100 songs from Wikipedia) and study real trends over time.

### Proposal 🚀

1. **Daily Scraper:** Use the scraper from the original project. Schedule it to run daily (you can use cron on Linux/Mac or Task Scheduler on Windows).

    Store the data in an SQLite database, adding a `date` column with the execution day.

2. **Database:** Create a table called `daily_rankings` with the following columns:

    - scraping_date
    - rank
    - song
    - artist
    - streams
    - release_year

3. **Suggested Visualizations:**

    - Evolution of a song over time
    - Average time spent in the top 10, top 50, or top 100
    - Artists with the most entries and highest average duration

4. **Make Your Work Visible:** Share your work on LinkedIn. Track the data for at least 2 weeks and publish a visualization or insight daily or every 2-3 days. Use notebooks, dashboards, or graphical posts to share what you’ve learned.

Here’s a suggested LinkedIn post:

> Among my first projects as a Data Scientist, today I started monitoring the daily rankings of the most-streamed songs on Spotify. Reviewing these rankings is key to understanding a lot about how money, marketing, and trends move in the music industry.
>
> I’ll be sharing my visualizations and insights in the coming days.
>
> Music can also be studied with data! 🎶📊
>
> **#DataScience #Spotify #WebScraping #MusicTrends**

