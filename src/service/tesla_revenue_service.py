import pandas as pd
import requests
import sys
import matplotlib.pyplot as plt
from utils.utils import Utils
from config.database import Database

class TeslaRevenueService:
    
    """Service to get the Tesla revenue."""

    utils = Utils()
    database = Database()

    def __init__(self):
        pass

    def download_html(self, uri):
        """Download the HTML."""
        target = requests.get(uri, timeout=5, headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
        if target.status_code == 200:
            print("Downloaded successfully")
        else:
            print("Failed to download")
            sys.exit(0)
        return target

    def find_quarterly_table(self, tables):
        """Find the table with the quarterly evolution."""
        for table in tables:
            if 'Net Income (Quarterly)' in str(table):
                return table
        return None
    

    def find_revenue_table(self, tables):
        """ Find the table with revenue evolution. """
        for table in tables:
            print(table)
        return None
    
    def plot_bar_chart(self, df):

        """Plot a bar chart."""
        
        df['Concept'] = df['Concept'].apply(lambda x: x.replace('(Quarterly)', ''))
        df['Figure'] = pd.to_numeric(df['Figure'], errors='coerce')
        df.plot(kind='bar', x='Concept', y='Figure', color='skyblue', width=0.8)
        plt.xticks(rotation=45)
        plt.ylabel('Millions of USD')
        plt.title('Tesla Quarterly Net Income')
        plt.show()


    def plot_pie_chart(self, df):

        """Plot a pie chart."""
        
        df['Concept'] = df['Concept'].apply(lambda x: x.replace('(Quarterly)', '').strip())
        df['Figure'] = pd.to_numeric(df['Figure'], errors='coerce')
        df = df.dropna(subset=['Figure'])
        plt.pie(df['Figure'], labels=df['Concept'])
        plt.title('Tesla Metrics - Pie Chart')
        plt.axis('equal')
        plt.show()


    def plot_line_chart(self, df):
        
        """Plot a line chart."""

        df['Concept'] = df['Concept'].apply(lambda x: x.replace('(Quarterly)', '').strip())
        df['Figure'] = pd.to_numeric(df['Figure'], errors='coerce')
        plt.plot(df['Concept'], df['Figure'], marker='o', linestyle='-', color='green')
        plt.xticks(rotation=45)
        plt.ylabel('Millions of USD')
        plt.title('Tesla Metrics - Line Chart')
        plt.grid(True)
        plt.show()



    def tesla_plot_bar_chart(self, df):

        """Plot a bar chart."""
        
        df.plot(kind='bar', x='Date', y='Revenue', color='skyblue', width=0.8)
        plt.xticks(rotation=45)
        plt.ylabel('Millions of USD')
        plt.title('Tesla Quarterly Net Income')
        plt.show()


    def tesla_plot_pie_chart(self, df):

        """Plot a pie chart."""

        df = df.dropna(subset=['Revenue'])
        plt.pie(df['Date'], labels=df['Revenue'])
        plt.title('Tesla Metrics - Pie Chart')
        plt.axis('equal')
        plt.show()


    def tesla_plot_line_chart(self, df):
        
        """Plot a line chart."""

        plt.plot(df['Date'], df['Revenue'], marker='o', linestyle='-', color='green')
        plt.xticks(rotation=45)
        plt.ylabel('Millions of USD')
        plt.title('Tesla Metrics - Line Chart')
        plt.grid(True)
        plt.show()




    def display_visualizations(self, df):

        """Display the visualizations."""
        self.plot_bar_chart(df)
        self.plot_pie_chart(df)
        self.plot_line_chart(df)


    def display_tesla_revenue(self, df):

        """Display the tesla revenue ."""
        self.tesla_plot_bar_chart(df)
        self.tesla_plot_pie_chart(df)
        self.tesla_plot_line_chart(df)

    
    def get_tesla_revenue(self):
        """Get the Tesla revenue."""

        revenue_table = self.utils.find_table(self.download_html("https://companies-market-cap-copy.vercel.app/index.html"))

        if revenue_table is None:
            print("No revenue table found")
            sys.exit(0)
        
        df_revenue = self.utils.convert_revenue_data_table(revenue_table)

        try:
            df_revenue.to_sql('tesla', self.database.connect(), if_exists='replace', index=False)
            print("Data saved successfully")
        except Exception as e:
            print(e)
            sys.exit(0)

        self.display_tesla_revenue(df_revenue)


    def get_tesla_quarterly(self):

        """Get the Testla Quarterly. """

        quarterly_table = self.find_quarterly_table(self.utils.find_all_tables(self.download_html("https://ycharts.com/companies/TSLA/revenues")))

        if quarterly_table is None:
            print("No quarterly table found")
            sys.exit(0)

        df = self.utils.convert_table_to_dataframe(quarterly_table)

        try:
            df.to_sql('tesla', self.database.connect(), if_exists='replace', index=False)
            print("Data saved successfully")
        except Exception as e:
            print(e)
            sys.exit(0)
        self.display_visualizations(df)

    def get_data_tesla(self):
        self.get_tesla_revenue()
        self.get_tesla_quarterly()
       
        