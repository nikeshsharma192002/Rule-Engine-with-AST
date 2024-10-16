# database.py

import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
        return conn

    def create_table(self):
        try:
            sql_create_rules_table = """
            CREATE TABLE IF NOT EXISTS rules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rule_string TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_create_rules_table)
        except Error as e:
            print(e)

    def insert_rule(self, rule_string):
        sql = '''INSERT INTO rules(rule_string) VALUES(?)'''
        cursor = self.connection.cursor()
        cursor.execute(sql, (rule_string,))
        self.connection.commit()
        return cursor.lastrowid
