names = ["Bob", "Anne", "Sally"]

chores = ["litterboxes", "trash", "dust"]

chore_num = len(chores)

def chore_counter():
    name_loc = 0
    chore_loc = 0
    print(names[name_loc], "chores completed: ")
    while True:
        if chore_loc < chore_num:
            print("How many times did ", names[name_loc], "do ", chores[chore_loc], "?")
            comp = input()
            if comp.isnumeric():
                print(names[name_loc], "completed ", chores[chore_loc], comp, "times.")
                chore_loc+=1
            else:
                print("please type a number")
                comp = input()
        else:
            break

chore_counter()

