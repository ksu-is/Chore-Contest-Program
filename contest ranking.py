

def contest_ranking():
    first_place = ""
    second_place = ""
    third_place = ""
    fourth_place = ""
    fifth_place = ""
    if first_chore_count > second_chore_count:
        if first_chore_count > third_chore_count:
            if first_chore_count> fourth_chore_count:
                if first_chore_count > fifth_chore_count:
                    first_place = name_list[0]
                else:
                    second_place = name_list[0]
            else:
                if first_chore_count > fifth_chore_count:
                    second_place = name_list[0]
                else:
                    third_place = name_list[0]
        else:
            if first_chore_count> fourth_chore_count:
                if first_chore_count > fifth_chore_count:
                    second_place = name_list[0]
                else:
                    third_place = name_list[0]
            else:
                if first_chore_count > fifth_chore_count:
                    third_place = name_list[0]
                else:
                    fourth_place = name_list[0]
    elif first_chore_count > third_chore_count:
        if first_chore_count > fourth_chore_count:
            if first_chore_count > fifth_chore_count:
                second_place = name_list[0]
            else:
                third_place = name_list[0]
        else:
            if first_chore_count > fifth_chore_count:
                third_place = name_list[0]
            else:
                fourth_place = name_list[0]
    elif first_chore_count > fourth_chore_count:
        if first_chore_count > fifth_chore_count:
            third_place = name_list[0]
        else:
            fourth_place = name_list[0]
    elif first_chore_count > fifth_chore_count:
        fourth_place = name_list[0]
    else:
        fifth_place = name_list[0]

    if second_chore_count > first_chore_count:
        if second_chore_count > third_chore_count:
            if second_chore_count> fourth_chore_count:
                if second_chore_count > fifth_chore_count:
                    first_place = name_list[1]
                else:
                    second_place = name_list[1]
            else:
                if second_chore_count > fifth_chore_count:
                    second_place = name_list[1]
                else:
                    third_place = name_list[1]
        else:
            if second_chore_count> fourth_chore_count:
                if second_chore_count > fifth_chore_count:
                    second_place = name_list[1]
                else:
                    second_place = name_list[1]
            else:
                if second_chore_count > fifth_chore_count:
                    third_place = name_list[1]
                else:
                    fourth_place = name_list[1]
    elif second_chore_count > third_chore_count:
        if second_chore_count > fourth_chore_count:
            if second_chore_count > fifth_chore_count:
                second_place = name_list[1]
            else:
                third_place = name_list[1]
        else:
            if second_chore_count > fifth_chore_count:
                third_place = name_list[1]
            else:
                fourth_place = name_list[1]
    elif second_chore_count > fourth_chore_count:
        if second_chore_count > fifth_chore_count:
            third_place = name_list[1]
        else:
            fourth_place = name_list[1]
    elif second_chore_count > fifth_chore_count:
        fourth_place = name_list[1]
    else:
        fifth_place = name_list[1]

    if third_chore_count > first_chore_count:
        if third_chore_count > second_chore_count:
            if third_chore_count> fourth_chore_count:
                if third_chore_count > fifth_chore_count:
                    first_place = name_list[2]
                else:
                    second_place = name_list[2]
            else:
                if third_chore_count > fifth_chore_count:
                    second_place = name_list[2]
                else:
                    third_place = name_list[2]
        else:
            if third_chore_count> fourth_chore_count:
                if third_chore_count > fifth_chore_count:
                    second_place = name_list[2]
                else:
                    second_place = name_list[2]
            else:
                if third_chore_count > fifth_chore_count:
                    third_place = name_list[2]
                else:
                    fourth_place = name_list[2]
    elif third_chore_count > second_chore_count:
        if third_chore_count > fourth_chore_count:
            if third_chore_count > fifth_chore_count:
                second_place = name_list[2]
            else:
                third_place = name_list[2]
        else:
            if third_chore_count > fifth_chore_count:
                third_place = name_list[2]
            else:
                fourth_place = name_list[2]
    elif third_chore_count > fourth_chore_count:
        if third_chore_count > fifth_chore_count:
            third_place = name_list[2]
        else:
            fourth_place = name_list[2]
    elif third_chore_count > fifth_chore_count:
        fourth_place = name_list[2]
    else:
        fifth_place = name_list[2]

    if fourth_chore_count > first_chore_count:
        if fourth_chore_count > second_chore_count:
            if fourth_chore_count> third_chore_count:
                if fourth_chore_count > fifth_chore_count:
                    first_place = name_list[3]
                else:
                    second_place = name_list[3]
            else:
                if fourth_chore_count > fifth_chore_count:
                    second_place = name_list[3]
                else:
                    third_place = name_list[3]
        else:
            if fourth_chore_count> third_chore_count:
                if fourth_chore_count > fifth_chore_count:
                    second_place = name_list[3]
                else:
                    second_place = name_list[3]
            else:
                if fourth_chore_count > fifth_chore_count:
                    third_place = name_list[3]
                else:
                    fourth_place = name_list[3]
    elif fourth_chore_count > second_chore_count:
        if fourth_chore_count > third_chore_count:
            if fourth_chore_count > fifth_chore_count:
                second_place = name_list[3]
            else:
                third_place = name_list[3]
        else:
            if fourth_chore_count > fifth_chore_count:
                third_place = name_list[3]
            else:
                fourth_place = name_list[3]
    elif fourth_chore_count > third_chore_count:
        if fourth_chore_count > fifth_chore_count:
            third_place = name_list[3]
        else:
            fourth_place = name_list[3]
    elif fourth_chore_count > fifth_chore_count:
        fourth_place = name_list[3]
    else:
        fifth_place = name_list[3]

    if fifth_chore_count > first_chore_count:
        if fifth_chore_count > second_chore_count:
            if fifth_chore_count> third_chore_count:
                if fifth_chore_count > fourth_chore_count:
                    first_place = name_list[4]
                else:
                    second_place = name_list[4]
            else:
                if fifth_chore_count > fourth_chore_count:
                    second_place = name_list[4]
                else:
                    third_place = name_list[4]
        else:
            if fifth_chore_count> third_chore_count:
                if fifth_chore_count > fourth_chore_count:
                    second_place = name_list[4]
                else:
                    second_place = name_list[4]
            else:
                if fifth_chore_count > fourth_chore_count:
                    third_place = name_list[4]
                else:
                    fourth_place = name_list[4]
    elif fifth_chore_count > second_chore_count:
        if fifth_chore_count > third_chore_count:
            if fifth_chore_count > fourth_chore_count:
                second_place = name_list[4]
            else:
                third_place = name_list[4]
        else:
            if fifth_chore_count > fourth_chore_count:
                third_place = name_list[4]
            else:
                fourth_place = name_list[4]
    elif fifth_chore_count > third_chore_count:
        if fifth_chore_count > fourth_chore_count:
            third_place = name_list[4]
        else:
            fourth_place = name_list[4]
    elif fifth_chore_count > fourth_chore_count:
        fourth_place = name_list[4]
    else:
        fifth_place = name_list[4]
        
    print("First place is:", first_place, "\nSecond place is:", second_place, "\nThird place is:", third_place, "\nFourth place is:", fourth_place, "\nFifth place is:", fifth_place)

contest_ranking()

