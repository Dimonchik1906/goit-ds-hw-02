import sqlite3
from faker import Faker
import random

#Скрипт заповнює нашу базу даних випадковими даними за допомоги бібліотеки Faker
def seed_database():
    conn = sqlite3.connect("task_management_systems.db")
    cursor = conn.cursor()
    faker = Faker()

    # Заповнюємо таблицю status
    statuses = [('new',), ('in progress',), ('completed',)]
    cursor.executemany("INSERT INTO status (name) VALUES (?) ON CONFLICT(name) DO NOTHING", statuses)

    # Заповнюємо таблицю users
    users = [(faker.name(), faker.email()) for _ in range(10)]
    cursor.executemany("INSERT INTO users (fullname, email) VALUES (?, ?) ON CONFLICT(email) DO NOTHING", users)

    # Отримуємо id користувачів і статусів
    cursor.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT id FROM status")
    status_ids = [row[0] for row in cursor.fetchall()]

    # Заповнюємо таблицю tasks
    tasks = [(faker.sentence(), faker.text(), random.choice(status_ids), random.choice(user_ids)) for _ in range(20)]
    cursor.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)", tasks)

    conn.commit()
    conn.close()
    print("Database seeded successfully.")


if __name__ == "__main__":
    seed_database()