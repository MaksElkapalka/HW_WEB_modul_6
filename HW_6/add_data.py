import logging
import random
import sqlite3

from connect import database
from faker import Faker

# Підключення до бази даних
conn = sqlite3.connect(database)
cursor = conn.cursor()

# Створення об'єкту Faker
fake = Faker("uk-UA")

# Заповнення таблиці груп
groups = [("Group A",), ("Group B",), ("Group C",)]
cursor.executemany("INSERT INTO groups (name) VALUES (?)", groups)

# Заповнення таблиці викладачів
teachers = [(fake.first_name(), fake.last_name()) for _ in range(5)]
cursor.executemany(
    "INSERT INTO teachers (first_name, last_name) VALUES (?, ?)", teachers
)

# Заповнення таблиці предметів
subjects = [(fake.word(), random.randint(1, 5)) for _ in range(8)]
cursor.executemany("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", subjects)

# Заповнення таблиці студентів
students = [
    (fake.first_name(), fake.last_name(), random.randint(1, 3)) for _ in range(50)
]
cursor.executemany(
    "INSERT INTO students (first_name, last_name, group_id) VALUES (?, ?, ?)", students
)

# Заповнення таблиці оцінок
grades = []
for student_id in range(1, 51):
    for subject_id in range(1, 9):
        for _ in range(20):
            mark = random.randint(1, 100)
            date = fake.date()
            grades.append((student_id, subject_id, mark, date))

cursor.executemany(
    "INSERT INTO grades (student_id, subject_id, mark, date) VALUES (?, ?, ?, ?)",
    grades,
)


try:
    # Збереження змін
    conn.commit()
except sqlite3.Error as e:
    logging.error(e)
    conn.rollback()
finally:
    # Закриття підключення
    cursor.close()
    conn.close()
