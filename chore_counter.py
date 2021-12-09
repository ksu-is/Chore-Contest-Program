name_list = []
def two_cont():
        one_name = input("Name of 1st contestant: ")
        name_list.append(one_name)
        two_name = input("Name of 2nd contestant: ")
        name_list.append(two_name)
        print("Contestants in this chore contest are: \n", one_name, "\n", two_name)

def three_cont():
        one_name = input("Name of 1st contestant: ")
        name_list.append(one_name)
        two_name = input("Name of 2nd contestant: ")
        name_list.append(two_name)
        three_name = input("Name of 3rd contestant: ")
        name_list.append(three_name)
        print("Contestants in this chore contest are: \n", one_name, "\n", two_name, "\n", three_name)

def four_cont():
        one_name = input("Name of 1st contestant: ")
        name_list.append(one_name)
        two_name = input("Name of 2nd contestant: ")
        name_list.append(two_name)
        three_name = input("Name of 3rd contestant: ")
        name_list.append(three_name)
        four_name = input("Name of 4th contestant: ")
        name_list.append(four_name)
        print("Contestants in this chore contest are: \n", one_name, "\n", two_name, "\n", three_name, "\n", four_name)

def five_cont():
        one_name = input("Name of 1st contestant: ")
        name_list.append(one_name)
        two_name = input("Name of 2nd contestant: ")
        name_list.append(two_name)
        three_name = input("Name of 3rd contestant: ")
        name_list.append(three_name)
        four_name = input("Name of 4th contestant: ")
        name_list.append(four_name)
        five_name = input("Name of 5th contestant: ")
        name_list.append(five_name)
        print("Contestants in this chore contest are: \n", one_name, "\n", two_name, "\n", three_name, "\n", four_name, "\n", five_name)
        
def num_names():
        name_count = input("How many contestants are in this contest? Choose a number between 2 and 5. ")
        if name_count.isdigit():
                name_amount = int(name_count)
                if name_amount<6:
                        if name_amount<2:
                                print("Sorry, there are not enough people for this contest.")
                                num_names()
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

chore_list = []
        
def one_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        print("The chores in the contest is:\n", chore_one, "\n")

def two_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n")

def three_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n")
        
def four_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n")
        
def five_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n")
        
def six_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        chore_six = input("6th chore in the contest: ")
        chore_list.append(chore_six)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n", chore_six, "\n")
        
def seven_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        chore_six = input("6th chore in the contest: ")
        chore_list.append(chore_six)
        chore_seven = input("7th chore in the contest: ")
        chore_list.append(chore_seven)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n", chore_six, "\n", chore_seven, "\n")
        
def eight_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        chore_six = input("6th chore in the contest: ")
        chore_list.append(chore_six)
        chore_seven = input("7th chore in the contest: ")
        chore_list.append(chore_seven)
        chore_eight = input("8th chore in the contest: ")
        chore_list.append(chore_eight)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n", chore_six, "\n", chore_seven, "\n", chore_eight, "\n")
        
def nine_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        chore_six = input("6th chore in the contest: ")
        chore_list.append(chore_six)
        chore_seven = input("7th chore in the contest: ")
        chore_list.append(chore_seven)
        chore_eight = input("8th chore in the contest: ")
        chore_list.append(chore_eight)
        chore_nine = input("9th chore in the contest: ")
        chore_list.append(chore_nine)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n", chore_six, "\n", chore_seven, "\n", chore_eight, "\n", chore_nine, "\n")
        
def ten_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        chore_six = input("6th chore in the contest: ")
        chore_list.append(chore_six)
        chore_seven = input("7th chore in the contest: ")
        chore_list.append(chore_seven)
        chore_eight = input("8th chore in the contest: ")
        chore_list.append(chore_eight)
        chore_nine = input("9th chore in the contest: ")
        chore_list.append(chore_nine)
        chore_ten = input("10th chore in the contest: ")
        chore_list.append(chore_ten)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n", chore_six, "\n", chore_seven, "\n", chore_eight, "\n", chore_nine, "\n", chore_ten, "\n")
        
