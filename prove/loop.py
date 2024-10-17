to_do_list = []
finish = False
while not finish:
    task = input("enter an object for the to do list: ")
    if len(task)==0:
        finish = True
    else:
        to_do_list.append(task)

print(to_do_list)
