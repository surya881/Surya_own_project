class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("Tasks in the to-do list:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

def main():
    todo_list = ToDoList()

    print("To-Do List Manager")
    print("------------------")

    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added to the to-do list.")
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
            print("Task removed from the to-do list.")
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

    print("Thank you for using the To-Do List Manager!")


if __name__ == '__main__':
    main()