def eleven_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        chore_six = input("6th chore in the contest: ")
        chore_list.append(chore_six)
        chore_seven = input("7th chore in the contest: ")
        chore_list.append(chore_seven)
        chore_eight = input("8th chore in the contest: ")
        chore_list.append(chore_eight)
        chore_nine = input("9th chore in the contest: ")
        chore_list.append(chore_nine)
        chore_ten = input("10th chore in the contest: ")
        chore_list.append(chore_ten)
        chore_eleven = input("11th chore in the contest: ")
        chore_list.append(chore_eleven)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n", chore_six, "\n", chore_seven, "\n", chore_eight, "\n", chore_nine, "\n", chore_ten, "\n", chore_eleven, "\n")
        
def twelve_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        chore_six = input("6th chore in the contest: ")
        chore_list.append(chore_six)
        chore_seven = input("7th chore in the contest: ")
        chore_list.append(chore_seven)
        chore_eight = input("8th chore in the contest: ")
        chore_list.append(chore_eight)
        chore_nine = input("9th chore in the contest: ")
        chore_list.append(chore_nine)
        chore_ten = input("10th chore in the contest: ")
        chore_list.append(chore_ten)
        chore_eleven = input("11th chore in the contest: ")
        chore_list.append(chore_eleven)
        chore_twelve = input("12th chore in the contest: ")
        chore_list.append(chore_twelve)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n", chore_six, "\n", chore_seven, "\n", chore_eight, "\n", chore_nine, "\n", chore_ten, "\n", chore_eleven, "\n", chore_twelve, "\n")
        
def thirteen_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        chore_six = input("6th chore in the contest: ")
        chore_list.append(chore_six)
        chore_seven = input("7th chore in the contest: ")
        chore_list.append(chore_seven)
        chore_eight = input("8th chore in the contest: ")
        chore_list.append(chore_eight)
        chore_nine = input("9th chore in the contest: ")
        chore_list.append(chore_nine)
        chore_ten = input("10th chore in the contest: ")
        chore_list.append(chore_ten)
        chore_eleven = input("11th chore in the contest: ")
        chore_list.append(chore_eleven)
        chore_twelve = input("12th chore in the contest: ")
        chore_list.append(chore_twelve)
        chore_thirteen = input("13th chore in the contest: ")
        chore_list.append(chore_thirteen)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n", chore_six, "\n", chore_seven, "\n", chore_eight, "\n", chore_nine, "\n", chore_ten, "\n", chore_eleven, "\n", chore_twelve, "\n", chore_thirteen, "\n")
        
def fourteen_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        chore_six = input("6th chore in the contest: ")
        chore_list.append(chore_six)
        chore_seven = input("7th chore in the contest: ")
        chore_list.append(chore_seven)
        chore_eight = input("8th chore in the contest: ")
        chore_list.append(chore_eight)
        chore_nine = input("9th chore in the contest: ")
        chore_list.append(chore_nine)
        chore_ten = input("10th chore in the contest: ")
        chore_list.append(chore_ten)
        chore_eleven = input("11th chore in the contest: ")
        chore_list.append(chore_eleven)
        chore_twelve = input("12th chore in the contest: ")
        chore_list.append(chore_twelve)
        chore_thirteen = input("13th chore in the contest: ")
        chore_list.append(chore_thirteen)
        chore_fourteen = input("14th chore in the contest: ")
        chore_list.append(chore_fourteen)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n", chore_six, "\n", chore_seven, "\n", chore_eight, "\n", chore_nine, "\n", chore_ten, "\n", chore_eleven, "\n", chore_twelve, "\n", chore_thirteen, "\n", chore_fourteen, "\n")
        
def fifteen_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        chore_six = input("6th chore in the contest: ")
        chore_list.append(chore_six)
        chore_seven = input("7th chore in the contest: ")
        chore_list.append(chore_seven)
        chore_eight = input("8th chore in the contest: ")
        chore_list.append(chore_eight)
        chore_nine = input("9th chore in the contest: ")
        chore_list.append(chore_nine)
        chore_ten = input("10th chore in the contest: ")
        chore_list.append(chore_ten)
        chore_eleven = input("11th chore in the contest: ")
        chore_list.append(chore_eleven)
        chore_twelve = input("12th chore in the contest: ")
        chore_list.append(chore_twelve)
        chore_thirteen = input("13th chore in the contest: ")
        chore_list.append(chore_thirteen)
        chore_fourteen = input("14th chore in the contest: ")
        chore_list.append(chore_fourteen)
        chore_fifteen = input("15th chore in the contest: ")
        chore_list.append(chore_fifteen)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n", chore_six, "\n", chore_seven, "\n", chore_eight, "\n", chore_nine, "\n", chore_ten, "\n", chore_eleven, "\n", chore_twelve, "\n", chore_thirteen, "\n", chore_fourteen, "\n", chore_fifteen, "\n")
        
