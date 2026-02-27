from datetime import datetime

class Task:
    def __init__(self, id, description, status, created_at, updated_at):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_dict(cls, d):
        return cls(
            d['id'],
            d['description'],
            d['status'],
            d['createdAt'],
            d['updatedAt']
        )

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }

    @staticmethod
    def now():
        return datetime.now().isoformat(sep=' ', timespec='seconds')
