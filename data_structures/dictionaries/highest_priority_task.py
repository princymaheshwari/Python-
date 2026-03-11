# Highest Priority Task
# Given a dictionary tasks where keys are task names and values are priorities (1-10, where 10 is the highest priority), write a function get_highest_priority_task() that removes the task with the highest priority from the dictionary and returns its name.
# If two tasks have the same priority, return the task that comes first in the alphabet.

def get_highest_priority_task(tasks):

    highest_priority = max(tasks.values())
    highest_priority_tasks = [task for task in tasks if tasks[task]== highest_priority]
    highest_priority_task = sorted(highest_priority_tasks)[0]
    del tasks[highest_priority_task]
    return highest_priority_task
    

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)