from mysql.connector import connect, Error
from settings import connect_data

con = connect_data()

try:
    with connect(
        host=con['host'],
        user=con['user'],
        password=con['password'],
    ) as connection:
        show_db_query = f"DROP DATABASE {con['database']}"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
except Error as e:
    print(e)