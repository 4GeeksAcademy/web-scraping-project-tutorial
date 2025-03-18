import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# URL of the webpage
url = "https://companies-market-cap-copy.vercel.app/index.html"

# Fetch the HTML content
response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Error accessing the page: {response.status_code}")
html_content = response.text

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract data from table
years = []
revenues = []
changes = []

for row in soup.select("table tr")[1:]:  # Skipping header row
    cols = row.find_all("td")
    if len(cols) > 1:
        years.append(cols[0].text.strip())
        revenues.append(cols[1].text.strip())
        changes.append(cols[2].text.strip() if len(cols) > 2 else "N/A")

# Create a DataFrame
data = pd.DataFrame({
    "Year": years,
    "Revenue": revenues,
    "Change": changes
})

# Save to CSV and Excel
csv_filename = "company_revenue_data.csv"
excel_filename = "company_revenue_data.xlsx"

data.to_csv(csv_filename, index=False)
data.to_excel(excel_filename, index=False)

print(f"Data saved to {csv_filename} and {excel_filename}")
