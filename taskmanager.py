task=[]

def add_task(task_list, description):

    task_id=len(task_list)+1
    new_task={
        "id" : task_id,
        "description" : description,
        "completed" : False
    }
    task_list.append(new_task)
    print(f"Task '{description}' added to the task list.\nTask ID: {task_id}")

def get_task(task_list, task_id):

    for task in task_list:
        if task["id"] is task_id:
            return task
    return None

def mark_task_completed(task_list, task_id):
    
    task = get_task(task_list, task_id)
    if task:
        if not task["completed"]:
            task["completed"] = True
            print(f"Task '{task["description"]}' with Task ID as '{task_id}', is marked completed.")
        else:
            print(f"Task '{task["description"]}' with Task ID as {task_id}, was already marked completed.")
    else:
        print(f"Error: Not task found with Task ID as {task_id}.")

def display_tasks(task_list):
    
    if not task_list:
        print(f"Looks like the task list is empty. Add new tasks to display them.")
        return
    
    print("----Task List----\n")
    for task in task_list:
        status="[X]" if task["completed"] else "[ ]"
        print(f"{status} ID: {task["id"]} - {task["description"]}")
    print("----------------------------")


def main():
    print("----Welcome to Task Manager----",end="")
    

    while True:
        print("\n\nChoose an option from below:-")
    
        choice = int(input("1.Add Task\n2.Mark a task completed\n3.Display all the tasks\n4.Exit\n"))

        match choice:
          case 1:
             description = input("Enter the description of the task: ")
             add_task(task,description)
          case 2:
             task_id = int(input("Enter ID of the task completed: "))
             mark_task_completed(task,task_id)
          case 3:
             display_tasks(task)
          case 4 | _: 
             return

main()
    
