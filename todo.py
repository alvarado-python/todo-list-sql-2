# todo-list-sql-2
To-do list application using Python and SQLite
import sqlite3

# conectar base de datos
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT
)
""")

conn.commit()

def add_task(task):
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()

def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    
    if tasks:
        for task in tasks:
            print(task[0], "-", task[1])
    else:
        print("No tasks found")

def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()

while True:
    print("\n1 Add Task")
    print("2 View Tasks")
    print("3 Delete Task")
    print("4 Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        task_id = input("Enter task ID: ")
        delete_task(task_id)

    elif choice == "4":
        break

    else:
        print("Invalid option")
