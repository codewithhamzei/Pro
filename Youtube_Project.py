# Student Grade Management System In Python

"""student = {}

# Add Student Name And Grades
def add_student(name,grades):
  student[name] = grades
  print(f"\nStudent {name} And Grades {grades} Added:")


# Update Student Grades
def update_student(name):
  if name in student:
    grades = int(input("Enter New Grades:"))
    student[name] = grades
    print(f"\n{name} Grades Updated {grades}")


# Delete Student
def delete_student(name):
  del student[name]
  print(f"{name} Is Deleted")    

# View 
def view():
  for key in student.keys():
    print(f"{key} : {student[key]}")  """

"""while True:
  user = int(input("""
  # 1. Add Student Name And Grades 
  # 2. Update Student Grades
  # 3. Delete Student
  # 4. View Student
  # 5. Exit
  # > """))


"""  if user == 1:
    name = input("Enter Your Name:")
    grades = int(input("Enter Your Grades:"))
    add_student(name, grades)

  elif user == 2:
    name = input("Enter Your Name:")
    update_student(name)

  elif user == 3:
    name = input("Enter Name To Delete:")
    delete_student(name)  

  elif user == 4:
    view()  

  elif user == 5:
    break  """


# Hotel Management System

"""def menu():
    menus = {
        "Pizza": 120,
        "Coffee": 100,
        "Mango Juice": 50,
        "Sting": 140,
        "Biryani": 200
    }      
    for key in menus.keys():
       print(f"{key} : Rs {menus[key]}")

    orders = 0
    while True:
        user = input("What You Want To Order:")

        if user in menus:
            print(f"Your Order {user} Added Into List")
            orders+=menus[user]
            
            while True:
                user1 = input("Did You Want To Order More Elements:")

                if user1.lower() == "no":
                    print(f"Total Bills Is {orders}")
                    print("Thanks")  
                    break

                if user1 in menus:
                    print(f"Order Addded")
                    orders+=menus[user1]
                else:
                    print("Item Not Present")    
            break            

        elif user.lower() == "no":
            print(f"\nTotal Bills Is {orders}")
            print("Thanks")   
            break


        else:
            print("Order Not Found")     

name = input("Your Name:")
if len(name)<3:
    raise ValueError("Name Should Contain More Then 5 Characters")

print(f"Welcome {name} To Our Hotel")
print("Here is the menu")
menu()"""

