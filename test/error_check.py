def error_check(m, main_input):
    if m == '1':
        # gre score must be between 0 and 340
        if int(main_input) >= 0 and int(main_input) <= 340:
            return True
        else:
            return False
    elif m == '2':
        # toefl score must be between 0 and 120
        if int(main_input) >= 0 and int(main_input) <= 120:
            return True
        else:
            return False
    elif m == '3':
        # cgpa must be between 0 and 10
        if float(main_input) >= 0 and float(main_input) <= 10.0000:
            return True
        else:
            return False
    elif m == '4':
        # research experience must be yes/no/y/n
        main_input = main_input.lower()
        if main_input == 'yes' or main_input == 'y' or main_input == 'no' or main_input == 'n':
            return True
        else:
            return False
    else:
        return False