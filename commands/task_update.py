from core.task_model import Task
from core.task_storage import TaskStorage

class TaskManager:
    def __init__(self):
        self.storage = TaskStorage()

    def update(self, task_id, description):
        tasks = self.storage.load()
        found = False
        for t in tasks:
            if t.id == task_id:
                t.description = description
                t.updated_at = Task.now()
                found = True
                break
        if found:
            self.storage.save(tasks)
            print('Task updated successfully')
        else:
            print('Task not found')
