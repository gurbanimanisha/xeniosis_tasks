import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.tasks = []
        self.load_tasks()

        # Create GUI widgets
        self.task_list = tk.Listbox(self.root, width=40, height=10)
        self.task_list.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)

        self.complete_button = tk.Button(self.root, text="Mark as Complete", command=self.mark_complete)
        self.complete_button.pack(padx=10, pady=10)

        self.save_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(padx=10, pady=10)

        self.load_button = tk.Button(self.root, text="Load Tasks", command=self.load_tasks)
        self.load_button.pack(padx=10, pady=10)

        self.update_task_list()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.update_task_list()

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.tasks.pop(task_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Error", "Select a task to delete")

    def mark_complete(self):
        try:
            task_index = self.task_list.curselection()[0]
            task = self.tasks[task_index]
            self.tasks[task_index] = f"[X] {task}"
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Error", "Select a task to mark as complete")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            pass

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List App")
    app = ToDoListApp(root)
    root.mainloop()