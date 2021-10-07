import datetime


# Create boolean for while loop
user_log_in = True
menus = False
admin = False
gen_user = False
error_message = True

# Function to add users by reading each line of user.txt file 

def user_reg(): # <----------------------------------------
    new_username = input("Enter a new username: ")
    new_password = input("Enter a new password: ")
    password_check = input("Please re-enter a password: ")
    username_check = new_username
    f = open('user.txt', 'r')
    w = open('user.txt', 'a')
    t = f.readlines()
    for line in t:
        line = line.split(',')
        username = line[0]
        if username_check == line[0]:
            print("Username already taken, please try again.")
            user_reg()
    if new_password == password_check:  
        combo = new_username + ',' + ' ' + password_check
        w.write("\n" + combo)
    print("Your details have been saved for login")
    if new_password != password_check:
        print("Sorry your passwords don't match")

# Function to add a task adn assign it to a specefic user

def add_task():
    p = open('tasks.txt', 'a')
    user_task = input("Who is this task assigned to:\n")
    title_task = input("What is the Title of the task:\n")
    desc_task = input("What is the task:\n")
    today_date = input("What is today's date: (YYYY-M-D H:M)\n")
    due_date = input("When is the task due: (YYYY-M-D H:M)\n")
    completed = "No"
    combo = (user_task + ", " + title_task + ", " + desc_task + ", " + today_date + ", " + due_date
             + ", " + completed)
    p.write("\n" + combo)
    print(f"Task has been added to {user_task}")

# function to read all users tasks

def va_tasks():
    v = open('tasks.txt', 'r')
    print("All Tasks\n")
    for lines in v:
        line1 = lines.split(",")[0].lower()
        line2 = lines.split(",")[1]
        line3 = lines.split(",")[2]
        line4 = lines.split(",")[3]
        line5 = lines.split(",")[4]
        line6 = lines.split(",")[5]
        print(f"Task Assigned to:\t {line1}\nTask Title:\t\t{line2}\nTask Description:\t{line3}\n"
                f"task was created:\t{line4}\nDue Date:\t\t{line5}\ntask completed\t\t{line6}")


# function to view all tasks assigned to the logged in user
        
def vm_tasks():
    indexes1 = []
    m = open('tasks.txt', 'r')
    y = m.readlines()
    count = -1
    displayed_count = 0
    for task in y:
        count +=1
        task_tempvariable = task.split(", ")
        if task_tempvariable[0]  == task_tempvariable[0]:
                displayed_count += 1
                indexes1.append(count)
                task = task.split(", ")
        if username == task[0]:
            print(f"""task number:{displayed_count}
Task Assigned to:   {task_tempvariable[0]}
Task Title:         {task_tempvariable[1]}
Task Description:   {task_tempvariable[2]}
Task was created:   {task_tempvariable[3]}
Due Date:           {task_tempvariable[4]}
Task completed:     {task_tempvariable[5]}
                      """)

# let the user select a task number to make changes or -1 to go back to main menu

    task_number = input("Please enter a task number to edit or -1 to return to main menu:\n")
    if task_number == "-1":
        menu2 = input("""
Please select one of the following options:
r - register user
a - add task
va - view all task
vm - view my tasks
st - statistics
gr - generate report
ds - display statistics
e - exit
""")
    displayed_task_num = int(task_number)
    real_Index = indexes1[displayed_task_num - 1]
    x = y[real_Index]
    x = x.split(", ")
    if displayed_task_num == displayed_task_num:
        print(f"""Task number {displayed_task_num}
Task Assigned to:   {x[0]}
Task Title:         {x[1]}
Task Description:   {x[2]}
Task was created:   {x[3]}
Due Date:           {x[4]}
Task completed:     {x[5]}       
        """)

# if the user would like to mark the task completed or edit they can select the options below 

    options = input(f"Would you like to mark Task {displayed_task_num} as completed or edit this task: (Please enter c to complete or e to edit)").lower()
    if options == "c":
        s = x[5].replace("No", "Yes") 
        y[real_Index] = f"{x[0]}, {x[1]}, {x[2]}, {x[3]}, {x[4]}, {s}"
        with open('tasks.txt' , 'w') as w:
            w.writelines(y)
    if options =="c" and x[5] == "Yes":
        print("Task already completed")
    if options == "e" and x[5] == "Yes":
        print("Cant edit a completed task")
    if options == "e" and x[5] == "No":
        n1 = x[0]
        dd = x[4]
        edit = input(f"Would you like to edit the username or due date of Task {displayed_task_num}: (please enter n for name dd for due date or b for both)").lower()
        if edit == "n":
            n = x[0].replace(n1, input("Please enter name for person responsible for task: "))
            y[real_Index] = f"{n}, {x[1]}, {x[2]}, {x[3]}, {x[4]}, {x[5]}"
            with open('tasks.txt' , 'w') as w:
                w.writelines(y)
        if edit == "dd":
            a = x[4].replace(dd, input("Please enter new due date: (YYYY-M-D H:M)"))
            y[real_Index] = f"{x[0]}, {x[1]}, {x[2]}, {x[3]}, {a}, {x[5]}"
            with open('tasks.txt' , 'w') as w:
                w.writelines(y)
        if edit == "b":
            n = x[0].replace(n1, input("Please enter name for person responsible for task: "))
            a = x[4].replace(dd, input("Please enter new due date: (YYYY-M-D H:M)"))
            y[real_Index] = f"{n}, {x[1]}, {x[2]}, {x[3]}, {a}, {x[5]}"
            with open('tasks.txt' , 'w') as w:
                w.writelines(y)

        