def sixteen_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        chore_six = input("6th chore in the contest: ")
        chore_list.append(chore_six)
        chore_seven = input("7th chore in the contest: ")
        chore_list.append(chore_seven)
        chore_eight = input("8th chore in the contest: ")
        chore_list.append(chore_eight)
        chore_nine = input("9th chore in the contest: ")
        chore_list.append(chore_nine)
        chore_ten = input("10th chore in the contest: ")
        chore_list.append(chore_ten)
        chore_eleven = input("11th chore in the contest: ")
        chore_list.append(chore_eleven)
        chore_twelve = input("12th chore in the contest: ")
        chore_list.append(chore_twelve)
        chore_thirteen = input("13th chore in the contest: ")
        chore_list.append(chore_thirteen)
        chore_fourteen = input("14th chore in the contest: ")
        chore_list.append(chore_fourteen)
        chore_fifteen = input("15th chore in the contest: ")
        chore_list.append(chore_fifteen)
        chore_sixteen = input("16th chore in the contest: ")
        chore_list.append(chore_sixteen)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n", chore_six, "\n", chore_seven, "\n", chore_eight, "\n", chore_nine, "\n", chore_ten, "\n", chore_eleven, "\n", chore_twelve, "\n", chore_thirteen, "\n", chore_fourteen, "\n", chore_fifteen, "\n", chore_sixteen, "\n")
        
def seventeen_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        chore_six = input("6th chore in the contest: ")
        chore_list.append(chore_six)
        chore_seven = input("7th chore in the contest: ")
        chore_list.append(chore_seven)
        chore_eight = input("8th chore in the contest: ")
        chore_list.append(chore_eight)
        chore_nine = input("9th chore in the contest: ")
        chore_list.append(chore_nine)
        chore_ten = input("10th chore in the contest: ")
        chore_list.append(chore_ten)
        chore_eleven = input("11th chore in the contest: ")
        chore_list.append(chore_eleven)
        chore_twelve = input("12th chore in the contest: ")
        chore_list.append(chore_twelve)
        chore_thirteen = input("13th chore in the contest: ")
        chore_list.append(chore_thirteen)
        chore_fourteen = input("14th chore in the contest: ")
        chore_list.append(chore_fourteen)
        chore_fifteen = input("15th chore in the contest: ")
        chore_list.append(chore_fifteen)
        chore_sixteen = input("16th chore in the contest: ")
        chore_list.append(chore_sixteen)
        chore_seventeen = input("17th chore in the contest: ")
        chore_list.append(chore_seventeen)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n", chore_six, "\n", chore_seven, "\n", chore_eight, "\n", chore_nine, "\n", chore_ten, "\n", chore_eleven, "\n", chore_twelve, "\n", chore_thirteen, "\n", chore_fourteen, "\n", chore_fifteen, "\n", chore_sixteen, "\n", chore_seventeen, "\n")
        
def eighteen_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        chore_six = input("6th chore in the contest: ")
        chore_list.append(chore_six)
        chore_seven = input("7th chore in the contest: ")
        chore_list.append(chore_seven)
        chore_eight = input("8th chore in the contest: ")
        chore_list.append(chore_eight)
        chore_nine = input("9th chore in the contest: ")
        chore_list.append(chore_nine)
        chore_ten = input("10th chore in the contest: ")
        chore_list.append(chore_ten)
        chore_eleven = input("11th chore in the contest: ")
        chore_list.append(chore_eleven)
        chore_twelve = input("12th chore in the contest: ")
        chore_list.append(chore_twelve)
        chore_thirteen = input("13th chore in the contest: ")
        chore_list.append(chore_thirteen)
        chore_fourteen = input("14th chore in the contest: ")
        chore_list.append(chore_fourteen)
        chore_fifteen = input("15th chore in the contest: ")
        chore_list.append(chore_fifteen)
        chore_sixteen = input("16th chore in the contest: ")
        chore_list.append(chore_sixteen)
        chore_seventeen = input("17th chore in the contest: ")
        chore_list.append(chore_seventeen)
        chore_eighteen = input("18th chore in the contest: ")
        chore_list.append(chore_eighteen)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n", chore_six, "\n", chore_seven, "\n", chore_eight, "\n", chore_nine, "\n", chore_ten, "\n", chore_eleven, "\n", chore_twelve, "\n", chore_thirteen, "\n", chore_fourteen, "\n", chore_fifteen, "\n", chore_sixteen, "\n", chore_seventeen, "\n", chore_eighteen, "\n")
        
