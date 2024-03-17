# -------------------Importing Libraries --------------------------------------

from datetime import date


# ----------------------- Functions -------------------------------------------
# This function only allow the admin user to register new user accounts
def reg_user(admin):
    while True:
        if admin == 'admin':
            username_ = input("Please enter a username: ")
            with open('user.txt', 'a+') as io_file:
                # Move the cursor to the beginning of the file
                io_file.seek(0)
                file_list = io_file.readlines()
                for _lines in file_list:
                    user_ = _lines.strip().split(',')
                    if username_ == user_[0].strip():
                        print("That username already exists!!")
                        break
                # Executed if the loop completes without finding a
                # duplicate username
                else:
                    password_ = input("Please create a new password: ")
                    password_confirmation = input("Please confirm your "
                                                  "password: ")
                    # Check if password and password confirmation are the same
                    if password_ != password_confirmation:
                        print("Your password confirmation is not the same as "
                              "your password")
                    else:
                        with open('user.txt', 'a+') as file_out:
                            file_out.write(f"\n{username_}, {password_}")
                            print("\nYou have successfully registered a user!"
                                  "\n")
                    # Exit the loop after successful registration
                    break
        else:
            # Exit the loop if the username is not 'admin'
            print("You are not authorized to perform this function!")
            break


# This function creates a new task and add it to the tasks.txt file
def add_task():
    _username = input("Please enter the username of the person whom the"
                      "task is assigned to: ").lower()
    task_title = input("Please enter the title of the task: ")
    task_description = input(
        "Please type the description of the task: ")
    task_due_date = input(
        "Please enter the due date of the task in the "
        "format - 01 Sep 2024: ")
    current_date = date.today()
    task_done = "No"
    # write the contents to the file
    with open('tasks.txt', 'a+') as f_output:
        f_output.write(f"\n{_username}, {task_title}, {task_description}, "
                       f"{task_due_date}, {current_date}, {task_done}")
    print("\nYou have successfully added task!\n")


# This function displays all the tasks in tasks.txt file
def view_all():
    with open('tasks.txt', 'r') as f_input:
        the_lines = f_input.readlines()
        # print a solid line using ext. ASCII
        print(u'\u2501' * 80)
        for each_line in the_lines:
            _user_ = each_line.strip().split(',')
            # display the contents that are in the file
            print(f"Task:\t\t\t{_user_[1]}\nUsername:\t\t {_user_[0]}")
            print(f"Due date:\t\t{_user_[3]}\nCurrent date: "
                  f"\t{_user_[4]}")
            print(
                f"Task complete?\t{_user_[5]}\nTask description:"
                f"\n{_user_[2]}\n")
        print(u'\u2501' * 80)


# This function displays the tasks of the currently logged on user
def view_mine(admin):
    # List to store tasks for display
    task_list = []

    with open('tasks.txt', 'r') as f_in:
        print(u'\u2501' * 80)
        # Initialize task number
        task_number = 1
        for line_ in f_in:
            _user = line_.strip().split(',')
            # Check if the username matches the admin parameter
            if admin == _user[0]:
                # Add task to list for display
                task_list.append(_user)
                print(f"{task_number}. Task:\t\t{_user[1]}\n   Username:\t\t "
                      f"{_user[0]}")
                print(f"   Due date:\t\t{_user[3]}\n   Current date: "
                      f"\t{_user[4]}")
                print(
                    f"   Task complete?\t{_user[5]}\n   Task description:\n   "
                    f"{_user[2]}\n")
                # Increment the task number by one after every iteration
                task_number += 1
        print(u'\u2501' * 80)

    # Allow user to select a task or return to main menu
    while True:
        # provide user with options to select from
        choice = input("Enter task number to select a task, or enter -1 to "
                       "return to main menu: ")
        if choice == '-1':
            # Return to main menu
            break
        # valid option choice
        elif choice.isdigit() and 1 <= int(choice) <= len(task_list):
            task_index = int(choice) - 1
            selected_task = task_list[task_index]
            print(f"Selected Task: {selected_task[1]}")
            # provide user with action choices
            action = input("Enter 'complete' to mark the task as complete, "
                           "'edit' to edit the task, or 'cancel' to go back: ")
            if action == 'complete':
                complete = input("Mark task as complete? (yes/no): ").lower()
                if complete == 'yes':
                    selected_task[5] = 'yes'
                    print("Task marked as complete.")
                    # updating the changes to tasks.txt file
                    with open('tasks.txt', 'w') as file_output:
                        for task in task_list:
                            file_output.write(','.join(task) + '\n')
                    break
                elif complete == 'no':
                    print("Task not marked as complete.")
                    break
                else:
                    print("Invalid input.")
            elif action == 'edit':
                if selected_task[5].lower() == 'no':
                    new_username = input("Enter new username or press Enter "
                                         "to keep the current one: ")
                    new_due_date = input("Enter new due date or press Enter "
                                         "to keep the current one: ")
                    if new_username:
                        selected_task[0] = new_username
                    if new_due_date:
                        selected_task[3] = new_due_date
                    print("Task edited successfully.")
                    break
                else:
                    print("Task is already marked as complete. Cannot edit.")
            elif action == 'cancel':
                # Return to main menu
                break
            else:
                print("Invalid action. Please enter 'complete', 'edit', "
                      "or 'cancel'.")
        else:
            print("Invalid input. Please enter a valid task number.")


