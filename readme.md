# Warcraft bot for discord
## installing
:shipit: [read](./install.md) for installing project

## About project
In this project I`m using mysql database. Originally you can add your connecting data to [this file](./db_manager/settings.py) and create secret file (./db_manager/secret.py) with bot-token.
<br>

### Creating db
For ease of deployment of the system, a script was written to create a database and fill it with data
<br>
In the folder ***db_manager*** there are database settings and files for automating the processes of creating and deleting a database
- [manage.py](./manage.py) manager for create ans delete db for this project

- [settings.py](./db_manager/settings.py) stores the base settings of the database
- [show_datebases.py](./db_manager/show_db.py) 
displays all existing databases according to [settings](./db_manager/settings.py)
- [drop_db.py](./db_manager/drop_db.py) 
deletes the database according to the [settings](./db_manager/settings.py)
- [create_db.py](./db_manager/create_db.py) creates base according to [settinga](./db_manager/settings.py) and fills it with data

### Main project files
After creating datebase and pasring main information from official sites, you can start your bot by [main.py](./main.py).

### DateBase structure
The database consists of 9 tables:
- [pers](#pers-table)
- [talant](#talant-table)
- [weapon_class_junction](#weapon_class_junction-table)
- [weapon](#weapon-table)
- [armor_class_junction](#armor_class_junction-table)
- [armor](#armor-table)
- [type_class_junction](#type_class_junction-table)
- [type](#type-table)
- [class](#class-table)

## Pers table
***pers*** consist of 7 fields:
- id (increment)
- class_id (int field) one_to_many relation 
- name (text field)
- user (text field)
- thrace (text field)
- lvl (int field)
- date (TIMESTAMP field)     

## Talant table
***talant*** consist of 4 fields:
- id (increment)
- class_id (int field) one_to_many relation 
- name (text field)
- descript (text field)

## Weapon_class_junction table
***weapon_class_junction*** consist of 3 fields:
- id (increment)
- class_id (int field) one_to_many relation 
- weapon_id (int field) one_to_many relation 

## Weapon table
***weapon*** consist of 2 fields:
- id (increment)
- name (text field)

## Armor_class_junction table
***armor_class_junction*** consist of 3 fields:
- id (increment)
- class_id (int field) one_to_many relation 
- armor_id (int field) one_to_many relation 

## Armor table
***armor*** consist of 2 fields:
- id (increment)
- name (text field)

## Type_class_junction table
***type_class_junction*** consist of 3 fields:
- id (increment)
- class_id (int field) one_to_many relation 
- type_id (int field) one_to_many relation 

## Type table
***type*** consist of 2 fields:
- id (increment)
- name (text field)

## Class table
***class*** consist of 3 fields:
- id (increment)
- name (text field)
- descript (text field)