# Установка 
## Загрузка проекта и виртуального окружения
Для загрузки проекта необходимо скачать его с github 
```commandline
https://github.com/Qetu987/back_test
```
после создать виртуальное окружение
- для unix систем
```commandline
python3 -m venv venv 
source venv/bin/activate
```
- для win
```commandline
python -m venv venv 
venv\Scripts\activate
```

## Установка необходимых билиотек
для корректной работы необходимо установить в виртуальное окружение все необходимые библиотеки 
- для unix систем
```commandline
pip3 install -r requarements.txt
```
- для win
```commandline
pip install -r requarements.txt
```

## создание базы
проверив что нашей базы нет в списке доступных баз 
- для unix систем
```commandline
cd create_base
python3 show_datebases.py
```
- для win
```commandline
cd create_base
python show_datebases.py
```
требуется создать с помощью [create_db.py](./create_base/create_db.py)
- для unix систем
```commandline
cd create_base
python3 create_db.py
```
- для win
```commandline
cd create_base
python create_db.py
```

## Запуск проекта 
Для запуска необходимо выполнить [run.py](./run.py)
- для unix систем
```commandline
python3 run.py
```
- для win
```commandline
python3 run.py
```