# This functions only displays the logged on user tasks
def display_stats(username):
    # only admin user can display statistics
    if username == 'admin':
        print(u'\u2501' * 80)
        print("              Tasks Statistics                ")
        print(u'\u2501' * 80)
        # open task_overview.txt and read and display each line
        with open('task_overview.txt', 'r') as input_file:
            lines = input_file.readlines()
            for line_ in lines:
                print(line_)
        print(u'\u2501' * 80)
        print("               Users Statistics               ")
        print(u'\u2501' * 80)
        # open the user_overview.txt and read and display each line
        with open('user_overview.txt', 'r') as file_input:
            lines_ = file_input.readlines()
            for _line in lines_:
                # display the information contained in each line
                print(_line)
    # error handling for non-admin users
    else:
        print("You are not authorized to view stats!")


# Task overview function to tracks task statistics and save them to a file
# called task_overview.txt
def task_overview():
    total_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0
    # open tasks.txt file to read contents and do statistics
    with open('tasks.txt', 'r') as f_input:
        for _line in f_input:
            total_tasks += 1
            task_done = _line.strip().split(',')[5]
            if task_done.lower() == 'yes':
                completed_tasks += 1
            else:
                uncompleted_tasks += 1
                task_due_date = _line.strip().split(',')[3]
                if task_due_date < str(date.today()):
                    overdue_tasks += 1

    total_incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
    total_overdue_percentage = (overdue_tasks / total_tasks) * 100

    # create task_overview.txt file to write the tasks.txt statistics
    with open('task_overview.txt', 'w') as file_out:
        file_out.write("Task Overview Report\n")
        file_out.write(f"Total number of tasks: {total_tasks}\n")
        file_out.write(f"Total number of completed tasks: {completed_tasks}\n")
        file_out.write(
            f"Total number of incomplete tasks: {uncompleted_tasks}\n")
        file_out.write(
            f"Total number of incomplete and overdue tasks: "
            f"{overdue_tasks}")
        file_out.write(
            f"\nPercentage of tasks that are incomplete: "
            f"{total_incomplete_percentage:.2f}%\n")
        file_out.write(
            f"Percentage of tasks that are overdue: "
            f"{total_overdue_percentage:.2f}%\n")