# Display statistics of tasks that have been completed not completed or overdue

def display_statistics():
    with open('task_overview.txt', 'r') as to:
        print("Task Overview")
        for line in to:
            print(line.replace("\n", ""))
    with open('user_overview.txt', 'r') as to:
        print("user Overview")
        for line in to:
            print(line.replace("\n", ""))


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

# Generate reports to calculate how many tasks have been tracked, completed or overdue.

def generate_reports(): 
    present = datetime.date.today()
    r = open('tasks.txt', 'r')
    u = open('user.txt', 'r')
    w = open('task_overview.txt', 'w') 
    uo = open('user_overview.txt', 'w')
    with open('tasks.txt', 'r') as t:
        task_counter = 0
        c_tasks = 0
        o_tasks = 0
        user_counter = 0
        yes_counter = 0
        no_counter = 0 
        overdue = 0
        not_overdue =0
        reg_user = 0
        user_over = 0
        content = t.read()
        contents = content.split(", ")
        co_list = content.split("\n")
    with open('user.txt', 'r'):
        users = u.read()
        user_line = users.split("\n")
    for i in user_line:
        reg_user += 1
    for i in co_list:
        date_list = []
        task_counter += 1
        new_content = i.split(", ")
        CurrentDate = datetime.datetime.now()
        #print(CurrentDate)
        overdue_date = new_content[4]
        overdue_date = datetime.datetime.strptime(overdue_date, "%Y-%m-%d")
        #print(overdue_date)
        if CurrentDate > overdue_date and new_content[5] == "No":
            overdue +=1
        else:
            not_overdue += 1
        if CurrentDate > overdue_date and new_content[0] == username:    
            user_over += 1    
        if new_content[5] == "No":
            o_tasks += 1
        if new_content[5] == "Yes":
            c_tasks += 1

        if username == new_content[0]:
            user_counter += 1  # counts how many tasks assigned to that user

        if new_content[5] == "Yes" and username == new_content[0]:
            yes_counter += 1# count yes to tasks asigned to user

        if new_content[5] == "No" and username == new_content[0]:
            no_counter += 1 # count No tasks assigned to

    task_percent = user_counter / task_counter * 100
    overdue_percent = overdue / user_counter * 100
    incompleted_percent = overdue / task_counter * 100
    user_percent_completed = yes_counter / user_counter * 100
    user_percent_not_completed = no_counter / user_counter * 100
    if i in co_list:
        overdue2_percent = overdue / task_counter * 100
        complete_percent = c_tasks / task_counter * 100
        incomplete_percent = o_tasks / task_counter * 100
        w.write(f"""There is a total of {task_counter} tasks generated and tracked with Task Manager.
There is {c_tasks} completed tasks.
There is {o_tasks} not completed tasks.
There is {overdue} tasks overdue.
There is {round(incomplete_percent, 2)}% incompleted tasks.
There is {round(overdue2_percent, 2)}% of tasks overdue.""")

        uo.write(f"""There is a total of {reg_user} users registered with Task Manager.
There is a total number of {task_counter} tasks registered with task manager.
There is a total of {user_counter} tasks assigned to {username}.
There is a total of {round(task_percent, 2)}% of tasks assigned to {username}.
There is a total of {round(user_percent_completed, 2)}% of tasks asigned to {username} completed.
There is {round(user_percent_not_completed, 2)}% of tasks assigned to {username} not completed.
There is {round(overdue2_percent, 2)}% overdue.""")





while admin:
    menu2 = input("""
Please select one of the following options:
r - register user
a - add task
va - view all task
vm - view my tasks
st - statistics
gr - generate report
ds - display statistics
e - exit
""")
    if menu2 == "r":  
        user_reg()
    if menu2 == "a": 
        add_task()
    if menu2 == "va":
        va_tasks()
    if menu2 == "vm":  # view tasks assigned to the user that is logged in by checking username
        vm_tasks()
    if menu2 == "gr":
        generate_reports()
    if menu2 == "ds":
        display_statistics()
    if menu2 == "e":  # if selected end program from beginning
        admin = False

while gen_user:
    menu1 = input("Please select one of the following options:"
                  "\na - add task\nva - view all task\n"
                  "vm - view my tasks\ne - exit \n")
    if menu1 == "a":
        add_task()
    if menu1 == "va":
        va_tasks()
    if menu1 == "vm":
        vm_tasks()
    if menu1 == "e":
        gen_user = False

