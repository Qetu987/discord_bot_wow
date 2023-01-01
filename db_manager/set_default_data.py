from db_manager.operations_db import ManageDB


class ParsSaver(ManageDB):
    def __init__(self, data):
        self.pars_data = data

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
