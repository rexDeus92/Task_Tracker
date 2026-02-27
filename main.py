import sys
import os
import json
from datetime import datetime

TASKS_FILE = 'tasks.json'

STATUS_TODO = 'todo'
STATUS_IN_PROGRESS = 'in-progress'
STATUS_DONE = 'done'


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except Exception:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def get_next_id(tasks):
    return max([t['id'] for t in tasks], default=0) + 1

def now():
    return datetime.now().isoformat(sep=' ', timespec='seconds')

def print_usage():
    print("""Usage:
   add "description"
   update <id> "description"
   delete <id>
   mark-in-progress <id>
   mark-done <id>
   list [done|todo|in-progress]
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1]
    tasks = load_tasks()

    if command == 'add' and len(sys.argv) >= 3:
        desc = sys.argv[2]
        task = {
            'id': get_next_id(tasks),
            'description': desc,
            'status': STATUS_TODO,
            'createdAt': now(),
            'updatedAt': now()
        }
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task added successfully (ID: {task['id']})")

    elif command == 'update' and len(sys.argv) >= 4:
        try:
            tid = int(sys.argv[2])
        except ValueError:
            print('Invalid ID')
            sys.exit(1)
        desc = sys.argv[3]
        found = False
        for t in tasks:
            if t['id'] == tid:
                t['description'] = desc
                t['updatedAt'] = now()
                found = True
                break
        if found:
            save_tasks(tasks)
            print('Task updated successfully')
        else:
            print('Task not found')

    elif command == 'delete' and len(sys.argv) >= 3:
        try:
            tid = int(sys.argv[2])
        except ValueError:
            print('Invalid ID')
            sys.exit(1)
        new_tasks = [t for t in tasks if t['id'] != tid]
        if len(new_tasks) != len(tasks):
            save_tasks(new_tasks)
            print('Task deleted successfully')
        else:
            print('Task not found')

    elif command == 'mark-in-progress' and len(sys.argv) >= 3:
        try:
            tid = int(sys.argv[2])
        except ValueError:
            print('Invalid ID')
            sys.exit(1)
        found = False
        for t in tasks:
            if t['id'] == tid:
                t['status'] = STATUS_IN_PROGRESS
                t['updatedAt'] = now()
                found = True
                break
        if found:
            save_tasks(tasks)
            print('Task marked as in progress')
        else:
            print('Task not found')

    elif command == 'mark-done' and len(sys.argv) >= 3:
        try:
            tid = int(sys.argv[2])
        except ValueError:
            print('Invalid ID')
            sys.exit(1)
        found = False
        for t in tasks:
            if t['id'] == tid:
                t['status'] = STATUS_DONE
                t['updatedAt'] = now()
                found = True
                break
        if found:
            save_tasks(tasks)
            print('Task marked as done')
        else:
            print('Task not found')

    elif command == 'list':
        filter_status = sys.argv[2] if len(sys.argv) >= 3 else None
        filtered = tasks
        if filter_status in [STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE]:
            filtered = [t for t in tasks if t['status'] == filter_status]
        if not filtered:
            print('No tasks found.')
        else:
            for t in filtered:
                print(f"ID: {t['id']} | {t['status']} | {t['description']} | Created: {t['createdAt']} | Updated: {t['updatedAt']}")
    else:
        print_usage()
        sys.exit(1)
