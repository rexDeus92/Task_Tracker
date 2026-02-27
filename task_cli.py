
import sys
from commands.task_add import TaskManager as AddManager
from commands.task_update import TaskManager as UpdateManager
from commands.task_delete import TaskManager as DeleteManager
from commands.task_mark_in_progress import TaskManager as InProgressManager
from commands.task_mark_done import TaskManager as DoneManager
from commands.task_list import TaskManager as ListManager

def print_usage():
    print("""Usage:
   add \"description\"
   update <id> \"description\"
   delete <id>
   mark-in-progress <id>
   mark-done <id>
   list [done|todo|in-progress]
""")

if __name__ == "__main__":
    print("Welcome to Task CLI Interactive Terminal!")
    print("Type 'help' for available commands. Type 'exit' to quit.")
    while True:
        try:
            inp = input("task_cli> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting Task CLI.")
            break
        if not inp:
            continue
        args = inp.split()
        command = args[0]
        if command == 'exit':
            print("Exiting Task CLI.")
            break
        elif command == 'help':
            print_usage()
        elif command == 'add' and len(args) >= 2:
            AddManager().add(' '.join(args[1:]))
        elif command == 'update' and len(args) >= 3:
            try:
                tid = int(args[1])
            except ValueError:
                print('Invalid ID')
                continue
            UpdateManager().update(tid, ' '.join(args[2:]))
        elif command == 'delete' and len(args) >= 2:
            try:
                tid = int(args[1])
            except ValueError:
                print('Invalid ID')
                continue
            DeleteManager().delete(tid)
        elif command == 'mark-in-progress' and len(args) >= 2:
            try:
                tid = int(args[1])
            except ValueError:
                print('Invalid ID')
                continue
            InProgressManager().mark_in_progress(tid)
        elif command == 'mark-done' and len(args) >= 2:
            try:
                tid = int(args[1])
            except ValueError:
                print('Invalid ID')
                continue
            DoneManager().mark_done(tid)
        elif command == 'list':
            status = args[1] if len(args) >= 2 else None
            ListManager().list(status)
        else:
            print("Unknown command. Type 'help' for available commands.")
