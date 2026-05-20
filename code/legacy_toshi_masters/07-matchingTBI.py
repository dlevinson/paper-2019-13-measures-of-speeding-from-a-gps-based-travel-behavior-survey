# extract file that match tripid of TBI data

import csv,os
from itertools import islice
import math
import shutil

title = ['Longitude','Latitude','Speed(kilometer)','Course(degrees)','NumberOfSatellites','HDOP','Altitude(meters)','DD/MM/YY','HH:MM:SS','Distance(meters)','GX','GY']
def matching():
	inputFile = open(path +'/' +filename,'rU')
	reader = csv.reader(inputFile)
	tripid = filename[0:6] + filename[7:9] + filename[10:12]
	TBIFile = open("/Users/toshiyokoo/Desktop/5133/TBIdata.csv",'rU')
	idlist = csv.reader(TBIFile)
	TBIFile.seek(0)
	id = 0
	for row in islice(idlist, 1, None):
		if int(row[3]) == int(tripid):
			root_path = '/Users/toshiyokoo/Desktop/07_result'
			outputFile = open(os.path.join(root_path, filename[:-4] + '.csv'), 'a')
			print >> outputFile, ','.join(title)
			inputFile.seek(0)
			for row in islice(reader,1,None):
				print >> outputFile, ','.join(row)
			outputFile.close()
			print filename[:-4], "match"
			id = 1
	
	if id == 0:
		root_error = '/Users/toshiyokoo/Desktop/07_result_error'
		outputFile_error = open(os.path.join(root_error, filename[:-4] + '.csv'), 'a')
		print >> outputFile_error, ','.join(title)
		inputFile.seek(0)
		for row in islice(reader,1,None):
			print >> outputFile_error, ','.join(row)
		outputFile_error.close()
		print filename[:-4], "mismatch"
	inputFile.close()

path = "/Users/toshiyokoo/Desktop/aaaee"
for filename in os.listdir(path):
	global filename
	matching()
