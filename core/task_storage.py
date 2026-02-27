import os
import json
from core.task_model import Task

TASKS_FILE = 'tasks.json'

class TaskStorage:
    def __init__(self, filename=TASKS_FILE):
        self.filename = filename

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                return [Task.from_dict(t) for t in data]
            except Exception:
                return []

    def save(self, tasks):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in tasks], f, indent=2, ensure_ascii=False)

    def get_next_id(self, tasks):
        return max([t.id for t in tasks], default=0) + 1
