# Remove data whose speed limit is 0 km/h.
import csv,os
from itertools import islice

title = ['Longitude','Latitude','Speed(kilometer)','DD/MM/YY','HH:MM:SS','GX','GY','Min_hight','Streetname', 'Streetlength', 'Roadtype','Speedlimit(mph)']
def removespeed():
	inputFile = open(path +'/' +filename,'rU')
	reader = csv.reader(inputFile)
	inputFile.seek(0)
	root1_path = "/Users/toshiyokoo/Desktop/10_result"
	root2_path = "/Users/toshiyokoo/Desktop/10_result_error"
	count = 0
	all_count = 0
	for row in islice(reader,1,None):
		if int(row[11]) > 0:
			count += 1
			all_count += 1
		else:
			all_count += 1
	
	inputFile.seek(0)
	if count == 0:
		print filename[:-4] + 'is empty'
		outputFile = open(os.path.join(root2_path,filename[:-4]+'.csv'),'a')
		writer = csv.writer(outputFile)	
		print >> outputFile, ','.join(title)	
		for row in islice(reader,1,None):
			print >> outputFile, ','.join(row)
		outputFile.close()
	elif count == all_count:
		print filename[:-4] + 'is full'
		outputFile = open(os.path.join(root1_path,filename[:-4]+'.csv'),'a')
		writer = csv.writer(outputFile)	
		print >> outputFile, ','.join(title)	
		for row in islice(reader,1,None):
			print >> outputFile, ','.join(row)
		outputFile.close()
	elif 0 < count < all_count:
		print filename[:-4] + 'is modified'
		outputFile = open(os.path.join(root1_path,filename[:-4]+'.csv'),'a')
		writer = csv.writer(outputFile)	
		print >> outputFile, ','.join(title)
		for row in islice(reader,1,None):
			if int(row[11]) > 0:
				print >> outputFile, ','.join(row)
		outputFile.close()
	inputFile.close()

path = "/Users/toshiyokoo/Desktop/aaafw"
for filename in os.listdir(path):
	global filename
	removespeed()
