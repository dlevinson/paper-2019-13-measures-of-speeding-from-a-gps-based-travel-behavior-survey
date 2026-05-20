# Remove GPS points which are outside Minneapolis.
# Longitude: -94.0123 <= Minneapolis <= -92.7397
# Latitude: 44.4714 <= Minneapolis <= 45.4139

import csv,os
from itertools import islice

title = ['Longitude','Latitude','Speed(kilometer)','Course(degrees)','NumberOfSatellites','HDOP','Altitude(meters)','DD/MM/YY','HH:MM:SS','Distance(meters)']
def insideMap():
	inputFile = open(path +'/' +filename,'rU')
	reader = csv.reader(inputFile)
	inputFile.seek(0)
	root_path = "/Users/toshiyokoo/Desktop/02_result"
	#dir_path = os.path.join(root_path,directory)
	#if not os.path.exists( dir_path):
	#	os.mkdir( dir_path)
	
	count = 0
	all_count = 0
	#writer = csv.writer(outputFile, lineterminator='\n')
	for row in islice(reader,1,None):
		if ( -94.0123 <= float(row[0]) <= -92.7397) and ( 44.4714 <= float(row[1]) <= 45.4139) :
			count += 1
			all_count += 1
		else:
			all_count += 1
	
	inputFile.seek(0)
	if count == all_count:
		print filename[:-4] + 'is full'
		outputFile = open(os.path.join(root_path,filename[:-4]+'.csv'),'a')
		print >> outputFile, ','.join(title)
		for row in islice(reader,1,None):
			print >> outputFile, ','.join(row)
			#writer.writerow(row)
		outputFile.close()
	elif 0 < count < all_count:
		print filename[:-4] + 'is modified'
		outputFile = open(os.path.join(root_path,filename[:-4]+'.csv'),'a')
		print >> outputFile, ','.join(title)
		for row in islice(reader,1,None):
			if ( -94.0123 <= float(row[0]) <= -92.7397) and ( 44.4714 <= float(row[1]) <= 45.4139):
				print >> outputFile, ','.join(row)
				#writer.writerow(row)
		outputFile.close()
	elif count == 0:
		print filename[:-4] + 'is empty'
	inputFile.close()

path = "/Users/toshiyokoo/Desktop/aaaau"
for filename in os.listdir(path):
	global filename
	insideMap()