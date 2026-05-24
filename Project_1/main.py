import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import random

# Initialize an empty task list
tasks = pd.DataFrame(columns=['description', 'priority'])

# Load pre-existing tasks from a CSV file (if any)
try:
    tasks = pd.read_csv('tasks.csv')
except FileNotFoundError:
    pass

# Function to save tasks to a CSV file
def save_tasks():
    tasks.to_csv('tasks.csv', index=False)

# Train the task priority classifier (only if enough data exists)
model = None

def train_model():
    global model
    if len(tasks) >= 2 and tasks['priority'].nunique() >= 2:
        vectorizer = CountVectorizer()
        clf = MultinomialNB()
        model = make_pipeline(vectorizer, clf)
        model.fit(tasks['description'], tasks['priority'])

train_model()

# Function to add a task to the list
def add_task(description, priority):
    global tasks
    new_task = pd.DataFrame({'description': [description], 'priority': [priority]})
    tasks = pd.concat([tasks, new_task], ignore_index=True)
    save_tasks()
    train_model()

# Function to remove a task by description
def remove_task(description):
    global tasks
    match = tasks['description'].str.lower() == description.lower()
    if match.any():
        tasks = tasks[~match]
        save_tasks()
        train_model()
        print("Task removed successfully.")
    else:
        print("Task not found!")

# Function to list all tasks
def list_tasks():
    if tasks.empty:
        print("No tasks available.")
    else:
        print("\n" + tasks.to_string(index=True))

# Function to recommend a task (High → Medium → Low waterfall)
def recommend_task():
    if tasks.empty:
        print("No tasks available for recommendations.")
        return

    for priority_level in ["High", "Medium", "Low"]:
        filtered = tasks[tasks['priority'] == priority_level]
        if not filtered.empty:
            random_task = random.choice(filtered['description'].tolist())
            print(f"Recommended task: {random_task} - Priority: {priority_level}")
            return

    print("No tasks available for recommendations.")

# Main menu
while True:
    print("\nTask Management App")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Recommend Task")
    print("5. Exit")

    choice = input("Select an option: ").strip()

    if choice == "1":
        description = input("Enter task description: ").strip()
        priority = input("Enter task priority (Low/Medium/High): ").strip().capitalize()
        if priority not in ["Low", "Medium", "High"]:
            print("Invalid priority! Please enter Low, Medium, or High.")
        else:
            add_task(description, priority)
            print("Task added successfully.")

    elif choice == "2":
        description = input("Enter task description to remove: ").strip()
        remove_task(description)

    elif choice == "3":
        list_tasks()

    elif choice == "4":
        recommend_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please select a valid option.")