"""
    Codígo reponsável pela construção do banco de dados.
"""
import sqlite3
from Globals import DATABASE_NAME

connection = sqlite3.connect(DATABASE_NAME)

with open('schema.sql', encoding="UTF-8") as f:
    connection.executescript(f.read())

connection.close()
