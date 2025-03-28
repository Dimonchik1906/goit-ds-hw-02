import sqlite3

# скрипт створює базу даних
def create_db():
    # читаємо файл зі скриптом для створення БД
    with open('tasks.sql', 'r') as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect('task_management_systems.db') as con:
        cur = con.cursor()
    # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)

if __name__ == "__main__":
    create_db()