def nineteen_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        chore_six = input("6th chore in the contest: ")
        chore_list.append(chore_six)
        chore_seven = input("7th chore in the contest: ")
        chore_list.append(chore_seven)
        chore_eight = input("8th chore in the contest: ")
        chore_list.append(chore_eight)
        chore_nine = input("9th chore in the contest: ")
        chore_list.append(chore_nine)
        chore_ten = input("10th chore in the contest: ")
        chore_list.append(chore_ten)
        chore_eleven = input("11th chore in the contest: ")
        chore_list.append(chore_eleven)
        chore_twelve = input("12th chore in the contest: ")
        chore_list.append(chore_twelve)
        chore_thirteen = input("13th chore in the contest: ")
        chore_list.append(chore_thirteen)
        chore_fourteen = input("14th chore in the contest: ")
        chore_list.append(chore_fourteen)
        chore_fifteen = input("15th chore in the contest: ")
        chore_list.append(chore_fifteen)
        chore_sixteen = input("16th chore in the contest: ")
        chore_list.append(chore_sixteen)
        chore_seventeen = input("17th chore in the contest: ")
        chore_list.append(chore_seventeen)
        chore_eighteen = input("18th chore in the contest: ")
        chore_list.append(chore_eighteen)
        chore_nineteen = input("19th chore in the contest: ")
        chore_list.append(chore_nineteen)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n", chore_six, "\n", chore_seven, "\n", chore_eight, "\n", chore_nine, "\n", chore_ten, "\n", chore_eleven, "\n", chore_twelve, "\n", chore_thirteen, "\n", chore_fourteen, "\n", chore_fifteen, "\n", chore_sixteen, "\n", chore_seventeen, "\n", chore_eighteen, "\n", chore_ninteen, "\n")
        
def twenty_chore():
        chore_one = input("1st chore in the contest: ")
        chore_list.append(chore_one)
        chore_two = input("2nd chore in the contest: ")
        chore_list.append(chore_two)
        chore_three = input("3rd chore in the contest: ")
        chore_list.append(chore_three)
        chore_four = input("4th chore in the contest: ")
        chore_list.append(chore_four)
        chore_five = input("5th chore in the contest: ")
        chore_list.append(chore_five)
        chore_six = input("6th chore in the contest: ")
        chore_list.append(chore_six)
        chore_seven = input("7th chore in the contest: ")
        chore_list.append(chore_seven)
        chore_eight = input("8th chore in the contest: ")
        chore_list.append(chore_eight)
        chore_nine = input("9th chore in the contest: ")
        chore_list.append(chore_nine)
        chore_ten = input("10th chore in the contest: ")
        chore_list.append(chore_ten)
        chore_eleven = input("11th chore in the contest: ")
        chore_list.append(chore_eleven)
        chore_twelve = input("12th chore in the contest: ")
        chore_list.append(chore_twelve)
        chore_thirteen = input("13th chore in the contest: ")
        chore_list.append(chore_thirteen)
        chore_fourteen = input("14th chore in the contest: ")
        chore_list.append(chore_fourteen)
        chore_fifteen = input("15th chore in the contest: ")
        chore_list.append(chore_fifteen)
        chore_sixteen = input("16th chore in the contest: ")
        chore_list.append(chore_sixteen)
        chore_seventeen = input("17th chore in the contest: ")
        chore_list.append(chore_seventeen)
        chore_eighteen = input("18th chore in the contest: ")
        chore_list.append(chore_eighteen)
        chore_nineteen = input("19th chore in the contest: ")
        chore_list.append(chore_nineteen)
        chore_twenty = input("20th chore in the contest: ")
        chore_list.append(chore_twenty)
        print("The chores in the contest are:\n", chore_one, "\n", chore_two, "\n", chore_three, "\n", chore_four, "\n", chore_five, "\n", chore_six, "\n", chore_seven, "\n", chore_eight, "\n", chore_nine, "\n", chore_ten, "\n", chore_eleven, "\n", chore_twelve, "\n", chore_thirteen, "\n", chore_fourteen, "\n", chore_fifteen, "\n", chore_sixteen, "\n", chore_seventeen, "\n", chore_eighteen, "\n", chore_ninteen, "\n", chore_twenty, "\n")

