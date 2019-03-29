import sys

# user interface
print('Choose from the following menu options:')
print('1 - Enter a Graduate Record Examinations (GRE) Score')
print('2 - Enter a Test of English as a Foreign Language (TOEFL) Score')
print('3 - Enter a University Rating')
print('4 - Enter a Statement of Purpose (SOP)')
print('5 - Enter a Letter of Recommendation (LOR)')
print('6 - Enter a Cumulative Grade Point Average (CGPA)')
print('7 - Enter a Research Experience')
print('8 - Calculate Chance of Admit') # Suggest alternatives, increase 'Chance of Admit'
print('9 - Print')
print('0 - Exit the program\n')

# local variables (uniform variable names, suffix/prefix: _val)
gre_score = 0
toefl_score = 0
university_rating = 0
sop_val = 0.0
lor_val = 0.0
cgpa_val = 0.0
research_val = 0
admit_val = 0.0

while True:
    # copy, paste here if menu should be printed every time when prompted 
    main_input = int(raw_input('Enter your choice -> '))

    #switch
    if main_input == 1:
        # Between 0 and 340 (whole number)
        # Cannot be a negative number
        gre_score = int(raw_input('Enter a GRE score  '))
    elif main_input == 2:
        # Between 0 and 120 (whole number)
        # Cannot be a negative number
        toefl_score = int(raw_input('Enter a TOEFL score  '))
    elif main_input == 3:
        # Between 0 and 5
        # Better as a String answer (less ambiguous)
        # Remove as a menu option and use mean or median
        university_rating = int(raw_input('Enter a University Rating  '))
    elif main_input == 4:
        # Between 0 and 5.0
        # Better as a String answer (less ambiguous)
        # Remove as a menu option and use mean or median
        sop_val = float(raw_input('Enter a SOP value  '))
    elif main_input == 5:
        # Between 0 and 5.0
        # Better as a String answer (less ambiguous)
        # Remove as a menu option and use mean or median
        lor_val = float(raw_input('Enter a LOR value  '))
    elif main_input == 6:
        # Between 0.0 and 10.0
        cgpa_val = float(raw_input('Enter a CGPA value  '))
    elif main_input == 7:
        # Convert Research Experience to a 0 or 1 (Y/N, Yes/No, yes/no)
        # Use lower()
        research_val = int(raw_input('Enter a Research Experience value (Y/N)  '))
    elif main_input == 8:
        # Do something
        print('Calculating...')
        
        # GRE, TOEFL, and CGPA required (default values -1, instead of 0?)

        # Otherwise, print a message and loop back

        # Print Chance of Admit
        print('Chance of Admit: ' + str(admit_val))
    elif main_input == 9:
        print('Currently, the following values have been entered:\n')
        print('Graduate Record Examination (GRE) Score: ' + str(gre_score))
        print('Test of English as a Foreign Language (TOEFL) Score: '+ str(toefl_score))
        print('University Rating: ' + str(university_rating))
        print('Statement of Purpose (SOP): ' + str(sop_val))
        print('Letter of Recommendation (LOR): ' + str(lor_val))
        print('Cumulative Grade Point Average (CGPA): ' + str(cgpa_val))
        print('Research Experience: ' + str(research_val))
    elif main_input == 0:
        print('Exiting...')
        sys.exit()
    else:
        print('Wrong input. Must be between 0 and 9.')
    
    print('\n')