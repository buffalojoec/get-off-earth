import psycopg2, os



def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get('POSTGRES_HOST'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD'),
        database=os.environ.get('POSTGRES_DB')
    )


def select_from_db(sql_string):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(sql_string)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result