#🐍 Day 27: Tick Tock: Mastering Date and Time 🐍
#get date and time
#from typing import List
from datetime import datetime, timedelta
now = datetime.now()
print(f"time is :{now}")
#add two days
future_date = now + timedelta(days=2)
print(f"two days from now is:{future_date}")
'''
Homework: Add Time to Your To-Do List App
Current Time: Display the current date and time whenever a task is added or completed.
Task Deadline: Allow users to set a deadline for tasks and display overdue tasks.
Advanced: Can you make your app send reminders? (This one's tricky, but give it a try!)
'''
#Current Time: Display the current date and time whenever a task is added or completed.
'''
to_do_list = { 
   "Personal": {
       "Buy groceries": False,
       "Go to gym": True,
       "Learn Python": True,
       "Apply for atleast 1 job a day": True,
       "Read a chapter a day": False
   },
    "Work": {},
}
now = datetime.now()
def add_task(category,task):
    if category not in to_do_list:
        to_do_list[category] = {}
    to_do_list[category][task] = False
    #now = datetime.now()
    #print(f"time is :{now}")
user = input("Enter category: ")
if user in to_do_list:
    task = input("Enter task: ")
    add_task(user,task)
else:
    print(f"Category '{user}' does not exist but has been added.")
    task = input("Enter task: ")
    add_task(user,task)
    now = datetime.now()
def task_completed(category,task,now):
    now = datetime.now()   
    if category in to_do_list and task in to_do_list:
        for category,task, is_complete in to_do_list.items():
         if is_complete:
            status ="Done"
            print(f"{category}{task} - {status}")
         else:
            status = "Incomplete"
            print(f"{category}{task} - {status}")
'''
#def task_completed(category,task,now):'''


to_do_list = {
    "Personal": {
        "Buy groceries": (False, None),
        "Go to gym": (True, None),
        "Learn Python": (True, None),
        "Apply for atleast 1 job a day": (True, None),
        "Read a chapter a day": (False, None)
    },
    "Work": {},
}

def add_task(category, task,days):
    if category not in to_do_list:
        to_do_list[category] = {}

    now  = datetime.now()
    days = int(days)
    
    to_do_list[category][task][days] = (False, now)
    print(f"Task '{task}' added to '{category}' at {now}")

user = input("Enter category: ")

if user in to_do_list:
    
    task = input("Enter task: ")
    days = input("Enter deadline in days: ")
    add_task(user, days, task)
if user =="q":
    print("bye!")
    exit()
else:
    print(f"Category '{user}' does not exist but has been added.")
    task = input("Enter task: ")
    days = input("Enter deadline in days: ")
    #future_date = now + timedelta(days=days)
    add_task(user, days, task)

def task_completed(category, task, days):
    for cat, tasks in to_do_list.items():
        for task_name, (is_complete, added_time) in tasks.items():
            if cat == category and task_name == task:
                if is_complete:
                    status = "Done"
            else:
                if   datetime.now()>timedelta(days=int()) :
                    status = "task is overdue"
                print(f"{category} {task_name} - {status} (Added at {added_time})")

'''def task_deadline(category, task, deadline):
    for cat, tasks in to_do_list.items():
        for task_name, (is_complete, added_time) in tasks.items():
            if cat == category and task_name == task:
                if is_complete:
                    status = "Done"

                else:
                    status = "Incomplete"
                print(f"{category} {task_name} {deadline}- {status} (Added at {added_time})")
'''

