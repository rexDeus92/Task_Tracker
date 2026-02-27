from core.task_model import Task
from core.task_storage import TaskStorage

STATUS_IN_PROGRESS = 'in-progress'

class TaskManager:
    def __init__(self):
        self.storage = TaskStorage()

    def mark_in_progress(self, task_id):
        tasks = self.storage.load()
        found = False
        for t in tasks:
            if t.id == task_id:
                t.status = STATUS_IN_PROGRESS
                t.updated_at = Task.now()
                found = True
                break
        if found:
            self.storage.save(tasks)
            print('Task marked as in progress')
        else:
            print('Task not found')
