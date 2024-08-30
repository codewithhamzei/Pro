# To Do List -- Add Task, Set Time For Task, Method -- Add,Remove,Update,View Tasks
task = []

try:
  task_add = int(input("How Many Task Did You Want To Add:"))

  for i in range(1,task_add+1):
    add = input(f"Enter Task {i} = ")
    task.append(add)
    
  print(f"\nToday Task Are {task}\n")

except ValueError:
  print("Enter str Not Number")  


def method():
  while True:
    # Set Time Or Method
    opertaions = int(input(" 1--> Want To Set Time For Your Task:\n 2--> Mehtod Of To do list\n 3-->Exit\n >> "))

    # Set Time
    if opertaions == 1:
      while True:
        try:
          user = int(input(" 1--Add Time \n 2--Exit:\n>>"))
          if user == 1:
            set_times = input(f"Enter Task name To Set Time {task}:")
            if set_times in task:
              time = int(input(f"Times For {set_times} (int) : "))
              todolist = {}
              todolist.update({set_times : time})
              print(f"{todolist} Added")    
            else:
              print(f"This Task {set_times} Are Not In Todilist")

          elif user == 2:
              print("Times Portion Ended")
              break
        except Exception as e:
          print(e)


    elif opertaions == 2:
      while True:
        user = int(input("1--Add\n2--Update\n3--Delete\n4--View\n5--Exit\n>>"))

        if user == 1:
          add = input("Enter Task:")
          task.append(add )
          print(f"\nTask {add} Addded Into lsit {task}\n")

        elif user == 2:
          print(f"Which Task Did You Want To Update: {task}")
          update_task = input("Write Task Name To Update:")
          if update_task in task:
            index_checking = task.index(update_task)
            new_task = input(f"Enter New Task:")
            task[index_checking] = new_task
            print(f"New Task {new_task} Added Into List")
          else:
            print(f"This Task {update_task} Are Not In The List")  

        elif user == 3:
          print(f"Which Task Did You Want To Delete: {task}")
          delete_task = print("Writes It's Name Here's:")
          if delete_task in task:
            index_checking = task.index(delete_task)
            del task[delete_task]
            print(f"Task {delete_task} Are Deleted")
          else:
            print("Task Are Not In The List")  

        elif user == 4:
          print("Today Task Are")
          print(task)
          print(f"Their Time to do {todolist}")

        elif user == 5:
          print("---- Method Ended ----")
          break

        else:
          print("You Put Wrong Number")

    elif opertaions == 3:
      print("---- Todolist Ended ----")
      break


method()
