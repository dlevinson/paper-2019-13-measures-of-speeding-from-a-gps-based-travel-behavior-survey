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
		am0 = data[data['hour'] == 0]['speed_limit_compliance']
		am1 = data[data['hour'] == 1]['speed_limit_compliance']
		am2 = data[data['hour'] == 2]['speed_limit_compliance']
		am3 = data[data['hour'] == 3]['speed_limit_compliance']
		am4 = data[data['hour'] == 4]['speed_limit_compliance']
		am5 = data[data['hour'] == 5]['speed_limit_compliance']
		am6 = data[data['hour'] == 6]['speed_limit_compliance']
		am7 = data[data['hour'] == 7]['speed_limit_compliance']
		am8 = data[data['hour'] == 8]['speed_limit_compliance']
		am9 = data[data['hour'] == 9]['speed_limit_compliance']
		am10 = data[data['hour'] == 10]['speed_limit_compliance']
		am11 = data[data['hour'] == 11]['speed_limit_compliance']
		pm12 = data[data['hour'] == 12]['speed_limit_compliance']
		pm1 = data[data['hour'] == 13]['speed_limit_compliance']
		pm2 = data[data['hour'] == 14]['speed_limit_compliance']
		pm3 = data[data['hour'] == 15]['speed_limit_compliance']
		pm4 = data[data['hour'] == 16]['speed_limit_compliance']
		pm5 = data[data['hour'] == 17]['speed_limit_compliance']
		pm6 = data[data['hour'] == 18]['speed_limit_compliance']
		pm7 = data[data['hour'] == 19]['speed_limit_compliance']
		pm8 = data[data['hour'] == 20]['speed_limit_compliance']
		pm9 = data[data['hour'] == 21]['speed_limit_compliance']
		pm10 = data[data['hour'] == 22]['speed_limit_compliance']
		pm11 = data[data['hour'] == 23]['speed_limit_compliance']
		print filename + "1"
	else:
		data = pandas.read_csv(path +'/' +filename)
		add0 = data[data['hour'] == 0]['speed_limit_compliance']
		add1 = data[data['hour'] == 1]['speed_limit_compliance']
		add2 = data[data['hour'] == 2]['speed_limit_compliance']
		add3 = data[data['hour'] == 3]['speed_limit_compliance']
		add4 = data[data['hour'] == 4]['speed_limit_compliance']
		add5 = data[data['hour'] == 5]['speed_limit_compliance']
		add6 = data[data['hour'] == 6]['speed_limit_compliance']
		add7 = data[data['hour'] == 7]['speed_limit_compliance']
		add8 = data[data['hour'] == 8]['speed_limit_compliance']
		add9 = data[data['hour'] == 9]['speed_limit_compliance']
		add10 = data[data['hour'] == 10]['speed_limit_compliance']
		add11 = data[data['hour'] == 11]['speed_limit_compliance']
		pdd12 = data[data['hour'] == 12]['speed_limit_compliance']
		pdd1 = data[data['hour'] == 13]['speed_limit_compliance']
		pdd2 = data[data['hour'] == 14]['speed_limit_compliance']
		pdd3 = data[data['hour'] == 15]['speed_limit_compliance']
		pdd4 = data[data['hour'] == 16]['speed_limit_compliance']
		pdd5 = data[data['hour'] == 17]['speed_limit_compliance']
		pdd6 = data[data['hour'] == 18]['speed_limit_compliance']
		pdd7 = data[data['hour'] == 19]['speed_limit_compliance']
		pdd8 = data[data['hour'] == 20]['speed_limit_compliance']
		pdd9 = data[data['hour'] == 21]['speed_limit_compliance']
		pdd10 = data[data['hour'] == 22]['speed_limit_compliance']
		pdd11 = data[data['hour'] == 23]['speed_limit_compliance']
		am0 = pd.concat([am0,add0])
		am1 = pd.concat([am1,add1])
		am2 = pd.concat([am2,add2])
		am3 = pd.concat([am3,add3])
		am4 = pd.concat([am4,add4])
		am5 = pd.concat([am5,add5])
		am6 = pd.concat([am6,add6])
		am7 = pd.concat([am7,add7])
		am8 = pd.concat([am8,add8])
		am9 = pd.concat([am9,add9])
		am10 = pd.concat([am10,add10])
		am11 = pd.concat([am11,add11])
		pm12 = pd.concat([pm12,pdd12])
		pm1 = pd.concat([pm1,pdd1])
		pm2 = pd.concat([pm2,pdd2])
		pm3 = pd.concat([pm3,pdd3])
		pm4 = pd.concat([pm4,pdd4])
		pm5 = pd.concat([pm5,pdd5])
		pm6 = pd.concat([pm6,pdd6])
		pm7 = pd.concat([pm7,pdd7])
		pm8 = pd.concat([pm8,pdd8])
		pm9 = pd.concat([pm9,pdd9])
		pm10 = pd.concat([pm10,pdd10])
		pm11 = pd.concat([pm11,pdd11])
		print filename + "2"
	if count == 11:
		print "am4, am7", stats.ttest_ind(am4,am7, equal_var = False)
		print "pm12, pm2", stats.ttest_ind(pm12,pm2, equal_var = False)
		print numpy.mean(am0)
		print numpy.mean(am1)
		print numpy.mean(am2)
		print numpy.mean(am3)
		print numpy.mean(am4)
		print numpy.mean(am5)
		print numpy.mean(am6)
		print numpy.mean(am7)
		print numpy.mean(am8)
		print numpy.mean(am9)
		print numpy.mean(am10)
		print numpy.mean(am11)
		print numpy.mean(pm12)
		print numpy.mean(pm1)
		print numpy.mean(pm2)
		print numpy.mean(pm3)
		print numpy.mean(pm4)
		print numpy.mean(pm5)
		print numpy.mean(pm6)
		print numpy.mean(pm7)
		print numpy.mean(pm8)
		print numpy.mean(pm9)
		print numpy.mean(pm10)
		print numpy.mean(pm11)
	count += 1
