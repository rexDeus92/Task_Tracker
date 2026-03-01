# Task CLI

## About the Project
Task CLI is a simple cross-platform command-line application for managing your tasks. It allows you to add, update, delete, and list tasks, as well as mark them as in-progress or done. All tasks are stored in a local JSON file. The project is modular and easy to extend.

## Technologies Used
- Python 3.7+
- Standard Python libraries only (no external dependencies)
- Cross-platform wrappers for Windows (cmd, PowerShell), Linux, and WSL

## How to Use

### 1. Clone the repository and enter the project directory:
```
git clone <repo-url>
cd ./task-tracker
```
### 2. Work in interactive mode:
After launch, you will see:
```
Welcome to Task CLI Interactive Terminal!
Type 'help' for available commands. Type 'exit' to quit.
task_cli>
```
Enter commands directly:
```
add Buy groceries
update 1 Buy groceries and cook dinner
delete 1
mark-in-progress 1
mark-done 1
list
done
todo
in-progress
help
exit
```

### 3. Project Structure
```
task-tracker/
├── core/         # Core logic (models, storage)
├── commands/     # Command modules (add, update, etc.)
├── wrappers/     # Cross-platform launchers
├── task_cli.py   # Main CLI entry point
├── README.md
├── tasks.json    # Your tasks data
```

---

All data is stored in `tasks.json` in the project root. No external dependencies required.

---

## Project Roadmap
For more ideas and features, see:
[Task Tracker Roadmap](https://roadmap.sh/projects/task-tracker)
