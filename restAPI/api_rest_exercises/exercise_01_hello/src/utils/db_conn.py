import psycopg


def db_connection() -> psycopg.extensions.connection:
    conn = psycopg.connect(
        "dbname=postgres host=localhost password=1234 user=postgres")

    return conn
