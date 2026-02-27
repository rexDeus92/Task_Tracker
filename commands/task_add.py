from core.task_model import Task
from core.task_storage import TaskStorage

STATUS_TODO = 'todo'

class TaskManager:
    def __init__(self):
        self.storage = TaskStorage()

    def add(self, description):
        tasks = self.storage.load()
        task = Task(
            self.storage.get_next_id(tasks),
            description,
            STATUS_TODO,
            Task.now(),
            Task.now()
        )
        tasks.append(task)
        self.storage.save(tasks)
        print(f"Task added successfully (ID: {task.id})")
