def WhatDay():
    '''
        input validation function for the day
        not case-sensitive but user must provide full day name
        returns index related to day    
    '''
    valid = False
    while not valid:
        valid = True
        day = input("What day of the week is it? Type a day from Sunday to Saturday: ")
        if day.lower() == "sunday":
            day_index = 1
        elif day.lower() == "monday":
            day_index = 2
        elif day.lower() == "tuesday":
            day_index = 3
        elif day.lower() == "wednesday":
            day_index = 4
        elif day.lower() == "thursday":
            day_index = 5
        elif day.lower() == "friday":
            day_index = 6
        elif day.lower() == "saturday":
            day_index = 7
        else:
            print("Please enter a valid day.")
            valid = False # reenter loop if not valid

    return day_index