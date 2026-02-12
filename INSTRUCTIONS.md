# Web Scraping

In this project, we will collect, process, and visualize data from a real web page. You are free to choose the website that interests you the most (as long as it is suitable for basic scraping) or use the suggested option.

### Which website can you use?

**Option A:** Website of your choice

You can choose any page that contains visible data in the HTML and is of interest to you.

> 💡 **IMPORTANT:** To ensure the practice can be carried out effectively, keep the following in mind:

- The data must be visible when viewing the source code (right-click → "View page source").

- The site should not require login or use JavaScript to load the content.

- The structure should be simple and repetitive (tables or lists).

**Option B:** Suggested option – Scrapethissite 

If you prefer not to search for a site on your own, you can use this web made specifically for scraping: https://www.scrapethissite.com/

This is an excellent option for practicing table scraping.

## Step 1: Install dependencies

Make sure you have the Python packages `pandas` and `requests` installed to work on the project. If you don't have these libraries installed, run the following in the console:

```bash
pip install pandas requests lxml
```

## Step 2: Download HTML

The HTML of the web page will be downloaded using the `requests` library, as we saw in the module's theory.

## Step 3: Transform the HTML

Using `BeautifulSoup`, analyze the HTML to find the structure containing the data (e.g., `<table>`, `<li>`, `<div>`, etc.).

If you are using Wikipedia and it contains a table, you can directly use `pandas.read_html()` to load it as a DataFrame.

## Step 4: Process the DataFrame

Next, clean the rows to obtain clean values. Also, remove any rows that are empty or lack information.

## Step 5: Store the data in SQLite

Create an empty database instance and include the cleaned data in it, as we saw in the database module. Once you have an empty database:

1. Create the table.
2. Insert the values.
3. Commit the changes.

## Step 6: Visualize the data (optional, but highly recommended)

If you haven’t gone through the visualization concepts and practices yet, don’t worry. Try making this work, and we’ll explore visualization in depth in the next few projects.

What types of visualizations can we make? Suggest at least 3 and plot them.

¡Good luck!
