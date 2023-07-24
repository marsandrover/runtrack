import psycopg2

def establish_connection():
    config = {
        'user': 'postgres',
        'password': 'admin',
        'host': '127.0.0.1',
        'database': 'rundb'
    }
    return psycopg2.connect(**config)

def insert_run(distance, duration, date):
    connection = establish_connection()
    cursor = connection.cursor()
    # Implement the SQL query to insert a run record
    # ...
    connection.commit()
    cursor.close()
    connection.close()

def get_all_runs():
    connection = establish_connection()
    cursor = connection.cursor()
    # Implement the SQL query to retrieve all run records
    # ...
    runs = cursor.fetchall()
    cursor.close()
    connection.close()
    return runs

def update_run_date(run_id, new_date):
    connection = establish_connection()
    cursor = connection.cursor()
    # Implement the SQL query to update the date for a run record
    # ...
    connection.commit()
    cursor.close()
    connection.close()
