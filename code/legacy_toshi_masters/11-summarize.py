import csv,os, numpy, math
from itertools import islice
import datetime

title = ['filename', 'tripid', 'date', 'time', 'speed(kilometer)', 'streetlength', 'speedlimit(mph)', 'speedlimit(km)', 'speed_limit_compliance', 'speed2', 'hour', 'speed_25', 'speed_30', 'speed_35', 'speed_40', 'speed_45', 'speed_50', 'speed_55', 'speed_60', 'speed_65', 'morning', 'afternoon', 'night', 'o_gender', 'o_edu', 'o_age', 'gender', 'education_1', 'education_2', 'age_25_to_34', 'age_35_to_44', 'age_45_to_54', 'age_55_to_64', 'age_65_to_74', 'age_75_to_84', 'age_85_and_over']

def summarize():
	inputFile = open(path +'/' +filename,'rU')
	reader = csv.reader(inputFile)
	inputFile.seek(0)
	root_path = '/Users/toshiyokoo/Desktop/11_result'
	outputFile = open(os.path.join(root_path, filename[:-4] + '.csv'), 'a')
	writer = csv.writer(outputFile, lineterminator='\n')
	print >> outputFile, ','.join(title)
	for row in islice(reader, 1, None):
		list = []
		Filename = filename[:-4]
		tripid = filename[0:6] + filename[7:9] + filename[10:12]
		speed = str(row[2])
		date = str(row[3])
		hms = str(row[4])
		streetlength = str(row[9])
		speedlimit = str(row[11])
		drive_speed = float(row[2])
		if date[-4:] == '2011':
			d = datetime.datetime.strptime(date, '%d/%m/%Y')
		else:
			d = datetime.datetime.strptime(date, '%d/%m/%y')
			
		#convert the unit of speedlimit from mile to kilometer
		mile = float(row[11])
		conv_fac = 1.609344
		kilometer = mile * conv_fac
		
		#calculate speed limit compliance
		speed_limit_compliance = drive_speed / kilometer
		
		#whether the speeding or not
		if (drive_speed - kilometer) > 0:
			speed2 = 1
		else:
			speed2 = 0
			
		#change the hour from UTC to MN (Time in GPS is Greenwich Mean Time (GMT))
		f = datetime.datetime.strptime(hms, '%H:%M:%S')
		hour = f.hour
		date1 = datetime.datetime(2011, 3, 13)
		date2 = datetime.datetime(2011, 11, 5)
		#Daylight Saving Time
		if date1 <= d <= date2:
			cal_hour = hour - 5
			fix_hour = cal_hour
			if cal_hour < 0:
				fix_hour = cal_hour + 24
		#Standard Time
		else:
			cal_hour = hour - 6
			fix_hour = cal_hour
			if cal_hour < 0:
				fix_hour = cal_hour + 24
		
		#Dummy variable (Speed limit)
		num_speedlimit = int(row[11])
		speed_25 = 0
		speed_30 = 0
		speed_35 = 0
		speed_40 = 0
		speed_45 = 0
		speed_50 = 0
		speed_55 = 0
		speed_60 = 0
		speed_65 = 0
		if num_speedlimit <= 25:
			speed_25 = 1
		elif num_speedlimit == 30:
			speed_30 = 1
		elif num_speedlimit == 35:
			speed_35 = 1
		elif num_speedlimit == 40:
			speed_40 = 1
		elif num_speedlimit == 45:
			speed_45 = 1
		elif num_speedlimit == 50:
			speed_50 = 1
		elif num_speedlimit == 55:
			speed_55 = 1
		elif num_speedlimit == 60:
			speed_60 = 1
		elif num_speedlimit == 65:
			speed_65 = 1
		elif num_speedlimit == 70:
			dummy = 0
		else:
			speed_25 = 99
			speed_30 = 99
			speed_35 = 99
			speed_40 = 99
			speed_45 = 99
			speed_50 = 99
			speed_55 = 99
			speed_60 = 99
			speed_65 = 99
			
		#Dummy variable (morning, afternoon, night)
		morning = 0
		afternoon = 0
		night = 0
		dummy_hour = int(fix_hour)
		if 6 <= dummy_hour < 12:
			morning = 1
		elif 12 <= dummy_hour < 18:
			afternoon = 1
		elif 18 <= dummy_hour < 24:
			night = 1
		elif 0 <= dummy_hour < 6:
			dummy = 0
		else:
			morning = 99
			afternoon = 99
			night = 99
		
		#Input Household survey data
		#Match Tripid between GPS file and Household survey data
		TBIFile = open("/Users/toshiyokoo/Desktop/5133/TBIdata.csv",'rU')
		idlist = csv.reader(TBIFile)
		TBIFile.seek(0)
		gender = 0
		age_25_to_34 = 0
		age_35_to_44 = 0
		age_45_to_54 = 0
		age_55_to_64 = 0
		age_65_to_74 = 0
		age_75_to_84 = 0
		age_85_and_over = 0
		education_1 = 0
		education_2 = 0
		for dem in islice(idlist, 1, None):
			if int(dem[3]) == int(tripid):
		#Dummy variable (Gender)
				o_gender = dem[4]
				if dem[4] == 'Male':
					gender = 1
				elif dem[4] == 'Female':
					gender = 0
				else:
					gender = 99
		#Dummy variable (Education)
				o_education = dem[5]
				if dem[5] == 'Daycare / Pre-school':
					dummy = 0
				elif dem[5] == 'Less than high school':
					dummy = 0
				elif dem[5] == 'High school graduate':
					dummy = 0
				elif dem[5] == 'Some college':
					education_1 = 1
				elif dem[5] == 'Vocational/Technical training':
					dummy = 0
				elif dem[5] == 'Associates degree':
					education_1 = 1
				elif dem[5] == 'Bachelors degree':
					education_2 = 1
				elif dem[5] == 'Graduate/Post-graduate degree':
					education_2 = 1
				else:
					education_1 = 99
					education_2 = 99
		#Dummy variable (Age)
				o_age = dem[6]
				if	int(dem[6]) == 6:
					age_25_to_34 = 1
				elif	int(dem[6]) == 7:
					age_35_to_44 = 1
				elif	int(dem[6]) == 8:
					age_45_to_54 = 1
				elif	int(dem[6]) == 9:
					age_55_to_64 = 1
				elif	int(dem[6]) == 10:
					age_65_to_74 = 1
				elif	int(dem[6]) == 11:
					age_75_to_84 = 1
				elif	int(dem[6]) == 12:
					age_85_and_over = 1
				elif	int(dem[6]) == 5:
					dummy = 0
				else:
					age_25_to_34 = 99
					age_35_to_44 = 99
					age_45_to_54 = 99
					age_55_to_64 = 99
					age_65_to_74 = 99
					age_75_to_84 = 99
					age_85_and_over = 99
		
		list.extend([Filename, tripid, date, hms, speed, streetlength, speedlimit, kilometer, speed_limit_compliance, speed2, fix_hour, speed_25, speed_30, speed_35, speed_40, speed_45, speed_50, speed_55, speed_60, speed_65, morning, afternoon, night, o_gender, o_education, o_age, gender, education_1, education_2, age_25_to_34, age_35_to_44, age_45_to_54, age_55_to_64, age_65_to_74, age_75_to_84, age_85_and_over])
		writer.writerow(list)
	inputFile.close()
	print filename

path = "/Users/toshiyokoo/Desktop/aaaif"
for filename in os.listdir(path):
	global filename
	summarize()
