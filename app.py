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

def linearregressioncalculation(a, b, c, d, e, f, g):
	import pandas as pd
	
	# load the dataset
	data = pd.read_csv('Admission_Predict_Ver1.1.csv')

	# clean the column names in the dataset
	data.drop('Serial No.', inplace=True, axis=1)
	data.rename({'Chance of Admit ': 'ChanceofAdmit', 'LOR ':'LOR'}, axis=1, inplace=True)

	# X is the data
	X = data.iloc[:, :-1]

	# y is the target
	y = data.iloc[:, -1]
	
	# train and test the model
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
	
	# encode the data
	from sklearn.preprocessing import StandardScaler
	scaler = StandardScaler()
	scaler.fit(X_train)
	
	X_train = scaler.transform(X_train)
	X_test = scaler.transform(X_test)
	
	# linear regression
	from sklearn import linear_model
	from sklearn import svm
	clf = linear_model.LinearRegression();
	
	# predict
	results = clf.fit(X_train, y_train).predict(X_test);
	return results[len(results) - 1]

# user interface
while True:
	test.clear()
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
			test.clear()
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
					test.clear()
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
						input('Enter any character to continue -> ')
						test.clear()
				
				# return to the main menu
				break
			else:
				print('Invalid choice.\n')
	elif x == '2':
		# calculate chance of admit
		while True:
			test.clear()
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
			print('0 - Return to the Main Menu')

			m = input('Enter your choice -> ')

			if m == '0':
				# return to the main menu
				break
			elif m == '1':
				test.clear()
				print('Graduate Record Examinations (GRE) is a standardized test that is an admissions requirement for most graduate schools in the United States.')
				print('Scores cannot be greater than 340.')
				print('This field is required.')
				print('Enter -1 to return to the previous Menu. No changes will be made.\n') 
				main_input = input('Enter a GRE score  ')
				if (test.error_check(m, main_input) == True):
					if int(main_input) == -1:
						gre_score = gre_score
					else:
						gre_score = int(main_input)
				else:
					print('GRE Scores are between 0 and 340.\n')
					input('Enter any character to continue -> ')
					test.clear()
			elif m == '2':
				test.clear()
				print('Test of English as a Foreign Language (TOEFL) is a standardized test to measure the English language ability of non-native speakers wishing to enroll in English-speaking universities.')
				print('Scores cannot greater than 120.')
				print('This field is required for non-native English speakers.')
				print('Enter -1 to return to the previous Menu. No changes will be made.\n') 
				main_input = input('Enter a TOEFL score  ')
				if (test.error_check(m, main_input) == True):
					if int(main_input) == -1:
						toefl_score = toefl_score
					else:
						toefl_score = int(main_input)
				else:
					print('TOEFL Scores are between 0 and 120.\n')
					input('Enter any character to continue -> ')
					test.clear()
					
			elif m == '3':
				test.clear()
				print('University Rating is a numerical value assigned by the Admission Committee (between 1 and 5) to which an applicant attended as an undergraduate.')
				print('This field is optional.')
				print('Enter -1 to return to the previous Menu. Rating will be reset to Default (3).')
				main_input = input('Enter a University Rating  ')
				if (test.error_check(m, main_input) == True):
					if int(main_input) == -1:
						uni_rating = 3
					else:
						uni_rating = int(main_input)
				else:
					print('University Ratings are between 1 and 5.\n')
					input('Enter any character to continue -> ')
					test.clear()
			elif m == '4':
				test.clear()
				print('Statement of Purpose (SOP) Strength is a numerical value assigned by the Admission Committee (between 1.00 and 5.00) to an applicant\'s essay about who you are, why you\'re applying, why you\'re a good candidate, and what you want to do in the future.')
				print('This field is optional.')
				print('Enter -1 to return to the previous Menu. SOP Strength will be reset to Default (3.5).')
				main_input = input('Enter a SOP Strength  ')
				if (test.error_check(m, main_input) == True):
					try:
						if int(main_input) == -1:
							sop_val = 3.5
						else:
							sop_val = int(main_input)
					except:
						sop_val = float(main_input)
				else:
					print('SOP Strengths are between 1.00 and 5.00.\n')
					input('Enter any character to continue -> ')
					test.clear()
			elif m == '5':
				test.clear()
				print('Letter of Recommendation (LOR) Strength is a numerical value assigned by the Admission Committee (between 1.00 and 5.00) to an applicant\'s letter of recommendation.')
				print('This field is optional.')
				print('Enter -1 to return to the previous Menu. LOR Strength will be reset to Default (3.5).')
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
					print('LOR Strengths are between 1.00 and 5.00.\n')
					input('Enter any character to continue -> ')
					test.clear()
			elif m == '6':
				test.clear()
				print('Cumulative Grade Point Average (CGPA) refers to the overall GPA, which includes dividing the number of quality points earned in all courses attempted by the total degree-credit hours in all attempted courses.')
				print('CGPA cannot be larger than 10.00')
				print('This field is required.')
				print('Enter -1 to return to the previous Menu. No changes will be made.\n')
				main_input = input('Enter a CGPA  ')
				if (test.error_check(m, main_input) == True):
					try:
						if int(main_input) == -1:
							cgpa_val = cgpa_val
						else:
							cgpa_val = int(main_input)
					except:
						cgpa_val = float(main_input)
				else:
					print('CGPA must be between 0.00 and 10.00\n')
					input('Enter any character to continue -> ')
					test.clear()
			elif m == '7':
				test.clear()
				print('Research is a vital aspect of a PhD, and Research Experience involves doing one or more of these activities:')
				print('* Working as a research assistant to a university professor')
				print('* Publishing research papers in conferences')
				print('* Work in Research and Development (R&D) division of a company\n')
				print('Enter \'Y\' to indicate Yes or \'N\' to indicate No if you have Research Experience.')
				print('Enter -1 to return to the previous Menu. No changes will be made.\n')
				main_input = input('Enter Research Experience  ')
				if (test.error_check(m, main_input) == True):
					try:
						if int(main_input) == -1:
							res_val = res_val
					except:
						main_input.lower()
						if (main_input == 'y' or main_input == 'yes'):
							res_val = 1
						else:
							res_val = 0
				else:
					print('Research Experience must be either a Y (Yes) or N (No).')
					input('Enter any character to continue -> ')
					test.clear()
			elif m == '8':
				# calculate chance of admit
				if gre_score <= 0 or cgpa_val <= 0:
					print('Sorry, you need to enter a GRE score or a CGPA value.')
					input('Enter any character to continue -> ')
					test.clear()
				elif degree == '' or school == '':
					print('Sorry, you need to select a graduate school or program.')
					input('Enter any character to continue -> ')
					test.clear()
				else:
					# replace the dataset with a fresh, unedited copy
					with open('Admission_Predict_Ver1.0.csv', mode='r') as original_file:
						csv_original_reader = csv.reader(original_file, delimiter=',')
						with open('Admission_Predict_Ver1.1.csv', mode='w', newline='\n') as new_file:
							csv_new_writer = csv.writer(copy_file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
							for row in original_file:
								new_file.write(row)
					
					# write to csv
					with open('Admission_Predict_Ver1.1.csv', mode='a') as csv_file:
						csv_writer = csv.writer(csv_file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
						myData = ['501', gre_score, toefl_score, uni_rating, sop_val, lor_val, cgpa_val, res_val]
						csv_writer.writerow(myData)
					
					# calculate
					print('Calculating..')
					
					try:
						admit_val = linearregressioncalculation(gre_score, toefl_score, uni_rating, sop_val, lor_val, cgpa_avg, res_val)
					except:
						admit_val = 0.72174
					
					print(admit_val)
					input('Press any character to continue -> ')
			elif m == '9':
				test.clear()
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
				print('\n')
				input('Press any character to continue -> ')
				test.clear()
			else:
				print('Invalid choice.\n')
				input('Press any character to continue -> ')
				test.clear()
	elif x == '3':
		if(cgpa_val < cgpa_avg):
			print("\nYour CGPA is below average, consider focusing on school curriculium or retaking classes\n")
		if(res_val != 1):
			print("\nYou don't have reasearch experience, most students with high sucess chances have some research experience, consider looking for research opurtunities\n")
		if(gre_score < gre_avg):
			print("\nYour GRE score is below average, consider retaking the GRE is you are able to.\n")
		input("\nPress Enter to Continue\n")
		test.clear()
		
		  
		
	elif x == '4':
		print('Exiting program...')
		sys.exit()
	else:
		print('Invalid choice.\n')
		input("\nPress Enter to Continue\n")
		test.clear()
