# extract file that match tripid of TBI data

import csv,os, pandas
import pandas as pd
from scipy import stats
from itertools import islice
import math
import numpy
	
path = "/Users/toshiyokoo/Desktop/aaals"
count = 1
for filename in os.listdir(path):
	if count == 1:
		data = pandas.read_csv(path +'/' +filename)
		asso = data[data['o_edu'] == 'Associates degree']['speed_limit_compliance']
		some = data[data['o_edu'] == 'Some college']['speed_limit_compliance']
		high = data[data['o_edu'] == 'High school graduate']['speed_limit_compliance']
		voca= data[data['o_edu'] == 'Vocational/Technical training']['speed_limit_compliance']
		bach = data[data['o_edu'] == 'Bachelors degree']['speed_limit_compliance']
		grad = data[data['o_edu'] == 'Graduate/Post-graduate degree']['speed_limit_compliance']
		print filename + "1"
	else:
		data = pandas.read_csv(path +'/' +filename)
		add0 = data[data['o_edu'] == 'Associates degree']['speed_limit_compliance']
		add1 = data[data['o_edu'] == 'Some college']['speed_limit_compliance']
		add2 = data[data['o_edu'] == 'High school graduate']['speed_limit_compliance']
		add3 = data[data['o_edu'] == 'Vocational/Technical training']['speed_limit_compliance']
		add4 = data[data['o_edu'] == 'Bachelors degree']['speed_limit_compliance']
		add5 = data[data['o_edu'] == 'Graduate/Post-graduate degree']['speed_limit_compliance']
		asso = pd.concat([asso,add0])
		some = pd.concat([some,add1])
		high = pd.concat([high,add2])
		voca = pd.concat([voca,add3])
		bach = pd.concat([bach,add4])
		grad = pd.concat([grad,add5])
		print filename + "2"
	if count == 11:
		print "high, some", stats.ttest_ind(high,some, equal_var = False)
		print "grad, some", stats.ttest_ind(grad,some, equal_var = False)
		print numpy.mean(asso)
		print numpy.mean(bach)
		print numpy.mean(grad)
		print numpy.mean(high)
		print numpy.mean(some)
		print numpy.mean(voca)
	count += 1
