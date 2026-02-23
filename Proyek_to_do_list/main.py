from task_add import add_task
from task_delete import delete_task
from task_update import mark_done
from task_display import show_tasks
from task_storage import load_tasks, save_tasks
from datetime import date

def main():
    tasks = load_tasks()

    while True:
        show_tasks(tasks)
        print("\n1.Tambah  2.Selesai  3.Hapus  4.Keluar")
        choice = input("Pilih: ")

        if choice == "1":
            title = input("Judul: ")
            deadline = input("Deadline : ")
            created_at = date.today().strftime("%d-%m-%Y")
            add_task(tasks, title, created_at, deadline)

        elif choice == "2":
            i = int(input("Index: "))
            mark_done(tasks, i)

        elif choice == "3":
            i = int(input("Index: "))
            delete_task(tasks, i)

        elif choice == "4":
            save_tasks(tasks)
            break

main()
