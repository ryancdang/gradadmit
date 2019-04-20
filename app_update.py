import csv
import sys
import test
# import warnings filter
#from warnings import simplefilter
# ignore all future warnings
#simplefilter(action='ignore', category=FutureWarning)
# import warnings filter
#from warnings import simplefilter
# ignore all future warnings
#simplefilter(action='ignore', category=FutureWarning)

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

def linearregressioncalculation(a, b, c, d, e, f, g):
    #import pandas as pd
    #data = pd.read_csv(file)

    #data.drop('Serial No.', inplace=True, axis=1)
    #data.rename({'Chance of Admit ': 'ChanceofAdmit', 'LOR ':'LOR'}, axis=1, inplace=True)

    ## Data has 500 rows and 8 columns, after erasing serial number
    #print(data.head())

    #X=data.iloc[:, 0:7].values
    #X is the attributes
    #y=data.iloc[:, 7].values
    #Y is the label

    #from sklearn.model_selection import train_test_split
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    #from sklearn.preprocessing import StandardScaler
    #scaler = StandardScaler()
    #scaler.fit(X_train)

    #X_train = scaler.transform(X_train)
    #X_test = scaler.transform(X_test)

    #from sklearn import linear_model
    #from sklearn import svm
    #clf = linear_model.LinearRegression();
    #results = clf.fit(X_train, y_train).predict(X_test);
    #return results[len(results) -1]


    # import packages
    #import numpy as np
    #import pandas as pd
    #from sklearn.tree import DecisionTreeRegressor
    #from sklearn.metrics import mean_absolute_error
    #from sklearn.model_selection import train_test_split

    # uploading the dataset
    #graduate_admisssion_data = pd.read_csv('Admission_Predict_Ver1.1.csv')

    # Test to see if the data can open
    #graduate_admisssion_data.head()

    # Check if the columns name are correctly named
    #graduate_admisssion_data.columns

    # Clean the titles of the columns, because there are spaces
    #graduate_admisssion_data.columns = graduate_admisssion_data.columns.str.replace(' ', '_')
    #Check to see if the spaces have been replaced
    #graduate_admisssion_data.columns

    ###
    #y = graduate_admisssion_data.Chance_of_Admit_
    #admission_features = ['GRE_Score', 'TOEFL_Score', 'University_Rating', 'SOP', 'LOR_', 'CGPA', 'Research']
    #X = graduate_admisssion_data[admission_features]

    #admission_model = DecisionTreeRegressor(random_state=1)
    #admission_model.fit(X, y)

    #print("Making predictions for the following 5 students:")
    #print(X.head(502))
    #print("The predictions are")
    #print(admission_model.predict(X.head()))

    #return admission_model.predict([[a,b,c,d,e,f,g]])

    import pandas as pd
    #import numpy as np
    #from sklearn.tree import DecisionTreeRegressor
    #from sklearn.metrics import mean_absolute_error
    #from sklearn.model_selection import train_test_split

    #from sklearn import neighbors

    # Load the dataset
    data = pd.read_csv('Admission_Predict_Ver1.1.csv')

    # Clean the column names in the dataset
    data.drop('Serial No.', inplace=True, axis=1)
    data.rename({'Chance of Admit ': 'ChanceofAdmit', 'LOR ':'LOR'}, axis=1, inplace=True)

    # X is the data
    #admission_features = ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'CGPA', 'Research']
    #X = data[admission_features]
    X = data.iloc[:, :-1]

    # y = target values, last column of the data frame
    y = data.iloc[:, -1]
    #data.head()
    #print(data.columns)

    # Check to see if columns were named correctly
    #data.GRE_Score
    
    # X is the data
    #X = data['GRE_Score', 'TOEFL_Score', 'University_Rating', 'SOP', 'LOR', 'CGPA', 'Research']
    
    # y is the target
    #y = data.ChanceofAdmit

    # Model
    #from sklearn.linear_model import LogisticRegression
    #from sklearn import svm
        
    #model = LogisticRegression(random_state=1)
    #model.fit(X,y)

    # Train/Test the Model
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

     #from sklearn.model_selection import train_test_split
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

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

    #print('Step 3, Done.\n')

    #from sklearn import preprocessing
    #from sklearn import utils

    #lab_enc = preprocessing.LabelEncoder()
    #encoded = lab_enc.fit_transform(data)

    # kNN
    #knn = neighbors.KNeighborsClassifier(n_neighbors=1)
    #knn.fit(X,y)

    #print('Step 4, Done.\n')

    # What is the ChanceofAdmit for a student with 
    #print(data.predict([[100,100,3,3.5,3.5,8.04,0]]))

    #return 1000


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
                print('Graduate Record Examinations (GRE) is a standardized test that is an admissions requirement for most graduate schools in the United States.'_
                print('Scores cannot be a number larger than 340.')
                print('This field is required.')
                print('Enter -1 to return to the Main Menu. No changes will be made.\n')
                main_input = input('Enter a GRE score  ')
                if (test.error_check(m, main_input) == True):
                    if int(main_input) == -1:
                        gre_score = gre_score
                    else:
                        gre_score = int(main_input)
                else:
                    print('GRE Scores are between 0 and 340.\n')
                    input('Enter any key to continue -> ')
                    test.clear()
            elif m == '2':
                print('Test of English as a Foreign Language (TOEFL) is a standardized test to measure the English language ability of non-native speakers wishing to enroll in English-speaking universities.')
                print('Scores cannot be a number larger than 120.')
                print('This field is required for non-native English speakers.')
                print('Enter -1 to return to the Main Menu. No changes will be made.\n')
                # The TOEFL is a test for non-native English speakers applying to English-speaking universities.
                #print('Test of English as a Foreign Language (TOEFL) scores should be entered as whole numbers between 0 and 120.')
                #print('This field is required.')
                #print('Enter -1 to return to the Main Menu. No changes will be made.\n')
                #print('Test of English as a Foreign Language (TOEFL) scores are whole numbers between 0 and 120.\n')
                main_input = input('Enter a TOEFL score  ')
                if (test.error_check(m, main_input) == True):
                    if int(main_input) == -1:
                        toefl_score = toefl_score
                    else:
                        toefl_score = int(main_input)
                else:
                    print('TOEFL Scores are between 0 and 120.\n')
                    input('Enter any key to continue -> ')
                    test.clear()
            elif m == '3':
                #print('University Ratings ')
                #print('University Ratings should be entered as a whole numbers between 0 and 5.')
                #print('This field is optional.')
                #print('Enter -1 to return to the Main Menu. Default: 3.')
                main_input = input('Enter a University Rating  ')
                if (test.error_check(m, main_input) == True):
                    if int(main_input) == -1:
                        uni_rating = 3
                    else:
                        uni_rating = int(main_input)
                else:
                    print('University Ratings are between 0 and 5.\n')
                    input('Enter any key to continue -> ')
                    test.clear()
            elif m == '4':
                print('A Statement of Purpose (SOP) is an essay telling the admission committee who you are, why you\'re applying, why you\'re a good candidate, and what you want to do in the future.')
                print('Since an applicant (under normal circumstances) does not know the strength of their SOP, this field is optional.')
                print('Unless you are confident that you have a strong SOP, the default is 3.5.')
                print('Enter -1 to return to the Main Menu. SOP will remain 3.5.')
                #print('A Statement of Purpose (SOP) Strength serves to introduce your research/professional skills and interests to the programs you\'re applying for.')
                #print('SOP values can be decimal values between 0 and 5. This field is optional.')
                #print('Enter -1 to return to the Main Menu. Default: 3.5')
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
                    print('SOP values are between 0.00 and 5.00.\n')
                    input('Enter any key to continue -> ')
                    test.clear()
            elif m == '5':
                print('A Letter of Recommendation (LOR) Strength...')
                print('LOR values can be decimal values between 0.00 and 5.00. This field is optional.')
                print('Enter -1 to return to the Main Menu.')
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
                    try:
                        if int(main_input) == -1:
                            res_val = 0
                        else:
                            if main_input.lower() == 'y' or main_input.lower() == 'yes':
                                res_val = 1
                            else:
                                res_val = 0
                    except:
                        res_val = res_val
                else:
                    print('Sorry, you need to enter a Y or N.\n')
                    input('Press Any Key to Continue\n')
                    test.clear()
            elif m == '8':
                # calculate chance of admit
                if gre_score <= 0 or cgpa_val <= 0:
                    print('Sorry, you need to enter a GRE score or a CGPA value.\n')
                    input('Press Any Key to Continue\n')
                    test.clear()
                elif degree == '' or school == '':
                    print('Sorry, you need to select a graduate school or program.\n')
                    input('Press Any Key to Continue\n')
                    test.clear()
                else:
                    # Copy original dataset to model test/train dataset (put it at the beginning, just in case?)
                    with open('Admission_Predict_Ver1.0.csv', mode='r') as original_file:
                        csv_reader_original = csv.reader(original_file, delimiter=',')
                        with open('Admission_Predict_Ver1.1.csv', mode='w', newline='\n') as copy_file:
                            csv_writer_copy = csv.writer(copy_file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                            for row in original_file:
                                copy_file.write(row)

                    # write to csv file
                    with open('Admission_Predict_Ver1.1.csv', mode='a', newline='\n') as csv_file:
                        csv_writer = csv.writer(csv_file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                        #csv_writer = csv.writer(csv_file, lineterminator='\n')
                        
                    
                        myData = ['501', int(gre_score), int(toefl_score), int(uni_rating), float(sop_val), float(lor_val), float(cgpa_val), int(res_val), float(admit_val)]

                        # write
                        csv_writer.writerow(myData)
                    
                    print('Calculating..\n')

                    #try:
                    admit_val = linearregressioncalculation(gre_score, toefl_score, uni_rating, sop_val, lor_val, cgpa_avg, res_val)
                    #except:
                        # What now? Store admit_val as what??
                    #    admit_val = 123456789
                    
                    print(admit_val)

                    # Replace Admission_Predict_Ver1.1.csv with Default Copy
                    #with open('Admission_Predict_Ver1.0.csv', mode='r') as original_file:
                    #    csv_reader = csv.reader(original_file, delimiter=',')
                    #    line_count = 0
                    #    for row in csv_reader:
                    #        if line_count == 0:
                    #            with open('Admission_Predict_Ver1.1.csv', mode='w', newline='') as copy_file:
                    #                csv_writer = csv.writer(copy_file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                    #                csv_writer.writerow(f'{", ".join(row)}')
                                #print(f'{", ".join(row)}')
                    #            line_count += 1
                    #        else:
                    #            if line_count <= 500:
                    #                with open('Admission_Predict_Ver1.1.csv', mode='a', newline='') as copy_file:
                    #                    csv_writer = csv.writer(copy_file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                    #                    csv_writer.writerow(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}') 
                                    #print(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}')
                    #                line_count += 1
                    #    print('\nDone.\n')

                    
                    
                    #print('\nDone.\n')

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