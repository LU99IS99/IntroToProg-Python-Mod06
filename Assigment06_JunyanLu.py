# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Your Name>,<Date>,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processing  --------------------------------------------------------------- #
class Processor:
    """Performs Processing tasks"""

    @staticmethod
    def read_data_from_file(file_name):
        """Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file
        :return: (list) of dictionary rows
        """
        list_of_rows = []
        try:
            with open(file_name, "r") as file:
                for line in file:
                    task, priority = line.strip().split(",")
                    row = {"Task": task, "Priority": priority}
                    list_of_rows.append(row)
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Creating a new file.")
            open(file_name, "w").close()  # Create an empty file if not found

        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """Adds data to a list of dictionary rows

        :param task: (string) with name of task
        :param priority: (string) with name of priority
        :param list_of_rows: (list) you want to add more data to
        :return: (list) of dictionary rows
        """
        row = {"Task": task.strip(), "Priority": priority.strip()}
        list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """Removes data from a list of dictionary rows

        :param task: (string) with name of task
        :param list_of_rows: (list) you want filled with file data
        :return: (list) of dictionary rows
        """
        list_of_rows = [row for row in list_of_rows if row["Task"] != task]
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file
        :param list_of_rows: (list) you want filled with file data
        :return: nothing
        """
        with open(file_name, "w") as file:
            for row in list_of_rows:
                file.write(row["Task"] + ", " + row["Priority"] + "\n")


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Performs Input and Output tasks"""

    @staticmethod
    def display_menu():
        """Displays a menu of choices to the user"""
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')

    @staticmethod
    def get_menu_choice():
        """Gets the menu choice from the user

        :return: string
        """
        choice = input("Which option would you like to perform? [1 to 4]: ").strip()
        return choice

    @staticmethod
    def display_tasks(list_of_rows):
        """Displays the current tasks in the list of dictionaries

        :param list_of_rows: (list) of rows you want to display
        """
        print("******* The current tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")

    @staticmethod
    def get_new_task_and_priority():
        """Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        task = input("Enter the task: ")
        priority = input("Enter the priority: ")
        return task, priority

    @staticmethod
    def get_task_to_remove():
        """Gets the task name to be removed from the list

        :return: (string) with task
        """
        task = input("Enter the task to remove: ")
        return task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
table_lst = Processor.read_data_from_file(file_name_str)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 - Show current data
    IO.display_tasks(list_of_rows=table_lst)  # Show current data in the list/table
    IO.display_menu()  # Shows menu
    choice_str = IO.get_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str == '1':  # Add a new Task
        task, priority = IO.get_new_task_and_priority()
        table_lst = Processor.add_data_to_list(task=task, priority=priority, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        task = IO.get_task_to_remove()
        table_lst = Processor.remove_data_from_list(task=task, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        Processor.write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
        print("Data Saved!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop

