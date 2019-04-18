import csv
import sys
import test

school = ''
degree = ''
gre_score = 0
toefl_score = 0
uni_rating = 3
sop_val = 3.5
lor_val = 3.5
cgpa_val = 0.0
res_val = 0
admit_val = 0.0

cgpa_avg = 8.57644
gre_avg = 316.472
tofel_avg = 107.192
has_rch_avg = 0.5

def linearregressioncalculation(file):
    import pandas as pd
    data = pd.read_csv(file)

    data.drop('Serial No.', inplace=True, axis=1)
    data.rename({'Chance of Admit ': 'ChanceofAdmit', 'LOR ':'LOR'}, axis=1, inplace=True)

    ## Data has 500 rows and 8 columns, after erasing serial number
    #print(data.head())

    X=data.iloc[:, 0:7].values
    #X is the attributes
    y=data.iloc[:, 7].values
    #Y is the label

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    from sklearn import linear_model
    from sklearn import svm
    clf = linear_model.LinearRegression();
    results = clf.fit(X_train, y_train).predict(X_test);
    return results[len(results) -1]

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
                        input('Press Any Key to Continue\n')
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
            print('3 - Enter a University Rating')
            print('4 - Enter a Statement of Purpose (SOP)')
            print('5 - Enter a Letter of Recommendation (LOR)')
            print('6 - Enter a Cumulative Grade Point Average (CGPA)')
            print('7 - Enter a Research Experience')
            print('8 - Calculate Chance of Admit')
            print('9 - Print')
            print('0 - Cancel')

            m = input('Enter your choice -> ')

            if m == '0':
                # return to the main menu
                break
            elif m == '1':
                print('Graduate Record Examinations (GRE) scores should be entered as whole numbers between 0 and 340.')
                print('This field is required.')
                print('Enter -1 to return to the Main Menu. No changes will be made.\n')
                main_input = input('Enter a GRE score  ')
                if (test.error_check(m, main_input) == True):
                    if int(main_input) == -1:
                        gre_score = gre_score
                    else:
                        gre_score = int(main_input)
                else:
                    print('Sorry, you need to enter a number between 0 and 340.\n')
                    input('Press Any Key to Continue\n')
                    test.clear()
            elif m == '2':
                print('Test of English as a Foreign Language (TOEFL) scores should be entered as whole numbers between 0 and 120.')
                print('This field is required.')
                print('Enter -1 to return to the Main Menu. No changes will be made.\n')
                #print('Test of English as a Foreign Language (TOEFL) scores are whole numbers between 0 and 120.\n')
                main_input = input('Enter a TOEFL score  ')
                if (test.error_check(m, main_input) == True):
                    if int(main_input) == -1:
                        toefl_score = toefl_score
                    else:
                        toefl_score = int(main_input)
                else:
                    print('Sorry, you need to enter a number between 0 and 120.\n')
                    input('Press Any Key to Continue\n')
                    test.clear()
            elif m == '3':
                main_input = input('Enter a University Rating  ')
                if (test.error_check(m, main_input) == True):
                    if int(main_input) == -1:
                        uni_rating = 3
                    else:
                        uni_rating = int(main_input)
                else:
                    print('Sorry, you need to enter a number between 0 and 5.\n')
                    input('Press Any Key to Continue\n')
                    test.clear()
            elif m == '4':
                main_input = input('Enter a SOP value  ')
                if (test.error_check(m, main_input) == True):
                    try:
                        if int(main_input) == -1:
                            sop_val = 3.5
                        else:
                            sop_val = int(main_input)
                    except:
                        sop_val = float(main_input)
                else:
                    print('Sorry, you need to enter a number between 0.00 and 5.00.\n')
                    input('Press Any Key to Continue\n')
                    test.clear()
            elif m == '5':
                main_input = input('Enter a LOR value  ')
                if (test.error_check(m, main_input) == True):
                    try:
                        if int(main_input) == -1:
                            lor_val = 3.5
                        else:
                            lor_val = int(main_input)
                    except:
                        lor_val = float(main_input)
                else:
                    print('Sorry, you need to enter a number between 0.00 and 5.00.\n')
                    input('Press Any Key to Continue\n')
                    test.clear()
            elif m == '6':
                main_input = input('Enter a CGPA value  ')
                if (test.error_check(m, main_input) == True):
                    try:
                        if int(main_input) == -1:
                            cgpa_val = 3.5
                        else:
                            cgpa_val = int(main_input)
                    except:
                        cgpa_val = float(main_input)
                else:
                    print('Sorry, you need to enter a number between 0.00 and 10.00\n')
                    input('Press Any Key to Continue\n')
                    test.clear()
            elif m == '7':
                main_input = input('Enter a Research Experience value  ')
                if (test.error_check(m, main_input) == True):
                    if int(main_input) == -1:
                        res_val = 0
                    else:
                        if main_input.lower() == 'y' or main_input.lower() == 'yes':
                            res_val = 1
                        else:
                            res_val = 0
                else:
                    print('Sorry, you need to enter a Y or N.\n')
                    input('Press Any Key to Continue\n')
                    test.clear()
            elif m == '8':
                # calculate chance of admit
                if gre_score <= 0 or toefl_score <= 0 or cgpa_val <= 0:
                    print('Sorry, you need to enter a GRE score, TOEFL score, or a CGPA value.\n')
                    input('Press Any Key to Continue\n')
                    test.clear()
                elif degree == '' or school == '':
                    print('Sorry, you need to select a graduate school or program.\n')
                    input('Press Any Key to Continue\n')
                    test.clear()
                else:
                    # write to csv file
                    with open('Admission_Predict_Ver1.1.csv', mode='a', newline='') as csv_file:
                        csv_writer = csv.writer(csv_file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)

                        myData = ['000', gre_score, toefl_score, uni_rating, sop_val, lor_val, cgpa_val, res_val]

                        # write
                        csv_writer.writerow(myData)
                    
                    admit_val = linearregressioncalculation('Admission_Predict_Ver1.1.csv')
                    
                    print(admit_val)
            elif m == '9':
                print('Currently, the following values have been entered:')
                print('Graduate Record Examination (GRE) Score: ' + str(gre_score))
                print('Test of English as a Foreign Language (TOEFL) Score: '+ str(toefl_score))
                print('University Rating: ' + str(uni_rating))
                print('Statement of Purpose (SOP): ' + str(sop_val))
                print('Letter of Recommendation (LOR): ' + str(lor_val))
                print('Cumulative Grade Point Average (CGPA): ' + str(cgpa_val))
                if res_val == 0:
                    print('Research Experience: No')
                else:
                    print('Research Experience: Yes')
                #print('Research Experience: ' + str(res_val))
                if admit_val > 0:
                    print('Chance of Admit: ' + str(admit_val))
                #print('\n')
                input('Press Any Key to Continue\n')
                test.clear()
            else:
                print('Invalid choice.\n')
                input('Press Any Key to Continue\n')
                test.clear()
    elif x == '3':
        if(cgpa_val < cgpa_avg):
            print('Your CGPA is below average, consider focusing on school curriculium or retaking classes\n')
        if(res_val != 1):
            print('You don\'t have reasearch experience, most students with high sucess chances have some research experience, consider looking for research opurtunities\n')
        if(gre_score < gre_avg):
            print('Your GRE score is below average, consider retaking the GRE is you are able to.\n')
        input('Press Any Key to Continue\n')
        test.clear()
    elif x == '4':
        print('Exiting program...')
        sys.exit()
    else:
        print('Invalid choice.\n')
        input('Press Any Key to Continue\n')
        test.clear()