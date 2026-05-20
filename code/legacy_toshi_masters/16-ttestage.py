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
		age5 = data[data['o_age'] == 5]['speed_limit_compliance']
		age6 = data[data['o_age'] == 6]['speed_limit_compliance']
		age7 = data[data['o_age'] == 7]['speed_limit_compliance']
		age8 = data[data['o_age'] == 8]['speed_limit_compliance']
		age9 = data[data['o_age'] == 9]['speed_limit_compliance']
		age10 = data[data['o_age'] == 10]['speed_limit_compliance']
		age11 = data[data['o_age'] == 11]['speed_limit_compliance']
		age12 = data[data['o_age'] == 12]['speed_limit_compliance']
		print filename + "1"
	else:
		data = pandas.read_csv(path +'/' +filename)
		add5 = data[data['o_age'] == 5]['speed_limit_compliance']
		add6 = data[data['o_age'] == 6]['speed_limit_compliance']
		add7 = data[data['o_age'] == 7]['speed_limit_compliance']
		add8 = data[data['o_age'] == 8]['speed_limit_compliance']
		add9 = data[data['o_age'] == 9]['speed_limit_compliance']
		add10 = data[data['o_age'] == 10]['speed_limit_compliance']
		add11 = data[data['o_age'] == 11]['speed_limit_compliance']
		add12 = data[data['o_age'] == 12]['speed_limit_compliance']
		age5 = pd.concat([age5,add5])
		age6 = pd.concat([age6,add6])
		age7 = pd.concat([age7,add7])
		age8 = pd.concat([age8,add8])
		age9 = pd.concat([age9,add9])
		age10 = pd.concat([age10,add10])
		age11 = pd.concat([age11,add11])
		age12 = pd.concat([age12,add12])
		print filename + "2"
	if count == 11:
		print "age6, age7", stats.ttest_ind(age6,age7, equal_var = False)
		print "age7, age8", stats.ttest_ind(age7,age8, equal_var = False)
		print numpy.mean(age5)
		print numpy.mean(age6)
		print numpy.mean(age7)
		print numpy.mean(age8)
		print numpy.mean(age9)
		print numpy.mean(age10)
		print numpy.mean(age11)
		print numpy.mean(age12)
	count += 1
