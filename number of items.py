def two_cont():
        one_name = input("Name of 1st contestant: ")
        two_name = input("Name of 2nd contestant: ")
        print("Contestants in this chore contest are: \n", one_name, "\n", two_name)

def three_cont():
        one_name = input("Name of 1st contestant: ")
        two_name = input("Name of 2nd contestant: ")
        three_name = input("Name of 3rd contestant: ")
        print("Contestants in this chore contest are: \n", one_name, "\n", two_name, "\n", three_name)

def four_cont():
        one_name = input("Name of 1st contestant: ")
        two_name = input("Name of 2nd contestant: ")
        three_name = input("Name of 3rd contestant: ")
        four_name = input("Name of 4th contestant: ")
        print("Contestants in this chore contest are: \n", one_name, "\n", two_name, "\n", three_name, "\n", four_name)

def five_cont():
        one_name = input("Name of 1st contestant: ")
        two_name = input("Name of 2nd contestant: ")
        three_name = input("Name of 3rd contestant: ")
        four_name = input("Name of 4th contestant: ")
        five_name = input("Name of 5th contestant: ")
        print("Contestants in this chore contest are: \n", one_name, "\n", two_name, "\n", three_name, "\n", four_name, "\n", five_name)
        
def num_names():
        name_count = input("How many contestants are in this contest? Choose a number between 2 and 5. ")
        if name_count.isdigit():
                name_amount = int(name_count)
                if name_amount<6:
                        if name_amount<2:
                                print("Sorry, there are not enough people for this contest.")
                        else:
                                if name_amount==2:
                                        two_cont()
                                elif name_amount==3:
                                        three_cont()
                                elif name_amount==4:
                                        four_cont()
                                else:
                                        five_cont()
                elif name_amount>5:
                        print("Too many contestants. Please break them into smaller groups.\n")
                        num_names()
                else:
                        print("invalid input")
        else:
                print("invalid input. Please type a number such as \"2\" rather than \"two\".\n")
                num_names()
num_names()

        
