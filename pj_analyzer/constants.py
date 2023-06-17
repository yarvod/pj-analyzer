class MessageBlocks:
    OTHER = 0  # мусор, то, что не распознать
    CONTACTS = 1  # контакт
    VACANCY_NAME = 2  # название вакансии
    COMPANY_NAME = 3  # название компании
    VACANCY_DESCRIPTION = 4  # описание вакансии
    COMPANY_DESCRIPTION = 5  # описание компании
    FORMAT = 6  # формат работы
    POSITION = 7  # позиция
    LEVEL = 8  # уровень позиции
    DUTIES = 9  # обязанности
    ADDRESS_OFFICE = 10  # адрес офиса
    REQUIREMENTS = 11  # требования
    SALARY = 12  # зарплата
    EMPLOYMENT = 13  # занятость
    SITE = 14  # сайт компании
    ADDITIONAL_INFO = 15  # доп информация
    STACK_TECH = 16  # стэк технологий
    WORK_CONDITIONS = 17  # условия работы
    LINK = 18  # какие-то ссылки
    HOW_APPLY = 19  # как откликаться
    POSITION_AND_SALARY = 20  # позиция и зарплата

    MAP = dict(
        (
            (OTHER, "Мусор"),
            (CONTACTS, "Контакт"),
            (VACANCY_NAME, "Название вакансии"),
            (COMPANY_NAME, "Название компании"),
            (VACANCY_DESCRIPTION, "Описание вакансии"),
            (COMPANY_DESCRIPTION, "Описание компании"),
            (FORMAT, "Формат работы"),
            (POSITION, "Позиция"),
            (LEVEL, "Уровень позции"),
            (DUTIES, "Обязанности"),
            (ADDRESS_OFFICE, "Адрес офиса"),
            (REQUIREMENTS, "Требования"),
            (SALARY, "Зарплата"),
            (EMPLOYMENT, "Занятость"),
            (SITE, "Сайт компании"),
            (ADDITIONAL_INFO, "Доп. Информация"),
            (STACK_TECH, "Стэк разработки"),
            (WORK_CONDITIONS, "Условия работы"),
            (LINK, "Ссылки"),
            (HOW_APPLY, "Как откликнуться"),
            (POSITION_AND_SALARY, "Позиция и зарплата"),
        )
    )
