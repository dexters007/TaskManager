import re
# Create boolean for while loop
user_log_in = True
menus = False
admin = False
gen_user = False
error_message = True

# Use a while loop to continue to ask a user for credentials until correct

while user_log_in:
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")
    for line in open('user.txt', 'r').readlines():
        login_info = line.split()
        if username == login_info[0].replace(",", "") and username == "admin" and password == login_info[1]:
            user_log_in = False
            admin = True
        if username == login_info[0].replace(",", "") and username != "admin" and password == login_info[1]:
            user_log_in = False
            gen_user = True
    else:
        print("Wrong Username or Password.")

# Once credentials have been verified and user is Admin print admin menu

while admin:
    menu2 = input("Please select one of the following options:" 
                  "\nr - register user\na - add task\nva - view all task\n" 
                  "vm - view my tasks\nst - statistics\ne - exit \n")
    if menu2 == "r":  # if r is selected register a user ad write it to user.txt
        with open('user.txt', 'a') as r:
            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            password_check = input("Please re-enter a password: ")
            if new_password == password_check:  # check if password matches password check to confirm password
                combo = new_username + ',' + ' ' + password_check 
                r.write("\n" + combo)
                r.close()
                print("Your details have been saved for login")
            if new_password != password_check:
                print("Sorry your passwords don't match")
    if menu2 == "a":  # add a task and write it to tasks.txt
        with open('tasks.txt', 'a') as p:
            user_task = input("Who is this task assigned to:\n")
            title_task = input("What is the Title of the task:\n")
            desc_task = input("What is the task:\n")
            today_date = input("What is today's date: (eg-01/Jan/2021)\n")
            due_date = input("When is the task due: (eg-01/Jan/2021)\n")
            completed = "No"
            combo = (user_task + ", " + title_task + ", " + desc_task + ", " + today_date + ", " + due_date
                     + ", " + completed)
            p.write("\n" + combo)
            print(f"Task has been added to {user_task}")
    if menu2 == "va":
        with open('tasks.txt', 'r') as t:  # View all tasks for all users by reading second string in tasks.txt
            print("All Tasks\n")
            for lines in t:
                line1 = lines.split(",")[0].lower()
                line2 = lines.split(",")[1]
                line3 = lines.split(",")[2]
                line4 = lines.split(",")[3]
                line5 = lines.split(",")[4]
                line6 = lines.split(",")[5]
                print(f"Task Assigned to:\t {line1}\nTask Title:\t\t\t{line2}\nTask Description:\t{line3}\n"
                      f"task was created:\t{line4}\nDue Date:\t\t\t{line5}\ntask completed\t\t{line6}")
    if menu2 == "vm":  # view tasks assigned to the user that is logged in by checking username
        with open('tasks.txt', 'r') as tasks:
            for task in tasks:
                for match in re.finditer(username, task):
                    task1 = task.split(",")[0].lower()
                    task2 = task.split(",")[1]
                    task3 = task.split(",")[2]
                    task4 = task.split(",")[3]
                    task5 = task.split(",")[4]
                    task6 = task.split(",")[5]
                    vm_task = task1, match.group()
                    print(f"Task Assigned to:\t {task1}\nTask Title:\t\t\t{task2}\nTask Description:\t{task3}\n"
                          f"task was created:\t{task4}\nDue Date:\t\t\t{task5}\ntask completed\t\t{task6}")
    if menu2 == "st":  # Print statistics by counting lines and displaying how many users and tasks there are
        with open('tasks.txt', 'r') as t:
            va_counter = 0
            content = t.read()
            co_list = content.split("\n")
            for i in co_list:
                if i:
                    va_counter += 1
        with open('user.txt', 'r') as t:
            va_counter = 0
            content = t.read()
            co_list = content.split("\n")
            for i in co_list:
                if i:
                    va_counter += 1
        print(f"There is currently {va_counter} tasks to do and {va_counter} users registered")
    if menu2 == "e":  # if selected end program from beginning
        admin = False


while gen_user:
    menu1 = input("Please select one of the following options:"
                  "\na - add task\nva - view all task\n"
                  "vm - view my tasks\ne - exit \n")
    if menu1 == "a":
        with open('tasks.txt', 'a') as p:
            user_task = input("Who is this task assigned to:\n")
            title_task = input("What is the Title of the task:\n")
            desc_task = input("What is the task:\n")
            today_date = input("What is today's date:(eg-01/Jan/2021)\n")
            due_date = input("When is the task due:(eg-01/Jan/2021)\n")
            completed = "No"
            combo = (user_task + ", " + title_task + ", " + desc_task + ", " + today_date + ", " + due_date
                     + ", " + completed)
            p.write("\n" + combo)
            print(f"\nTask has been added to {user_task}")
    if menu1 == "va":
        with open('tasks.txt', 'r') as t:  # View all tasks for all users by reading second string in tasks.txt
            print("All Tasks\n")
            for lines in t:
                line1 = lines.split(",")[0].lower()
                line2 = lines.split(",")[1]
                line3 = lines.split(",")[2]
                line4 = lines.split(",")[3]
                line5 = lines.split(",")[4]
                line6 = lines.split(",")[5]
                print(f"Task Assigned to:\t {line1}\nTask Title:\t\t\t{line2}\nTask Description:\t{line3}\n"
                      f"task was created:\t{line4}\nDue Date:\t\t\t{line5}\ntask completed\t\t{line6}")
    if menu1 == "vm":
        with open('tasks.txt', 'r') as tasks:
            for task in tasks:
                for match in re.finditer(username, task):
                    task1 = task.split(",")[0].lower()
                    task2 = task.split(",")[1]
                    task3 = task.split(",")[2]
                    task4 = task.split(",")[3]
                    task5 = task.split(",")[4]
                    task6 = task.split(",")[5]
                    vm_task = task1, match.group()
                    print(f"Task Assigned to:\t {task1}\nTask Title:\t\t\t{task2}\nTask Description:\t{task3}\n"
                          f"task was created:\t{task4}\nDue Date:\t\t\t{task5}\ntask completed\t\t{task6}")
    if menu1 == "e":
        gen_user = False
