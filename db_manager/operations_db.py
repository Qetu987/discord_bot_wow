from mysql.connector import connect, Error
from db_manager.settings import connect_data as settings

class ManageDB:
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

    # добавляем запись в базу со запросу и данным к нему
    def data_setter(self, querry):
        con = self.connect_data()
        try:
            with connect(
                host=con['host'],
                user=con['user'],
                password=con['password'],
                database=con['database'],
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(querry)
                    connection.commit()
            return ('[+] data set successful')
        except Error as e:
            return (e)


class PlayerManager(ManageDB):
    def __init__(self, user_id):
        self.user_id = user_id
    
    def check_user(self, name, table):
        return self.get_one_data(f'SELECT id FROM {table} WHERE name = "{name}"')

    def user_register(self, name, lvl):
        table = 'pers'
        if not self.check_user(name, table):
            querry = f"INSERT INTO {table} (name, user, lvl) VALUES ('{name}', '{self.user_id}', '{lvl}')"
            ans = self.data_setter(querry)
            pers_id = self.get_one_data(f'SELECT id FROM {table} WHERE user = "{self.user_id}" and name = "{name}"')
            return {'ans': ans, 'id':pers_id[0]}
        else:
            return None

    def user_class_update(self, pers_class, pers_id):
        table = 'pers'
        pers_data = self.get_one_data(f'SELECT * FROM {table} WHERE id = "{pers_id}" and user = "{self.user_id}"')
        if pers_data:
            if self.get_one_data(f'SELECT class_id FROM {table} WHERE id = "{pers_id}"')[0] == None:
                class_id = self.check_user(pers_class, 'class')[0]
                querry = f'UPDATE pers SET class_id = "{class_id}" WHERE id = "{pers_id}";'
                ans = self.data_setter(querry)
                return {'ans': ans}
            else:
                return None
        else:
            return None