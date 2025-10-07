import sqlite3

class DBUtils:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def fetch_data_in_loop(self, table_name):
        results = []
        for i in range(100):
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name} WHERE id = {i}")
            results.extend(cursor.fetchall())
        return results

    def process_without_pool_config(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchall()
