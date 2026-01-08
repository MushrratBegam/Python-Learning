def task():
    tasks = []
    print("----WELCOM TO THE TASK MANAGEMENT----")
    
    total_task = int(input("Enter how many task you want to add ="))
    for i in range(1, total_task+1):
        task_name = input(f"enter task {i} = ")
        tasks.append(task_name)
        print(f"Today's tasks are\n{tasks}")
        
    while True:
        operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/stop/"))
        if operation == 1:
           add = input("Enter task you want to add =")
           tasks.append(add)
           print(f"task {add} has been succesfully added...")
            
        elif operation == 2:
             update_val = input("Enter task you want to update =")
             if update_val in task:
                up = input("Enter new task = ")
                ind = task.index(update_val)
                task [ind] = up
                print(f"update task {up}")
            
        elif operation == 3:
             del_val = input("Enter task you want to deleted =")
             if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"task {del_val} has been deleted...")
                
        elif operation == 4:
               print(f"total tasks = {tasks}")
                
        elif operation == 5:
             print("closing the program...")
             break
                
        else:
            print("Invalid input")
task()
            
            
            