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


def insert_one(table_name, record):
    if table_name == "planets":
        columns = "(name, distance)"
        values = "(%s, %s)"
    elif table_name == "ship_types":
        columns = "(model_name, hypserspeed_rating, max_capacity)"
        values = "(%s, %s, %s)"
    elif table_name == "ships":
        columns = "(planet_id, ship_type_id, name, trip_time, trip_danger)"
        values = "(%s, %s, %s, %s, %s)"
    elif table_name == "tickets":
        columns = "(ship_id, name, pod_quantity)"
        values = "(%s, %s, %s)"
    sql_string = f"INSERT INTO {table_name} {columns} VALUES {values}"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(sql_string, record)
    conn.commit()
    cursor.close()
    conn.close()