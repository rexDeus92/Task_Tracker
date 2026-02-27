from core.task_storage import TaskStorage

class TaskManager:
    def __init__(self):
        self.storage = TaskStorage()

    def delete(self, task_id):
        tasks = self.storage.load()
        new_tasks = [t for t in tasks if t.id != task_id]
        if len(new_tasks) != len(tasks):
            self.storage.save(new_tasks)
            print('Task deleted successfully')
        else:
            print('Task not found')
