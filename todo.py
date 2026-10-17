import argparse
import json
import os

FILE_NAME = "todos.json"


def load_todos():
    # if the file doesn't exist yet, start with an empty list
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_todos(todos):
    with open(FILE_NAME, "w") as f:
        json.dump(todos, f, indent=2)


def add_todo(title):
    todos = load_todos()
    # give each todo an id that is always bigger than the last one
    new_id = todos[-1]["id"] + 1 if todos else 1
    todos.append({"id": new_id, "title": title, "done": False})
    save_todos(todos)
    print(f"Added: {title} (id {new_id})")


def list_todos():
    todos = load_todos()
    if not todos:
        print("No todos yet. Add one with: python app.py add \"your task\"")
        return
    for todo in todos:
        mark = "[x]" if todo["done"] else "[ ]"
        print(f"{todo['id']}. {mark} {todo['title']}")


def complete_todo(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = True
            save_todos(todos)
            print(f"Marked as done: {todo['title']}")
            return
    print(f"No todo with id {todo_id}")


def delete_todo(todo_id):
    todos = load_todos()
    new_todos = [t for t in todos if t["id"] != todo_id]
    if len(new_todos) == len(todos):
        print(f"No todo with id {todo_id}")
        return
    save_todos(new_todos)
    print(f"Deleted todo {todo_id}")


def clear_done():
    todos = load_todos()
    remaining = [t for t in todos if not t["done"]]
    removed = len(todos) - len(remaining)
    save_todos(remaining)
    print(f"Removed {removed} completed todo(s)")


def main():
    parser = argparse.ArgumentParser(description="A simple command line todo app")
    sub = parser.add_subparsers(dest="command")

    add_p = sub.add_parser("add", help="add a new todo")
    add_p.add_argument("title", help="what you need to do")

    sub.add_parser("list", help="show all todos")

    done_p = sub.add_parser("done", help="mark a todo as done")
    done_p.add_argument("id", type=int, help="id of the todo")

    del_p = sub.add_parser("delete", help="delete a todo")
    del_p.add_argument("id", type=int, help="id of the todo")

    sub.add_parser("clear", help="remove all completed todos")

    args = parser.parse_args()

    if args.command == "add":
        add_todo(args.title)
    elif args.command == "list":
        list_todos()
    elif args.command == "done":
        complete_todo(args.id)
    elif args.command == "delete":
        delete_todo(args.id)
    elif args.command == "clear":
        clear_done()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
