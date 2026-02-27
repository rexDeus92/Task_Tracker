from core.task_storage import TaskStorage
from core.task_model import Task

STATUS_TODO = 'todo'
STATUS_IN_PROGRESS = 'in-progress'
STATUS_DONE = 'done'

class TaskManager:
    def __init__(self):
        self.storage = TaskStorage()

    def list(self, status=None):
        tasks = self.storage.load()
        filtered = tasks
        if status in [STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE]:
            filtered = [t for t in tasks if t.status == status]
        if not filtered:
            print('No tasks found.')
        else:
            for t in filtered:
                print(f"ID: {t.id} | {t.status} | {t.description} | Created: {t.created_at} | Updated: {t.updated_at}")
