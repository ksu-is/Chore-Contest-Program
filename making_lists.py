chore_list = ["litterboxes", "trash", "dust"]
name_list = ["Bob", "Sally"]

             
first_list = []
first_chore_count = 0

for chore in chore_list:
    print("How many times did", name_list[0], "do", chore, "?")
    chore = chore.capitalize()+":"
    first_list.append(chore)
    chore_num = input()
    counting = int(chore_num)
    first_chore_count += counting
    chore_num = str(counting)
    first_list.append(chore_num)
    
    
print("\n"+name_list[0]+"'s chores completed:\n")

print("\n".join(first_list))
print("\nTotal chore count for ", name_list[0], "is:", first_chore_count)

