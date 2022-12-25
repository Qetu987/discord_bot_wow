from init_db import Create_db
from set_default_data import ParsSaver
from pars import get_info_by_classes


if __name__ == "__main__":
    # создаем базу, таблицы и базовые данные
    cr = Create_db()
    cr.create_db()

    # парсим данные с сайта
    pars_data = get_info_by_classes()

    # дополняем данными после парсинга
    ps = ParsSaver(pars_data)
    ans = ps.set_class_data()