def chore_num():
        num_of_chores = input("How many chores are in the contest? The maximum allowed in the contest is 20. ")
        if num_of_chores.isnumeric():
                num_chores = int(num_of_chores)
                if num_chores == 1:
                        one_chore()
                elif num_chores == 2:
                        two_chore()
                elif num_chores == 3:
                        three_chore()
                elif num_chores == 4:
                        four_chore()
                elif num_chores == 5:
                        five_chore()
                elif num_chores == 6:
                        six_chore()
                elif num_chores == 7:
                        seven_chore()
                elif num_chores == 8:
                        eight_chore()
                elif num_chores == 9:
                        nine_chore()
                elif num_chores == 10:
                        ten_chore()
                elif num_chores == 11:
                        eleven_chore()
                elif num_chores == 12:
                        twelve_chore()
                elif num_chores == 13:
                        thirteen_chore()
                elif num_chores == 14:
                        fourteen_chore()
                elif num_chores == 15:
                        fifteen_chore()
                elif num_chores == 16:
                        sixteen_chore()
                elif num_chores == 17:
                        seventeen_chore()
                elif num_chores == 18:
                        eighteen_chore()
                elif num_chores == 19:
                        nineteen_chore()
                elif num_chores == 20:
                        twenty_chore()
                elif num_chores > 20:
                        print("Too many chores. Please elimate some or run more than one contest.\n")
                        chore_num()
                else:
                        print("Invalid input. Please try again.\n")
                        chore_num()
        else:
                print("Invalid input. Please try again.\n")
                chore_num()


chore_num()

def two_count():
    first_list = []
    first_chore_count = 0
    print("\n"+name_list[0]+"'s chores...\n")
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
    second_list = []
    second_chore_count = 0
    print("\n"+name_list[1]+"'s chores...\n")
    for chore in chore_list:
        print("How many times did", name_list[1], "do", chore, "?")
        chore = chore.capitalize()+":"
        second_list.append(chore)
        chore_num = input()
        counting = int(chore_num)
        second_chore_count += counting
        chore_num = str(counting)
        second_list.append(chore_num)   
    print("\n"+name_list[1]+"'s chores completed:\n")
    print("\n".join(second_list))
    print("\nTotal chore count for ", name_list[1], "is:", second_chore_count)

def three_count():
    first_list = []
    first_chore_count = 0
    print("\n"+name_list[0]+"'s chores...\n")
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
    second_list = []
    second_chore_count = 0
    print("\n"+name_list[1]+"'s chores...\n")
    for chore in chore_list:
        print("How many times did", name_list[1], "do", chore, "?")
        chore = chore.capitalize()+":"
        second_list.append(chore)
        chore_num = input()
        counting = int(chore_num)
        second_chore_count += counting
        chore_num = str(counting)
        second_list.append(chore_num)   
    print("\n"+name_list[1]+"'s chores completed:\n")
    print("\n".join(second_list))
    print("\nTotal chore count for ", name_list[1], "is:", second_chore_count)
    third_list = []
    third_chore_count = 0
    print("\n"+name_list[2]+"'s chores...\n")
    for chore in chore_list:
        print("How many times did", name_list[2], "do", chore, "?")
        chore = chore.capitalize()+":"
        third_list.append(chore)
        chore_num = input()
        counting = int(chore_num)
        third_chore_count += counting
        chore_num = str(counting)
        third_list.append(chore_num)   
    print("\n"+name_list[2]+"'s chores completed:\n")
    print("\n".join(third_list))

