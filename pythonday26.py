#🐍 Day 26: Taskmaster: Build Your To-Do List App 🐍
'''
Setting Up
To get started, think of the features you want in your app. A basic To-Do List App usually allows you to:
Add tasks,Delete tasks,View all tasks
Mark tasks as complete
'''
'''
Defining the App
todo_list = {
    "Buy groceries": False,
    "Go to gym": True,
    "Learn Python": False
}

# Function to add a task
def add_task(task):
    todo_list[task] = False

# Function to mark a task as complete
def complete_task(task):
    if task in todo_list:
        todo_list[task] = True

# Function to display all tasks
def display_tasks():
    for task, is_complete in todo_list.items():
        status = "Done" if is_complete else "Incomplete"
        print(f"{task} - {status}")
    
# Call the display_tasks function
display_tasks()
'''
'''
Homework: Build and Enhance Your App
Build the Basics: Using the structure above, build out your To-Do List App.
Enhancements: Add functionalities to delete tasks and to view only completed or only incomplete tasks.
Advanced: Use a nested structure to categorize tasks (e.g., Personal, Work).
Thinking Ahead: If you feel confident, 
think about how using classes (remember Day 17?) 
could help make your app more organized and scalable.
'''

#defining the app
to_do_list = {
   "Personal":{
    "Buy groceries": False,
    "Go to gym": True,
    "Learn Python": True,
    "Apply for atleast 1 job a day": True,
    "Write a blog post": False,
    "Read a chapter a day": False
  },
  "Work":{
    "Apply for a job": False,
    "Apply for a promotion": False,
    "Submit a report before deadline": False,
  }
}
#function to add task
def add_task(category,task):
    to_do_list[category][task] = False#
#function to mark task as complete
def complete_task(category,task):
    if task in to_do_list.items():
        to_do_list[category][task] = True
#function to display only completed task
'''def display_completed():
   for category,task, is_complete in to_do_list.items():
      if is_complete:
        status ="Done"
        print(f"{category}{task} - {status}")
      else:
        status = "Incomplete"
        print(f"{category}{task} - {status}")
#Advanced: Use a nested structure to categorize tasks (e.g., Personal, Work). 
'''
# Function to mark a task as complete
def display_task(category, task):
    if category in to_do_list and task in todo_list[category]:
        to_do_list[category][task] = True
    else:
        print(f"Task '{task}' does not exist in category '{category}'.")

# Function to display all tasks
def display_completed():
    for category, tasks in to_do_list.items():
        print(f"Category: {category}")
        for task, is_complete in tasks.items():
            status = "Done" if is_complete else "Incomplete"
            print(f"{task} - {status}")

# Call the display_tasks function
#display_tasks()
#call the function
display_completed()

