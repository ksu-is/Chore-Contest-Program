chores = []

def chore_list():
    chore=input("Chore to add to list of chores: ")
    while len(chore)>1:
        if chore == 0:
            break
        else:
            chores.append(chore)
            chore = input("Chore to add to list of chores: ")


print("Please type chores as prompted until all the chores included in the contest have been added to the list. When done simply type '0'")
chore_list()
print(chores)
