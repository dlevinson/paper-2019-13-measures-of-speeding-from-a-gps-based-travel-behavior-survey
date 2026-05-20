# compute t-test and average

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
		female = data[data['gender'] == 0]['speed_limit_compliance']
		male = data[data['gender'] == 1]['speed_limit_compliance']
		print filename + "1"
	else:
		data = pandas.read_csv(path +'/' +filename)
		add1 = data[data['gender'] == 0]['speed_limit_compliance']
		add2 = data[data['gender'] == 1]['speed_limit_compliance']
		female = pd.concat([female,add1])
		male = pd.concat([male,add2])
		print filename + "2"
	
	if count == 11:
		print stats.ttest_ind(female, male, equal_var = False)
		print numpy.mean(female)
		print numpy.mean(male)
	count += 1
