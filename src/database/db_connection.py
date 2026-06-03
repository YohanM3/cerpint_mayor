import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "cerpint_db",
}


def get_connection():
    """Return a new database connection using the configured credentials."""
    return mysql.connector.connect(**DB_CONFIG)