# The user report - tracks the user statistics, i.e. the number of incomplete
# tasks, the number of completed tasks, the number of overdue tasks etc
def user_overview():
    total_tasks = 0
    total_users = 0
    user_task_count = {}
    user_completed_task_count = {}
    user_incomplete_task_count = {}
    user_overdue_task_count = {}
    # open the user.txt to read to count users registered
    with open('user.txt', 'r') as f_input:
        for line_ in f_input:
            total_users += 1
            usernames = line_.strip().split(',')[0]
            user_task_count[usernames] = 0
            user_completed_task_count[usernames] = 0
            user_incomplete_task_count[usernames] = 0
            user_overdue_task_count[usernames] = 0
    # open the tasks.txt, track for tasks and whether are complete, overdue/not
    with open('tasks.txt', 'r') as f_input:
        for _line in f_input:
            total_tasks += 1
            _username = _line.strip().split(',')[0]
            user_task_count[_username] += 1
            task_done = _line.strip().split(',')[5]
            if task_done.lower() == 'yes':
                user_completed_task_count[_username] += 1
            else:
                user_incomplete_task_count[_username] += 1
                task_due_date = _line.strip().split(',')[3]
                if task_due_date < str(date.today()):
                    user_overdue_task_count[_username] += 1
    # create a user_overview and write to it the user statistics
    with open('user_overview.txt', 'w') as file_1_out:
        file_1_out.write("User Overview Report\n")
        file_1_out.write(f"Total number of users registered: {total_users}\n")
        file_1_out.write(f"Total number of tasks: {total_tasks}\n")
        for username_ in user_task_count:
            total_tasks_assigned = user_task_count[username_]
            completed_tasks_assigned = user_completed_task_count[username_]
            incomplete_tasks_assigned = user_incomplete_task_count[username_]
            overdue_tasks_assigned = user_overdue_task_count[username_]
            if total_tasks_assigned == 0:
                tasks_assigned_percentage = 0
            else:
                tasks_assigned_percentage = (total_tasks_assigned /
                                             total_tasks) * 100
            if completed_tasks_assigned == 0:
                completed_tasks_percentage = 0
            else:
                completed_tasks_percentage = (completed_tasks_assigned /
                                              total_tasks_assigned) * 100
            if incomplete_tasks_assigned == 0:
                incomplete_tasks_percentage = 0
            else:
                incomplete_tasks_percentage = (incomplete_tasks_assigned /
                                               total_tasks_assigned) * 100
            if overdue_tasks_assigned == 0:
                overdue_tasks_percentage = 0
            else:
                overdue_tasks_percentage = (overdue_tasks_assigned /
                                            total_tasks_assigned) * 100
            # writing data to the file
            file_1_out.write(f"\nUser: {username_}\n")
            file_1_out.write(
                f"Percentage of total tasks assigned: "
                f"{tasks_assigned_percentage:.2f}%\n")
            file_1_out.write(
                f"Percentage of completed tasks assigned: "
                f"{completed_tasks_percentage:.2f}%\n")
            file_1_out.write(
                f"Percentage of incomplete tasks assigned: "
                f"{incomplete_tasks_percentage:.2f}%\n")
            file_1_out.write(
                f"Percentage of incomplete and overdue tasks assigned: "
                f"{overdue_tasks_percentage:.2f}%\n")


# -----------------------Login Section ----------------------------------------
"""
write code that will allow a user to login. - Your code must read usernames 
and password from the user.txt file with use of a while loop to validate your
username and password
"""
while True:
    admin_username = input("Enter username: ").lower()
    password = input("Enter password: ").lower()
    # open user.txt for reading contents
    with open('user.txt', 'r') as file_in:
        users_list = file_in.readlines()
        authenticated = False  # Flag to track authentication status
        for line in users_list:
            user = line.strip().split(',')
            # check if the username and password match the credentials in
            # user.txt
            if (admin_username == user[0].strip()
                    and password == user[1].strip()):
                print(f"Welcome Back {user[0]}!\n")
                authenticated = True  # Set authentication flag to True
                break
        if not authenticated:  # If authentication failed
            print("Incorrect username or password!\n")
        else:
            break  # Exit the loop if authentication is successful

# ----------------------------- User Options ----------------------------------
while True:
    # ------------------ Present Menu to the user ---------------------------
    menu = input('''Select one of the following options:
            r - register a user
            a - add task
            va - view all tasks
            vm - view my tasks
            gr - generate reports
            ds - display statistics
            e - exit : ''').lower()

    # ---------------- 1. Register a user 'r' ---------------------------------
    if menu == 'r':
        reg_user(admin_username)
    # ----------------- 2. Add task 'a'---------------------------------------
    elif menu == 'a':
        add_task()
    # ------------------ 3. View all tasks 'va'--------------------------------
    elif menu == 'va':
        view_all()
    # ------------------- 4. View my tasks 'vm'--------------------------------
    elif menu == 'vm':
        view_mine(admin_username)

    # ----------------- 5. generate reports 'gr' -----------------------------
    elif menu == 'gr':
        task_overview()
        user_overview()

    # ------------------ 6. display statistics 'ds' --------------------------
    elif menu == 'ds':
        # generate reports if not already generated
        task_overview()
        user_overview()
        # display stats if the username is 'admin'
        display_stats(admin_username)

    # ----------------- 7. Exit 'e'--------------------------------------------
    elif menu == 'e':
        # print exit message and exit the program
        print('Goodbye!!!')
        exit()
    # ----------------- 6. Invalid input -------------------------------------
    else:
        print("You have entered an invalid input. Please try again")
