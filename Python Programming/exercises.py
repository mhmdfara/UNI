#!/usr/bin/python
task_index = 0
what_to_do = []

while True:
    print("\nMenu:" , "\n1.Add a Task","\n2.View Tasks", "\n3.Delete a Task", "\n4.Exit")

    Select = input("Select (1/2/3/4): ")

    if Select == '1':
        Do = input("Add a Task: ")
        what_to_do.append(Do)
        task_index += 1
        print(f"Task '{Do}' added!")
    elif Select == '2':
        if not what_to_do:
            print("Nothing Exist.")
        else:
            print("Task List:")
            for i in range(len(what_to_do)):
                print(f"{i + 1}. {what_to_do[i]}")
    elif Select == '3':
        if not what_to_do:
            print("Nothing Exist.")
        else:
            print("Task List:")
            for i in range(len(what_to_do)):
                print(f"{i + 1}. {what_to_do[i]}")
            try:
                task_index = int(input("Enter number to remove: ")) - 1
                if 0 <= task_index < len(what_to_do):
                    deleted_task = what_to_do.pop(task_index)
                    print(f"Task '{deleted_task}' deleted!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid. Please enter a valid number.")
    elif Select == '4':
        print("Exiting...")
        break
    else:
        print("Invalid. Please select a valid number (1/2/3/4).")

