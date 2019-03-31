import sys

school = ''
degree = ''
gre_score = 0
toefl_score = 0
uni_rating = 0
sop_val = 0.0
lor_val = 0.0
cgpa_val = 0.0
res_val = 0
admit_Val = 0.0
schoolSuccess = False
degreeSuccess = False

# user interface
while True:
    print('Choose from the following menu options:')
    print('1 - Select a Graduate School and Program')
    print('2 - Calculate Chance of Admit')
    print('3 - Run GradAdvice')
    print('4 - Exit')

    x = int(raw_input('Enter your choice -> '))
    
    # switch
    if x == 1:
        # select a graduate school
        while True:
            print('Choose from the following graduate schools:')
            print('1 - UCLA')
            for i in range(8):
                print(str(i+2) + ' - [Empty]')
            print('0 - Cancel')

            y = int(raw_input('Enter your choice -> '))
            
            if y == 0:
                # return to the main menu
                break
            elif y == 1:
                schoolSuccess = True
                school = 'UCLA'

                # select a graduate program
                while True:
                    print('Choose from the following graduate programs:')
                    print('1 - Business')
                    print('2 - Engineering')
                    print('3 - Law')
                    print('0 - Cancel')

                    z = int(raw_input('Enter your choice -> '))

                    if z == 0:
                        # return to the graduate school menu
                        break
                    elif z == 1 or z == 2 or z == 3:
                        degreeSuccess = True
                        degree = 'Business/Engineering/Law'
                        break
                    else:
                        print('Invalid choice.\n')
                
                # return to the main menu
                break
            else:
                print('Invalid choice.\n')
    elif x == 2:
        # calculate chance of admit
        # required: degreeSuccess, schoolSuccess = True
        while True:
            print('Choose from the following menu options:')
            print('1 - Enter a Graduate Record Examinations (GRE) Score')
            print('2 - Enter a Test of English as a Foreign Language (TOEFL) Score')
            print('3 - Enter a University Rating')
            print('4 - Enter a Statement of Purpose (SOP)')
            print('5 - Enter a Letter of Recommendation (LOR)')
            print('6 - Enter a Cumulative Grade Point Average (CGPA)')
            print('7 - Enter a Research Experience')
            print('8 - Calculate Chance of Admit')
            print('9 - Print')
            print('0 - Cancel')

            m = int(raw_input('Enter your choice -> '))

            if m == 0:
                # return to the main menu
                break
            elif m == 1:
                # sanitize, error check, print error messages #1 - #7
                gre_score = int(raw_input('Enter a GRE score  '))
            elif m == 2:
                toefl_score = int(raw_input('Enter a TOEFL score  '))
            elif m == 3:
                # evaluate to a numerical value from a text input #3 - #5
                uni_rating = int(raw_input('Enter a University Rating  '))
            elif m == 4:
                sop_val = float(raw_input('Enter a SOP value  '))
            elif m == 5:
                lor_val = float(raw_input('Enter a LOR value  '))
            elif m == 6:
                # similar to #1, #2
                cgpa_val = float(raw_input('Enter a CGPA value  '))
            elif m == 7:
                # convert to 0 (No) and 1 (Yes)
                res_val = int(raw_input('Enter a Research Experience value  '))
            elif m == 8:
                # calculate chance of admit
                # required gre_score, toefl_score, and cgpa_val (success = True)
                print(admit_val)
            elif m == 9:
                print('Currently, the following values have been entered:')
                print('Graduate Record Examination (GRE) Score: ' + str(gre_score))
                print('Test of English as a Foreign Language (TOEFL) Score: '+ str(toefl_score))
                print('University Rating: ' + str(uni_rating))
                print('Statement of Purpose (SOP): ' + str(sop_val))
                print('Letter of Recommendation (LOR): ' + str(lor_val))
                print('Cumulative Grade Point Average (CGPA): ' + str(cgpa_val))
                print('Research Experience: ' + str(res_val))
                print('\n')
            else:
                print('Invalid choice.\n')

    elif x == 4:
        print('Exiting program...')
        sys.exit()
    else:
        print('Invalid choice.\n')