# Todo_list

## Project description
 ***Todo_list*** - a project to create a website with a to-do list

## Task Overview

The project consists of two main models: `Task` and `Tag`.

### **Task Model**
A **task** represents an individual item in the todo list and includes:
- `content` – description of the task.
- `created_task` – timestamp of task creation.
- `deadline` – optional deadline for task completion.
- `is_done` – boolean field marking task completion status.
- `tags` – relevant tags assigned to the task.

### **Tag Model**
A **tag** symbolizes the theme of a task and consists only of a `name`.  
A task can have multiple tags, and a tag can be associated with multiple tasks.
 ____________
## Features

- Add, update, and delete tasks.

- Mark tasks as complete or undo them.

- Organize tasks using tags.

- Sort tasks from not done to done and from newest to oldest.

- Sidebar navigation for easy access to tasks and tags.
____________

## 📦 Installation

### 1️⃣ **Clone the repository**. 
https://github.com/andreykolomiec/Todo_list.git

### 2️⃣ Create a virtual environment and activate it
python -m venv venv
- Windows:
  - venv\Scripts\activate

- Mac/Linux:
  - source venv/bin/activate

### 3️⃣ Setting up dependencies
pip install -r requirements.txt

### 4️⃣ Setting up the database and applying migrations
python manage.py migrate

### 5️⃣ Create a superuser (for access to the admin panel)
python manage.py createsuperuser

### 6️⃣ Starting the server
python manage.py runserver

### The application will be available at: http://127.0.0.1:8000/
### To access the page after registration: http://127.0.0.1:8000/task_list/
____________
🔧 Technology:
- Python (Django) – backend framework
- Django ORM – database management
- SQLite (default) – database (can be switched to PostgreSQL/MySQL)
- HTML, CSS, Bootstrap – frontend styling
- Git & GitHub – version control and collaboration
___________
### 👥 Authors:
- 📂 andreykolomiec (https://github.com/andreykolomiec/Todo_list/)