def error_check(m, main_input):
    #err_msg = ''
    try:
        if m == '1':
            # gre score must be between 0 and 340
            if int(main_input) >= 0 and int(main_input) <= 340:
                return True
            elif int(main_input) == -1:
                return True
            else:
                return False
        elif m == '2':
            # toefl score must be between 0 and 120
            if int(main_input) >= 0 and int(main_input) <= 120:
                return True
            elif int(main_input) == -1:
                return True
            else:
                return False
        elif m == '3':
            # uni rating must be between 0 and 5
            if int(main_input) >= 0 and int(main_input) <= 5:
                return True
            elif int(main_input) == -1:
                return True
            else:
                return False
        elif m == '4':
            # sop must be between 0.00 and 5.00
            if float(main_input) >= 0.00 and float(main_input) <= 5.00:
                return True
            elif int(main_input) == -1:
                return True
            else:
                return False
        elif m == '5':
            # lor must be between 0.00 and 5.00
            if float(main_input) >= 0.00 and float(main_input) <= 5.00:
                return True
            elif int(main_input) == -1:
                return True
            else:
                return False
        elif m == '6':
            # cgpa must be between 0.00 and 10.00
            if float(main_input) >= 0.00 and float(main_input) <= 10.00:
                return True
            elif int(main_input) == -1:
                return True
            else:
                return False
        elif m == '7':
            # res exp must be yes, no, y, n
            if main_input.lower() == 'yes' or main_input.lower() == 'y' or main_input.lower() == 'no' or main_input.lower() == 'n':
                return True
            elif int(main_input) == -1:
                return True
            else:
                return False
        else:
            return False
    except:
        return False
        # print message