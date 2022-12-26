from mysql.connector import connect, Error
from settings import connect_data


class Create_db:
    def __init__(self):
        self.con = connect_data()

    def create_tables(self):
        try:
            with connect(
                host=self.con['host'],
                user=self.con['user'],
                password=self.con['password'],
                database=self.con['database'],
            ) as connection:
                create_class_table_query = """
                        CREATE TABLE class(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(100),
                            descript varchar(1000)
                        )
                        """
                create_type_table_query = """
                        CREATE TABLE type(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(100)
                        )
                        """
                create_type_class_junction_table_query = """
                        CREATE TABLE type_class_junction(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            class_id INT NOT NULL,
                            type_id INT NOT NULL,
                            FOREIGN KEY (class_id) REFERENCES class(id) ON DELETE CASCADE,
                            FOREIGN KEY (type_id) REFERENCES type(id) ON DELETE CASCADE
                        )
                        """
                
                create_armor_table_query = """
                        CREATE TABLE armor(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(100)
                        )
                        """
                create_armor_class_junction_table_query = """
                        CREATE TABLE armor_class_junction(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            class_id INT NOT NULL,
                            armor_id INT NOT NULL,
                            FOREIGN KEY (class_id) REFERENCES class(id) ON DELETE CASCADE,
                            FOREIGN KEY (armor_id) REFERENCES armor(id) ON DELETE CASCADE
                        )
                        """
                
                create_weapon_table_query = """
                        CREATE TABLE weapon(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(100)
                        )
                        """
                create_weapon_class_junction_table_query = """
                        CREATE TABLE weapon_class_junction(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            class_id INT NOT NULL,
                            weapon_id INT NOT NULL,
                            FOREIGN KEY (class_id) REFERENCES class(id) ON DELETE CASCADE,
                            FOREIGN KEY (weapon_id) REFERENCES weapon(id) ON DELETE CASCADE
                        )
                        """
                
                create_talant_table_query = """
                        CREATE TABLE talant(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(100),
                            descript varchar(1000) NOT NULL,
                            class_id INT NOT NULL,
                            FOREIGN KEY (class_id) REFERENCES class(id) ON DELETE CASCADE
                        )
                        """
                create_pers_table_query = """
                        CREATE TABLE pers (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            class_id INT,
                            name VARCHAR(100),
                            lvl INT,
                            date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (class_id) REFERENCES class(id) ON DELETE CASCADE
                        )
                        """
                with connection.cursor() as cursor:
                    cursor.execute(create_class_table_query)
                    cursor.execute(create_type_table_query)
                    cursor.execute(create_type_class_junction_table_query)
                    cursor.execute(create_armor_table_query)
                    cursor.execute(create_armor_class_junction_table_query)
                    cursor.execute(create_weapon_table_query)
                    cursor.execute(create_weapon_class_junction_table_query)
                    cursor.execute(create_talant_table_query)
                    cursor.execute(create_pers_table_query)
            print('[+] tables created is successful')
        except Error as e:
            print(e)

    def create_datebase(self):
        try:
            with connect(
                host=self.con['host'],
                user=self.con['user'],
                password=self.con['password'],
            ) as connection:
                create_db_query = f"CREATE DATABASE {self.con['database']} CHARACTER SET utf8 COLLATE utf8_general_ci;"
                with connection.cursor() as cursor:
                    cursor.execute(create_db_query)
            print('[+] database created is successful')
        except Error as e:
            print(e)

    def set_data(self):
        try:
            with connect(
                host=self.con['host'],
                user=self.con['user'],
                password=self.con['password'],
                database=self.con['database'],
            ) as connection:
                sql_weapon = "INSERT INTO weapon (name) VALUES (%s)"
                val_weapon =[
                    ('кинжалы',),
                    ('кистевое оружие',),
                    ('кистевое',),
                    ('топоры',),
                    ('дробящее оружие',),
                    ('дробящее',),
                    ('мечи',),
                    ('древковое оружие',),
                    ('древковое',),
                    ('посохи',),
                    ('луки',),
                    ('арбалеты',),
                    ('одноручные топоры',),
                    ('одноручное дробящее',),
                    ('одноручные мечи',),
                    ('жезлы',),
                ]

                sql_armor = "INSERT INTO armor (name) VALUES (%s)"
                val_armor =[
                    ('кольчуга',),
                    ('латы',),
                    ('щиты',),
                    ('кожа',),
                    ('ткань',),
                ]

                sql_type = "INSERT INTO type (name) VALUES (%s)"
                val_type =[
                    ('танк',),
                    ('боец',),
                    ('лекарь',),
                ]

                with connection.cursor() as cursor:
                    cursor.executemany(sql_weapon, val_weapon)
                    cursor.executemany(sql_armor, val_armor)
                    cursor.executemany(sql_type, val_type)
                    connection.commit()
            print('[+] data set successful')
        except Error as e:
            print(e)

    def create_db(self):
        self.create_datebase()
        self.create_tables()
        self.set_data()



