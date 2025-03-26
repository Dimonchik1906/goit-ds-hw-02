import sqlite3

#Скрипт виконання всіх запитів до БД для отримання відповіді введіть номер запиту від 1 до 14 або введіть exit для завершення
def execute_queries(task_num: int):
    conn = sqlite3.connect("task_management_systems.db")
    cursor = conn.cursor()

    match task_num:
        case '1':   # 1. Отримати всі завдання певного користувача
            user_id = 1  # Приклад ID
            cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
            print("Tasks of user:", cursor.fetchall())

        case '2': # 2. Вибрати завдання за певним статусом
            status_name = 'new'
            cursor.execute("SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = ?)", (status_name,))
            print("Tasks with status 'new':", cursor.fetchall())


        case '3': # 3. Оновити статус конкретного завдання
            title = 'However common stand ask source one deep.'  # Приклад конкретного завдання
            new_status = 'in progress'
            cursor.execute("UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = ?) WHERE title = ?",
                               (new_status, title))

        case '4': # 4. Отримати список користувачів, які не мають жодного завдання
            cursor.execute("SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks)")
            print("Users without tasks:", cursor.fetchall())

        case '5':# 5. Додати нове завдання для конкретного користувача
            new_task = ("New Task", "This is a test task.", 1, 10)
            cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)", new_task)

        case '6':# 6. Отримати всі завдання, які ще не завершено
            cursor.execute("SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed')")
            print("Unfinished tasks:", cursor.fetchall())

        case '7':# 7. Видалити конкретне завдання
            task_id = 21 # Приклад id
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

        case '8':# 8. Знайти користувачів з певною електронною поштою
             email_pattern = "%@example.com"
             cursor.execute("SELECT * FROM users WHERE email LIKE ?", (email_pattern,))
             print("Users with specific email:", cursor.fetchall())

        case '9':# 9. Оновити ім'я користувача
             new_name = 'NewJohn Gry'
             user_id = 9
             cursor.execute("UPDATE users SET fullname = ? WHERE id = ?", (new_name, user_id))

        case '10':# 10. Отримати кількість завдань для кожного статусу
             cursor.execute("SELECT status.name, COUNT(tasks.id) FROM tasks JOIN status ON tasks.status_id = status.id GROUP BY status.name")
             print("Task count per status:", cursor.fetchall())

        case '11':# 11. Отримати завдання для користувачів із певним доменом email
            email_pattern = "%@example.com"
            cursor.execute("SELECT tasks.* FROM tasks JOIN users ON tasks.user_id = users.id WHERE users.email LIKE ?",(email_pattern,))
            print("Tasks for users with domain email:", cursor.fetchall())

        case '12': # 12. Отримати список завдань, що не мають опису
            cursor.execute("SELECT * FROM tasks WHERE description IS NULL OR description = ''")
            print("Tasks without description:", cursor.fetchall())

        case '13': # 13. Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
             cursor.execute(
             "SELECT users.fullname, tasks.title FROM users INNER JOIN tasks ON users.id = tasks.user_id JOIN status ON tasks.status_id = status.id WHERE status.name = 'in progress'")
             print("Users with 'in progress' tasks:", cursor.fetchall())

        case '14':# 14. Отримати користувачів та кількість їхніх завдань
              cursor.execute(
              "SELECT users.fullname, COUNT(tasks.id) FROM users LEFT JOIN tasks ON users.id = tasks.user_id GROUP BY users.id")
              print("Users and their task counts:", cursor.fetchall())
    conn.commit()
    conn.close()
    print("Queries executed successfully.")

def main():
    task_num = 1
    while True:
         task_num = input("Put number of tasks from 1 to 14 or exit: ")
         if task_num == 'exit':
             break
         execute_queries(task_num)

if __name__ == "__main__":
    main()
