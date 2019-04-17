import csv
import sys
import test

school = ''
degree = ''
gre_score = 0
toefl_score = 0
uni_rating = 0
sop_val = 0.0
lor_val = 0.0
cgpa_val = 0.0
res_val = 0
admit_val = 0.0

cgpa_avg = 8.57644
gre_avg = 316.472
tofel_avg = 107.192
has_rch_avg = 0.5

# user interface
while True:
    print('Choose from the following menu options:')
    print('1 - Select a Graduate School and Program')
    print('2 - Calculate Chance of Admit')
    print('3 - Run GradAdvice')
    print('4 - Exit')

    x = input('Enter your choice -> ')
    
    # switch
    if x == '1':
        # select a graduate school
        while True:
            print('Choose from the following graduate schools:')
            print('1 - UCLA')
            for i in range(8):
                print(str(i+2) + ' - [Empty]')
            print('0 - Cancel')

            y = input('Enter your choice -> ')
            
            if y == '0':
                # return to the main menu
                break
            elif y == '1':
                school = 'UCLA'

                # select a graduate program
                while True:
                    print('Choose from the following graduate programs:')
                    print('1 - Business')
                    print('2 - Engineering')
                    print('3 - Law')
                    print('0 - Cancel')

                    z = input('Enter your choice -> ')

                    if z == '0':
                        # return to the graduate school menu
                        break
                    elif z == '1':
                        degree = 'Business'
                        break
                    elif z == '2':
                        degree = 'Engineering'
                        break
                    elif z == '3':
                        degree = 'Law'
                        break
                    else:
                        print('Invalid choice.\n')
                        input("\nPress Any Key to Continue\n")
                        test.clear()
                
                # return to the main menu
                break
            else:
                print('Invalid choice.\n')
    elif x == '2':
        # calculate chance of admit
        while True:
            print('Choose from the following menu options:')
            print('1 - Enter a Graduate Record Examinations (GRE) Score')
            print('2 - Enter a Test of English as a Foreign Language (TOEFL) Score')
            #print('3 - Enter a University Rating')
            #print('4 - Enter a Statement of Purpose (SOP)')
            #print('5 - Enter a Letter of Recommendation (LOR)')
            print('3 - Enter a Cumulative Grade Point Average (CGPA)')
            print('4 - Enter a Research Experience')
            print('5 - Calculate Chance of Admit')
            print('6 - Print')
            print('7 - Cancel')

            m = input('Enter your choice -> ')

            if m == '7':
                # return to the main menu
                break
            elif m == '1':
                main_input = input('Enter a GRE score  ')
                if (test.error_check(m, main_input) == True):
                    gre_score = int(main_input)
                else:
                    print('Sorry, you need to enter a number between 0 and 340.')
                    input("\nPress Any Key to Continue\n")
                    test.clear()
            elif m == '2':
                main_input = input('Enter a TOEFL score  ')
                if (test.error_check(m, main_input) == True):
                    toefl_score = int(main_input)
                else:
                    print('Sorry, you need to enter a number between 0 and 120.')
                    input("\nPress Any Key to Continue\n")
                    test.clear()
                    
            #elif m == '3':
                # evaluate to a numerical value from a text input #3 - #5
            #    uni_rating = int(input('Enter a University Rating  '))
            #elif m == '4':
            #    sop_val = float(input('Enter a SOP value  '))
            #elif m == '5':
            #    lor_val = float(input('Enter a LOR value  '))
            elif m == '3':
                main_input = input('Enter a CGPA value  ')
                if (test.error_check(m, main_input) == True):
                    cgpa_val = float(main_input)
                else:
                    print('Sorry, you need to enter a number between 0.00 and 10.00')
                    input("\nPress Any Key to Continue\n")
                    test.clear()
            elif m == '4':
                main_input = input('Enter a Research Experience value  ')
                if (test.error_check(m, main_input) == True):
                    main_input = main_input.lower()
                    if (main_input == 'y' or main_input == 'yes'):
                        res_val = 1
                    else:
                        res_val = 0
                else:
                    print('Sorry, you need to enter a Y or N.')
                    input("\nPress Any Key to Continue\n")
                    test.clear()
            elif m == '5':
                # calculate chance of admit
                if gre_score <= 0 or toefl_score <= 0 or cgpa_val <= 0:
                    print('Sorry, you need to enter a GRE score, TOEFL score, or a CGPA value.')
                    input("\nPress Any Key to Continue\n")
                    test.clear()
                elif degree == '' or school == '':
                    print('Sorry, you need to select a graduate school or program.')
                    input("\nPress Any Key to Continue\n")
                    test.clear()
                else:
                    # write to csv file
                    with open('Admission_Predict_Ver1.1.csv', mode='a') as csv_file:
                        csv_writer = csv.writer(csv_file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)

                        myData = ['000', gre_score, toefl_score, 3, 3.5, 3.5, cgpa_val, res_val]

                        # write
                        csv_writer.writerow(myData)

                    print(admit_val)
            elif m == '6':
                print('Currently, the following values have been entered:')
                print('Graduate Record Examination (GRE) Score: ' + str(gre_score))
                print('Test of English as a Foreign Language (TOEFL) Score: '+ str(toefl_score))
                #print('University Rating: ' + str(uni_rating))
                #print('Statement of Purpose (SOP): ' + str(sop_val))
                #print('Letter of Recommendation (LOR): ' + str(lor_val))
                print('Cumulative Grade Point Average (CGPA): ' + str(cgpa_val))
                if res_val == 0:
                    print('Research Experience: No')
                else:
                    print('Research Experience: Yes')
                #print('Research Experience: ' + str(res_val))
                
                #print('\n')
                input("\nPress Any Key to Continue\n")
                test.clear()
            else:
                print('Invalid choice.\n')
                input("\nPress Any Key to Continue\n")
                test.clear()
    elif x == '3':
        if(cgpa_val < cgpa_avg):
                print("\nYour CGPA is below average, consider focusing on school curriculium or retaking classes\n")
        if(res_val ~= 1):
                print("\nYou don't have reasearch experience, most students with high sucess chances have some research experience, consider looking for research opurtunities\n")
        if(gre_score < gre_avg):
                print("\nYour GRE score is below average, consider retaking the GRE is you are able to.\n)
        input("\nPress Any Key to Continue\n")
        test.clear()
        
          
        
    elif x == '4':
        print('Exiting program...')
        sys.exit()
    else:
        print('Invalid choice.\n')
        input("\nPress Any Key to Continue\n")
        test.clear()
