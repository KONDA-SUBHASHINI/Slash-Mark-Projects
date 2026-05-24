# Project 1 - Simple Task Management App

A command-line based Task Management application built using Python. It allows users to manage their daily tasks efficiently with features like adding, removing, listing, and getting smart task recommendations based on priority.

---

## 📌 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [How to Run](#how-to-run)
- [Usage Guide](#usage-guide)
- [How the Recommendation Works](#how-the-recommendation-works)
- [Sample Output](#sample-output)

---

## 📖 About the Project

The Simple Task Management App is a Python-based command-line application that helps users keep track of their tasks. Each task has a **description** and a **priority level** (Low, Medium, or High). Tasks are saved persistently in a CSV file so they are not lost when the app is closed.

The app also includes a smart **task recommendation system** that suggests the most important task to work on based on priority — always recommending High priority tasks first, then Medium, then Low.

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| ➕ Add Task | Add a new task with a description and priority (Low / Medium / High) |
| ❌ Remove Task | Remove a task by its description (case-insensitive) |
| 📋 List Tasks | View all current tasks with their priorities |
| 💡 Recommend Task | Get a smart recommendation based on task priority |
| 💾 Persistent Storage | All tasks are saved to `tasks.csv` and reloaded on next run |

---

## 🛠 Tech Stack

- **Language:** Python 3.x
- **Libraries:**
  - `pandas` — for task storage and data manipulation
  - `scikit-learn` — for the ML-based priority classifier (Naive Bayes)

---

## 📁 Project Structure

```
project1/
├── main.py            # Main application logic
├── requirements.txt   # Python dependencies
├── tasks.csv          # Persistent task storage (preloaded with sample tasks)
├── instructions.txt   # Setup instructions
└── README.md          # Project documentation
```

---

## ✅ Prerequisites

- Python 3.x installed on your system
- pip (Python package manager)

---

## ⚙️ Installation & Setup

**Step 1: Navigate to the project folder**
```bash
cd project1
```

**Step 2: (Optional) Create a virtual environment**
```bash
python -m venv task_app
source task_app/bin/activate        # macOS/Linux
task_app\Scripts\activate           # Windows
```

**Step 3: Install required packages**
```bash
pip install pandas scikit-learn
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 📘 Usage Guide

Once the app starts, you will see this menu:

```
Task Management App
1. Add Task
2. Remove Task
3. List Tasks
4. Recommend Task
5. Exit
```

### 1. Add Task
- Enter a task description and a priority level: `Low`, `Medium`, or `High`
- Invalid priority entries are rejected with an error message

### 2. Remove Task
- Enter the task description to remove
- The search is **case-insensitive** (e.g., "CODING", "coding", "Coding" all work)
- Displays "Task not found!" if the description doesn't match

### 3. List Tasks
- Displays all tasks in a formatted table with index, description, and priority

### 4. Recommend Task
- Recommends the most important task based on priority
- See recommendation logic below

### 5. Exit
- Exits the application

---

## 💡 How the Recommendation Works

The recommendation follows a **priority waterfall**:

```
Has High priority tasks?
    ✅ Yes → Recommend a random High priority task
    ❌ No  ↓
Has Medium priority tasks?
    ✅ Yes → Recommend a random Medium priority task
    ❌ No  ↓
Has Low priority tasks?
    ✅ Yes → Recommend a random Low priority task
    ❌ No  → "No tasks available for recommendations."
```

This ensures the most urgent task is always recommended first.

---

## 🖥 Sample Output

```
Task Management App
1. Add Task
2. Remove Task
3. List Tasks
4. Recommend Task
5. Exit
Select an option: 1
Enter task description: Complete assignment
Enter task priority (Low/Medium/High): High
Task added successfully.

Select an option: 3
   description              priority
0  Complete assignment      High
1  Buy groceries            Medium
2  Evening walk             Low

Select an option: 4
Recommended task: Complete assignment - Priority: High

Select an option: 2
Enter task description to remove: complete assignment
Task removed successfully.

Select an option: 4
Recommended task: Buy groceries - Priority: Medium

Select an option: 5
Goodbye!
```

---

## 📝 Notes

- `tasks.csv` comes with sample tasks preloaded. New tasks are appended automatically.
- Do not delete `tasks.csv` unless you want to reset all tasks.
- The ML classifier trains automatically as more tasks are added with varied priorities.
- Tasks are stored with two columns: `description` and `priority`.