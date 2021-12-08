chore_list = ["litterboxes", "trash", "dust"]
name_list = ["Bob", "Sally"]




first_list = []
first_chore_count = 0

for chore in chore_list:
    chore = chore.capitalize()+":"
    first_list.append(chore)
    chore_num = input("enter")
    counting = int(chore_num)
    first_chore_count += counting
    chore_num = str(counting)
    first_list.append(chore_num)
    
    
print(name_list[0]+"'s chores completed:\n")

print("\n".join(first_list))
print("\nTotal chore count for ", name_list[0], "is:\n", first_chore_count)
