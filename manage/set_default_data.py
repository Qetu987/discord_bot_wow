from mysql.connector import connect, Error
from settings import connect_data as settings

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

    # разносим данные к таблице класов
    def set_class_info(self, class_info):
        querry = f"INSERT INTO class (name, descript) VALUES ('{class_info['name'].lower()}', '{class_info['desc']}')"
        result = self.data_setter(querry)
        print(result, 'class')

    def set_class_subtables(self, table_junction, subtable, data, class_id ):
        for i in data:
            subtable_id = self.get_one_data(f'SELECT * FROM {subtable} WHERE name = "{i}"')[0]
            querry = f"INSERT INTO {table_junction} (class_id, {subtable}_id) VALUES ({class_id}, {subtable_id})"
            result = self.data_setter(querry)
            print(result, subtable)

    def set_class_data(self):
        for class_data in self.pars_data:
            self.set_class_info(class_data)
            class_id = self.get_one_data(f'SELECT * FROM class WHERE name = "{class_data["name"].lower()}"')[0]
            self.set_class_subtables('armor_class_junction', 'armor', class_data['Броня'], class_id)
            self.set_class_subtables('type_class_junction', 'type', class_data['Тип'], class_id)
            self.set_class_subtables('weapon_class_junction', 'weapon', class_data['Оружие'], class_id)
        
        print('[+] all tables set successful')
