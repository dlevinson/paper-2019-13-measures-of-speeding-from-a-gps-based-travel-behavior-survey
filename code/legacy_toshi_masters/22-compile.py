import csv,os
from itertools import islice

title = ['PersonID', 'Tripid', 'LinkID', 'streetname', 'hour', 'streetlength', 'Speedlimit', 'Sum_drivespeed(kilometer)', 'sum_speedlimit(kilometer)', 'sum_speed', 'sum_time', 'degree','percentage']
def compile():
	inputFile = open(path +'/' +filename,'rU')
	reader = csv.reader(inputFile)
	inputFile.seek(0)
	for row in islice(reader,1,None):
		print >> outputFile, ','.join(row)
	inputFile.close()
	print filename

path = "/Users/toshiyokoo/Desktop/aaafi"	
root_path = "/Users/toshiyokoo/Desktop/13_result"
outputFile = open(os.path.join(root_path,"summary_13")+'.csv','a')
writer = csv.writer(outputFile)
print >> outputFile, ','.join(title)
for filename in os.listdir(path):
	global filename
	compile()
outputFile.close()