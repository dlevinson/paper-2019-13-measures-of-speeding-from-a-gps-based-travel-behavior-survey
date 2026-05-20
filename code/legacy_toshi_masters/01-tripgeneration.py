# Trip generation. Divide the GPS data into trip data.
# When the gap time is more than 300 seconds, divide the data.

import csv, dateutil, os
from itertools import islice
from dateutil import parser


tripEndTimeList = []
title = ['Longitude','Latitude','Speed(kilometer)','Course(degrees)','NumberOfSatellites','HDOP','Altitude(meters)','DD/MM/YY','HH:MM:SS','Distance(meters)']

def getTimeElapsed(time1, time2):
	t1 = parser.parse(time1)
	t2 = parser.parse(time2)
	return (t2 - t1).seconds
			
def countTrips():
	count = 0
	line = 0
	root_path = "/Users/toshiyokoo/Desktop/result1"
	dir_path = os.path.join(root_path,filename[0:12])
	#os.mkdir(dir_path)
	inputFile = open(path +'/' +filename,'rU')
	reader = csv.reader(inputFile)
	fileCount=len(inputFile.readlines())
	inputFile.seek(0)
	oldTime = None
	oldDate = None
	for row in islice(reader, 1, fileCount-1):
		line +=1
		if oldDate == None:
			oldDate = row[7]
			oldTime = row[8]
			tripFile = open(os.path.join(root_path,filename[0:12]+'_'+str(count+1))+'.csv','a')
			print >>tripFile,','.join(title)
			print >>tripFile,','.join(row)
			tripFile.close()
			continue
		else:
			newDate = row[7]
			newTime = row[8]
			oldline = line
			if line < fileCount-2:
				if newDate != oldDate: 
					tripEndTimeList.append(oldTime)
					oldDate = newDate
					oldTime = newTime
					count +=1
					tripFile = open(os.path.join(root_path,filename[0:12]+'_'+str(count+1))+'.csv','a')
					print >>tripFile,','.join(title)
					print >>tripFile,','.join(row)
					tripFile.close()
					continue
				if newDate == oldDate:
					if getTimeElapsed(oldTime, newTime) >=300: 
						tripEndTimeList.append(oldTime)
						oldDate = newDate
						oldTime = newTime
						count += 1
						tripFile = open(os.path.join(root_path,filename[0:12]+'_'+str(count+1))+'.csv','a')
						print >>tripFile,','.join(title)
						print >>tripFile,','.join(row)
						tripFile.close()
						continue
					else:
						oldDate = newDate
						oldTime = newTime
						tripFile = open(os.path.join(root_path,filename[0:12]+'_'+str(count+1))+'.csv','a')
						print >>tripFile,','.join(row)
						tripFile.close
						continue
			if line == fileCount-2:
				tripFile = open(os.path.join(root_path,filename[0:12]+'_'+str(count+1))+'.csv','a')
				print >>tripFile,','.join(row)
				tripFile.close					
				count +=1		
				tripEndTimeList.append(row[8])	
	print filename[0:12], count

path = "/Users/toshiyokoo/Desktop/aaaac"
for filename in os.listdir(path):
	global filename
	countTrips()