def four_count():
    first_list = []
    first_chore_count = 0
    print("\n"+name_list[0]+"'s chores...\n")
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
    second_list = []
    second_chore_count = 0
    print("\n"+name_list[1]+"'s chores...\n")
    for chore in chore_list:
        print("How many times did", name_list[1], "do", chore, "?")
        chore = chore.capitalize()+":"
        second_list.append(chore)
        chore_num = input()
        counting = int(chore_num)
        second_chore_count += counting
        chore_num = str(counting)
        second_list.append(chore_num)   
    print("\n"+name_list[1]+"'s chores completed:\n")
    print("\n".join(second_list))
    print("\nTotal chore count for ", name_list[1], "is:", second_chore_count)
    third_list = []
    third_chore_count = 0
    print("\n"+name_list[2]+"'s chores...\n")
    for chore in chore_list:
        print("How many times did", name_list[2], "do", chore, "?")
        chore = chore.capitalize()+":"
        third_list.append(chore)
        chore_num = input()
        counting = int(chore_num)
        third_chore_count += counting
        chore_num = str(counting)
        third_list.append(chore_num)   
    print("\n"+name_list[2]+"'s chores completed:\n")
    print("\n".join(third_list))
    print("\nTotal chore count for ", name_list[2], "is:", third_chore_count)
    fourth_list = []
    fourth_chore_count = 0
    print("\n"+name_list[3]+"'s chores...\n")
    for chore in chore_list:
        print("How many times did", name_list[3], "do", chore, "?")
        chore = chore.capitalize()+":"
        fourth_list.append(chore)
        chore_num = input()
        counting = int(chore_num)
        fourth_chore_count += counting
        chore_num = str(counting)
        fourth_list.append(chore_num)   
    print("\n"+name_list[3]+"'s chores completed:\n")
    print("\n".join(fourth_list))
    print("\nTotal chore count for ", name_list[3], "is:", fourth_chore_count)

def five_count():
    first_list = []
    first_chore_count = 0
    print("\n"+name_list[0]+"'s chores...\n")
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
    second_list = []
    second_chore_count = 0
    print("\n"+name_list[1]+"'s chores...\n")
    for chore in chore_list:
        print("How many times did", name_list[1], "do", chore, "?")
        chore = chore.capitalize()+":"
        second_list.append(chore)
        chore_num = input()
        counting = int(chore_num)
        second_chore_count += counting
        chore_num = str(counting)
        second_list.append(chore_num)   
    print("\n"+name_list[1]+"'s chores completed:\n")
    print("\n".join(second_list))
    print("\nTotal chore count for ", name_list[1], "is:", second_chore_count)
    third_list = []
    third_chore_count = 0
    print("\n"+name_list[2]+"'s chores...\n")
    for chore in chore_list:
        print("How many times did", name_list[2], "do", chore, "?")
        chore = chore.capitalize()+":"
        third_list.append(chore)
        chore_num = input()
        counting = int(chore_num)
        third_chore_count += counting
        chore_num = str(counting)
        third_list.append(chore_num)   
    print("\n"+name_list[2]+"'s chores completed:\n")
    print("\n".join(third_list))
    print("\nTotal chore count for ", name_list[2], "is:", third_chore_count)
    fourth_list = []
    fourth_chore_count = 0
    print("\n"+name_list[3]+"'s chores...\n")
    for chore in chore_list:
        print("How many times did", name_list[3], "do", chore, "?")
        chore = chore.capitalize()+":"
        fourth_list.append(chore)
        chore_num = input()
        counting = int(chore_num)
        fourth_chore_count += counting
        chore_num = str(counting)
        fourth_list.append(chore_num)   
    print("\n"+name_list[3]+"'s chores completed:\n")
    print("\n".join(fourth_list))
    print("\nTotal chore count for ", name_list[3], "is:", fourth_chore_count)
    fifth_list = []
    fifth_chore_count = 0
    print("\n"+name_list[4]+"'s chores...\n")
    for chore in chore_list:
        print("How many times did", name_list[4], "do", chore, "?")
        chore = chore.capitalize()+":"
        fifth_list.append(chore)
        chore_num = input()
        counting = int(chore_num)
        fifth_chore_count += counting
        chore_num = str(counting)
        fifth_list.append(chore_num)   
    print("\n"+name_list[4]+"'s chores completed:\n")
    print("\n".join(fifth_list))
    print("\nTotal chore count for ", name_list[4], "is:", fifth_chore_count)

def chore_counter():
        if len(name_list) == 2:
                two_count()
        if len(name_list) == 3:
                three_count()
        if len(name_list) == 4:
                four_count()
        if len(name_list) == 5:
                five_count()

chore_counter()
