def two_cont():
        one_name = input("Name of contestant: ")
        two_name = input("Name of 2nd contestant: ")
        print("Contestants in this chore contest are: ", one_name, two_name)

def three_cont():
        one_name = input("Name of contestant: ")
        two_name = input("Name of 2nd contestant: ")
        three_name = input("Name of 3rd contestant: ")
        print("Contestants in this chore contest are: ", one_name, two_name, three_name)

def four_cont():
        one_name = input("Name of contestant: ")
        two_name = input("Name of 2nd contestant: ")
        three_name = input("Name of 3rd contestant: ")
        four_name = input("Name of 4th contestant: ")
        print("Contestants in this chore contest are: ", one_name, two_name, three_name, four_name)

def five_cont():
        one_name = input("Name of contestant: ")
        two_name = input("Name of 2nd contestant: ")
        three_name = input("Name of 3rd contestant: ")
        four_name = input("Name of 4th contestant: ")
        five_name = input("Name of 5th contestant: ")
        print("Contestants in this chore contest are: ", one_name, two_name, three_name, four_name, five_name)
        
name_amount = input("How many contestants are in this contest? Choose a number between 2 and 5. ")
while name_amount.isnumeric():
	if name_amount<2:
		print("Sorry, there are not enough people for this contest.")
	elif name_amount>5:
                print("There are too many contestants. You will have to divide into smaller groups to play.")
        else:
                if name_amount==2:
                        two_cont()
                elif name_amount==3:
                        three_cont()
                elif name_amount==4:
                        four_cont()
                else:
                        five_count()

        
