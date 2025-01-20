import sqlite3

class Database:

    """Database class."""

    def __init__(self):
        self.host = 'localhost'
        self.port = 5432

    def connect(self):
        
        """Connect to the database."""

        return sqlite3.connect('tesla.db')
    
    def close(self, connection):
        
        """Close the connection."""

        connection.close()

    def create_table(self):
        
        """Create the table."""

        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tesla (
                id INTEGER PRIMARY KEY,
                concept TEXT  NOT NULL,
                figure TEXT NOT NULL
            )
        ''')
        connection.commit()
        self.close(connection)