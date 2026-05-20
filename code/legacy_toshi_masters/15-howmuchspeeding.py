
import csv,os
from itertools import islice

title = ['tripid', 'total_time', 'total_speeding', 'percentage', 'gender', 'education', 'age']
def howmuch():
	inputFile = open(path +'/' +filename,'rU')
	reader = csv.reader(inputFile)
	count = 0
	num_speed = 0
	list = []
	for row in islice(reader,1,None):
		count += 1
		tripid = int(row[1])
		speeding = int(row[9])		
		if speeding == 1:
			num_speed +=1
			
		if count == 1:
			#Input Household survey data
			#Match Tripid between GPS file and Household survey data
			TBIFile = open("/Users/toshiyokoo/Desktop/5133/TBIdata.csv",'rU')
			idlist = csv.reader(TBIFile)
			TBIFile.seek(0)
			for dem in islice(idlist, 1, None):
				if int(dem[3]) == int(tripid):
					o_gender = dem[4]
					o_education = dem[5]
					o_age = dem[6]
	
	time = count
	speed = num_speed
	total_time = float(time)
	total_speeding = float(speed)
	
	#percentage of speeding depends on individuals
	percentage = float(total_speeding / total_time)
	
	list.extend([tripid, total_time, total_speeding, percentage, o_gender, o_education, o_age])
	writer.writerow(list)
	list = []
	
	inputFile.close()
	print filename

path = "/Users/toshiyokoo/Desktop/aaaie"
root_path = '/Users/toshiyokoo/Desktop/15_result'
outputFile = open(os.path.join(root_path,"summary_percentage")+'.csv','a')
writer = csv.writer(outputFile, lineterminator='\n')
print >> outputFile, ','.join(title)
for filename in os.listdir(path):
	global filename
	howmuch()
outputFile.close()