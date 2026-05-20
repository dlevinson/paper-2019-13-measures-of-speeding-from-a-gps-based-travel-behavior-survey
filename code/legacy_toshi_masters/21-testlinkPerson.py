#integrate multiple GPS points of one link into one GPS point

import csv,os, numpy, math
from itertools import islice
import datetime

title = ['PersonID', 'Tripid', 'LinkID', 'streetname', 'hour', 'streetlength', 'Speedlimit', 'Sum_drivespeed(kilometer)', 'sum_speedlimit(kilometer)', 'sum_speed', 'sum_time', 'degree','percentage']

def calculate():
	link_new = 999999 #Errornumber
	count = 0
	all_count = 0
	time = 0
	drive = 0
	speedlimit = 0
	speeding = 0
	inputFile = open(path +'/' +filename,'rU')
	reader = csv.reader(inputFile)
	inputFile.seek(0)
	for row in islice(reader, 1, None):
		all_count += 1

	reader = csv.reader(inputFile)
	inputFile.seek(0)	
	for row in islice(reader, 1, None):
		root_path = '/Users/toshiyokoo/Desktop/12_result'
		outputFile = open(os.path.join(root_path, filename[:-4] + '.csv'), 'a')
		writer = csv.writer(outputFile, lineterminator='\n')
		Tripname = filename[:-4]
		personid = filename[0:6] + filename[7:9] + filename[10:12]
		date = str(row[6])
		hms = str(row[7])
		streetname = str(row[10])
		streetlength = str(row[11])
		linkID = str(row[2])
		speedmph = str(row[12])
		list = []
	
		if link_new == 999999:
			print >> outputFile, ','.join(title)
			time += 1
			drive += float(row[5]) #drive_speed(kilometer)
			speedlimit += float(row[13]) #speedlimit(kilometer)
			speeding += float(row[14]) #whether speeding or not
			link_new = linkID
			old_date = date
			old_hms = hms
			old_streetname = streetname
			old_streetlength = streetlength
			old_linkID = linkID
			old_speedlimit = speedmph
			count += 1
			continue
	
		elif link_new == linkID:
			time += 1
			drive += float(row[5])
			speedlimit += float(row[13])
			speeding += float(row[14])
			#old_streetname = streetname
			#old_streetlength = streetlength
			#old_linkID = linkID
			count += 1
			if count == all_count:
				sum_drive = drive
				sum_speedlimit = speedlimit
				sum_speed = speeding
				sum_time = time
				degree = sum_drive / sum_speedlimit
				percentage = sum_speed / sum_time
				if old_date[-4:] == '2011':
					d = datetime.datetime.strptime(old_date, '%d/%m/%Y')
				else:
					d = datetime.datetime.strptime(old_date, '%d/%m/%y')
		
				#change the hour from UTC to MN (Time in GPS is Greenwich Mean Time (GMT))
				f = datetime.datetime.strptime(old_hms, '%H:%M:%S')
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
						
				list.extend([personid, Tripname, old_linkID, old_streetname, fix_hour, old_streetlength, old_speedlimit, sum_drive, sum_speedlimit, sum_speed, sum_time, degree, percentage])
				writer.writerow(list)
				break
			continue
	
		elif link_new != linkID:
			sum_drive = drive
			sum_speedlimit = speedlimit
			sum_speed = speeding
			sum_time = time
			degree = sum_drive / sum_speedlimit
			percentage = sum_speed / sum_time
			if old_date[-4:] == '2011':
				d = datetime.datetime.strptime(old_date, '%d/%m/%Y')
			else:
				d = datetime.datetime.strptime(old_date, '%d/%m/%y')
		
			#change the hour from UTC to MN (Time in GPS is Greenwich Mean Time (GMT))
			f = datetime.datetime.strptime(old_hms, '%H:%M:%S')
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
					
			list.extend([personid, Tripname, old_linkID, old_streetname, fix_hour, old_streetlength, old_speedlimit, sum_drive, sum_speedlimit, sum_speed, sum_time, degree, percentage])
			writer.writerow(list)
			list = []
			time = 1
			drive = float(row[5])
			speedlimit = float(row[13])
			speeding = float(row[14])
			link_new = linkID
			count += 1
			old_date = date
			old_hms = hms
			old_streetname = streetname
			old_streetlength = streetlength
			old_linkID = linkID
			old_speedlimit = speedmph
			if count == all_count:
				sum_drive = drive
				sum_speedlimit = speedlimit
				sum_speed = speeding
				sum_time = time
				degree = sum_drive / sum_speedlimit
				percentage = sum_speed / sum_time
				if old_date[-4:] == '2011':
					d = datetime.datetime.strptime(old_date, '%d/%m/%Y')
				else:
					d = datetime.datetime.strptime(old_date, '%d/%m/%y')
		
				#change the hour from UTC to MN (Time in GPS is Greenwich Mean Time (GMT))
				f = datetime.datetime.strptime(old_hms, '%H:%M:%S')
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
				list.extend([personid, Tripname, old_linkID, old_streetname, fix_hour, old_streetlength, old_speedlimit, sum_drive, sum_speedlimit, sum_speed, sum_time, degree, percentage])
				writer.writerow(list)
				break
	
	print filename		 
	inputFile.close()
	outputFile.close()

path = "/Users/toshiyokoo/Desktop/aaafh"
for filename in os.listdir(path):
	global filename
	calculate()