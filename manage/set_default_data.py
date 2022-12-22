from mysql.connector import connect, Error
from settings import connect_data as settings
from pars import get_info_by_classes


class ParsSaver:
    def __init__(self, data):
        self.pars_data = data

    # настройки бд
    def connect_data(self):
        return settings()

    # возвращает результат запроса всех строк с бд
    def get_all_data(self, querry):
        con = self.connect_data()
        try:
            with connect(
                host=con['host'],
                user=con['user'],
                password=con['password'],
                database=con['database'],
            ) as connection:
                with connection.cursor() as row_cursor:
                    row_cursor.execute(querry)
                    execute_data = row_cursor.fetchall()
                    return execute_data
        except Error as e:
            print(e)

    # возвращает результат запроса первой строки с бд
    def get_one_data(self, querry):
        con = self.connect_data()
        try:
            with connect(
                host=con['host'],
                user=con['user'],
                password=con['password'],
                database=con['database'],
            ) as connection:
                with connection.cursor() as row_cursor:
                    row_cursor.execute(querry)
                    execute_data = row_cursor.fetchone()
                    return execute_data
        except Error as e:
            print(e)






#pars_data = get_info_by_classes()
pars_data = ''
ps = ParsSaver(pars_data)
ans = ps.get_one_data('SELECT * FROM weapon WHERE name = "дробящее"')
print(ans)