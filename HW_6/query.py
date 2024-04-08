from pprint import pprint as print
from sqlite3 import Error

from connect import create_connection, database


def get_sql_query_number():
    print(
        """1.Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    2.Знайти студента із найвищим середнім балом з певного предмета.
    3.Знайти середній бал у групах з певного предмета.
    4.Знайти середній бал на потоці (по всій таблиці оцінок).
    5.Знайти які курси читає певний викладач.
    6.Знайти список студентів у певній групі.
    7.Знайти оцінки студентів у окремій групі з певного предмета.
    8.Знайти середній бал, який ставить певний викладач зі своїх предметів.
    9.Знайти список курсів, які відвідує студент.
    10.Список курсів, які певному студенту читає певний викладач.
    11.Середній бал, який певний викладач ставить певному студентові.
    12.Оцінки студентів у певній групі з певного предмета на останньому занятті."""
    )
    while True:
        try:
            query_num = int(input("Введіть номер запиту: "))
            if 1 <= query_num <= 12:
                return query_num
            else:
                print("Невірний номер запиту. Введіть число від 1 до 12.")
        except ValueError:
            print("Невірний формат. Введіть число.")


def execute_query(conn, sql_query):
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute(sql_query)
            return cursor.fetchall()
    except Error as e:
        print("Помилка SQL:", e)


if __name__ == "__main__":
    with create_connection(database) as conn:
        if conn is not None:
            query_num = get_sql_query_number()
            sql_file = f"query_{query_num}.sql"
            try:
                with open(sql_file, "r", encoding="utf-8") as sql:
                    print(sql_file)
                    sql_query = sql.read()
                    print(sql_query)
                    results = execute_query(conn, sql_query)
                    if results:
                        print(results)
                    else:
                        print("Немає результатів.")
            except FileNotFoundError:
                print(f"Файл з SQL-запитом '{sql_file}' не знайдено.")
        else:
            print("Помилка! Неможливо підключитись до бази даних.")
