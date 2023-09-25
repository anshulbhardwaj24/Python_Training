import threading
import multiprocessing

# Define an abstract Task interface
class TaskInterface:
    def execute(self):
        pass

# Implement two concrete tasks
class Task1(TaskInterface):
    def execute(self):
        print("Executing Task 1")

class Task2(TaskInterface):
    def execute(self):
        print("Executing Task 2")

# Create a class to manage tasks
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if isinstance(task, TaskInterface):
            self.tasks.append(task)
        else:
            raise ValueError("Invalid task type")

    def execute_all_tasks(self):
        for task in self.tasks:
            task.execute()

# Create an exception class for task execution errors
class TaskExecutionError(Exception):
    def __init__(self, message):
        super().__init__(message)

# Define a worker function for multi-threading
def worker( task, manager):
    try:
        task.execute()
    except Exception as e:
        raise TaskExecutionError(str(e))

if __name__ == "__main__":
    task_manager = TaskManager()

    task1 = Task1()
    task2 = Task2()

    task_manager.add_task(task1)
    task_manager.add_task(task2)

    # Use multi-threading to execute tasks concurrently
    thread1 = threading.Thread(target=worker, args=(task1, task_manager))
    thread2 = threading.Thread(target=worker, args=(task2, task_manager))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Tasks executed using multi-threading")

    # Use multiprocessing to execute tasks in separate processes
    process1 = multiprocessing.Process(target=worker, args=(task1, task_manager))
    process2 = multiprocessing.Process(target=worker, args=(task2, task_manager))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Tasks executed using multiprocessing")

    task_manager.execute_all_tasks()
