# Remove data whose speed limit is 0 km/h.
import csv,os
from itertools import islice

title = ['filename', 'tripid', 'date', 'time', 'speed(kilometer)', 'streetlength', 'speedlimit(mph)', 'speedlimit(km)', 'speed_limit_compliance', 'speed2', 'hour', 'speed_25', 'speed_30', 'speed_35', 'speed_40', 'speed_45', 'speed_50', 'speed_55', 'speed_60', 'speed_65', 'morning', 'afternoon', 'night', 'o_gender', 'o_edu', 'o_age', 'gender', 'education_1', 'education_2', 'age_25_to_34', 'age_35_to_44', 'age_45_to_54', 'age_55_to_64', 'age_65_to_74', 'age_75_to_84', 'age_85_and_over']
def compile():
	inputFile = open(path +'/' +filename,'rU')
	top = filename[0:2]
	top2 = int(top)
	if top2 == 10:
		reader = csv.reader(inputFile)
		inputFile.seek(0)
		for row in islice(reader,1,None):
			print >> outputFile1, ','.join(row)
		inputFile.close()
	elif top2 == 11:
		reader = csv.reader(inputFile)
		inputFile.seek(0)
		for row in islice(reader,1,None):
			print >> outputFile2, ','.join(row)
		inputFile.close()
	elif top2 == 12:
		reader = csv.reader(inputFile)
		inputFile.seek(0)
		for row in islice(reader,1,None):
			print >> outputFile3, ','.join(row)
		inputFile.close()
	elif top2 == 13:
		reader = csv.reader(inputFile)
		inputFile.seek(0)
		for row in islice(reader,1,None):
			print >> outputFile4, ','.join(row)
		inputFile.close()
	elif top2 == 14:
		reader = csv.reader(inputFile)
		inputFile.seek(0)
		for row in islice(reader,1,None):
			print >> outputFile5, ','.join(row)
		inputFile.close()
	elif top2 == 15:
		reader = csv.reader(inputFile)
		inputFile.seek(0)
		for row in islice(reader,1,None):
			print >> outputFile6, ','.join(row)
		inputFile.close()
	elif top2 == 16:
		reader = csv.reader(inputFile)
		inputFile.seek(0)
		for row in islice(reader,1,None):
			print >> outputFile7, ','.join(row)
		inputFile.close()
	elif top2 == 17:
		reader = csv.reader(inputFile)
		inputFile.seek(0)
		for row in islice(reader,1,None):
			print >> outputFile8, ','.join(row)
		inputFile.close()
	elif top2 == 18:
		reader = csv.reader(inputFile)
		inputFile.seek(0)
		for row in islice(reader,1,None):
			print >> outputFile9, ','.join(row)
		inputFile.close()
	elif top2 == 19:
		reader = csv.reader(inputFile)
		inputFile.seek(0)
		for row in islice(reader,1,None):
			print >> outputFile10, ','.join(row)
		inputFile.close()
	elif top2 == 20:
		reader = csv.reader(inputFile)
		inputFile.seek(0)
		for row in islice(reader,1,None):
			print >> outputFile11, ','.join(row)
		inputFile.close()
	print filename

path = "/Users/toshiyokoo/Desktop/aaaig"	
root_path = "/Users/toshiyokoo/Desktop/12_result"
outputFile1 = open(os.path.join(root_path,"summary_10")+'.csv','a')
outputFile2 = open(os.path.join(root_path,"summary_11")+'.csv','a')
outputFile3 = open(os.path.join(root_path,"summary_12")+'.csv','a')
outputFile4 = open(os.path.join(root_path,"summary_13")+'.csv','a')
outputFile5 = open(os.path.join(root_path,"summary_14")+'.csv','a')
outputFile6 = open(os.path.join(root_path,"summary_15")+'.csv','a')
outputFile7 = open(os.path.join(root_path,"summary_16")+'.csv','a')
outputFile8 = open(os.path.join(root_path,"summary_17")+'.csv','a')
outputFile9 = open(os.path.join(root_path,"summary_18")+'.csv','a')
outputFile10 = open(os.path.join(root_path,"summary_19")+'.csv','a')
outputFile11 = open(os.path.join(root_path,"summary_20")+'.csv','a')
writer = csv.writer(outputFile1)
writer = csv.writer(outputFile2)
writer = csv.writer(outputFile3)
writer = csv.writer(outputFile4)
writer = csv.writer(outputFile5)
writer = csv.writer(outputFile6)
writer = csv.writer(outputFile7)
writer = csv.writer(outputFile8)
writer = csv.writer(outputFile9)
writer = csv.writer(outputFile10)
writer = csv.writer(outputFile11)
print >> outputFile1, ','.join(title)
print >> outputFile2, ','.join(title)
print >> outputFile3, ','.join(title)
print >> outputFile4, ','.join(title)
print >> outputFile5, ','.join(title)
print >> outputFile6, ','.join(title)
print >> outputFile7, ','.join(title)
print >> outputFile8, ','.join(title)
print >> outputFile9, ','.join(title)
print >> outputFile10, ','.join(title)
print >> outputFile11, ','.join(title)
for filename in os.listdir(path):
	global filename
	compile()
outputFile1.close()
outputFile2.close()
outputFile3.close()
outputFile4.close()
outputFile5.close()
outputFile6.close()
outputFile7.close()
outputFile8.close()
outputFile9.close()
outputFile10.close()
outputFile11.close()