# CLI Todo App

A small command line todo app written in Python. It's my first project on GitHub, so it's simple on purpose. Your todos are saved in a local `todos.json` file, so they are still there the next time you open the app.

## Features

- Add new todos
- List all todos
- Mark todos as done
- Delete todos
- Clear all completed todos

## Requirements

- Python 3.6 or newer
- No extra packages needed

## Installation

```bash
git clone https://github.com/yasin-amiri-dev/CLI-Todo-App.git
cd CLI-Todo-App
```

## Usage

Add a todo:

```bash
python app.py add "Learn Git"
```

Show all todos:

```bash
python app.py list
```

Example output:

```
1. [ ] Learn Git
2. [x] Write my first README
```

Mark a todo as done (use the id from the list):

```bash
python app.py done 1
```

Delete a todo:

```bash
python app.py delete 2
```

Remove all completed todos:

```bash
python app.py clear
```

Show help:

```bash
python app.py --help
```

## How it works

Todos are stored as a list of dictionaries in `todos.json`. Each todo has an `id`, a `title` and a `done` value. The app uses Python's built-in `argparse` module for the commands and `json` for saving the data.

## Ideas for the future

- Due dates
- Priorities
- Edit an existing todo
- Colors in the terminal

## Author

Made by [yasin-amiri-dev](https://github.com/yasin-amiri-dev)
