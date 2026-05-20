import csv,os, numpy, math
from itertools import islice
import datetime

title = ['PersonID', 'TripID', 'LinkID', 'Hour', 'streetlength', 'Speedlimit', 'degree', 'percentage', 'speed_25', 'speed_30', 'speed_35', 'speed_40', 'speed_45', 'speed_50', 'speed_55', 'speed_60', 'speed_65', 'morning', 'afternoon', 'night', 'o_gender', 'o_edu', 'o_age', 'gender', 'education_1', 'education_2', 'age_25_to_34', 'age_35_to_44', 'age_45_to_54', 'age_55_to_64', 'age_65_to_74', 'age_75_to_84', 'age_85_and_over', 'person1', 'person2', 'person3', 'person4', 'person5', 'person6', 'person7', 'person8', 'person9', 'person10', 'person11', 'person12', 'person13', 'person14', 'person15', 'person16', 'person17', 'person18', 'person19', 'person20', 'person21', 'person22', 'person23', 'person24', 'person25', 'person26', 'person27', 'person28', 'person29', 'person30', 'person31', 'person32', 'person33', 'person34', 'person35', 'person36', 'person37', 'person38', 'person39', 'person40', 'person41', 'person42', 'person43', 'person44', 'person45', 'person46', 'person47', 'person48', 'person49', 'person50', 'person51', 'person52', 'person53', 'person54', 'person55', 'person56', 'person57', 'person58', 'person59', 'person60', 'person61', 'person62', 'person63', 'person64', 'person65', 'person66', 'person67', 'person68', 'person69', 'person70', 'person71', 'person72', 'person73', 'person74', 'person75', 'person76', 'person77', 'person78', 'person79', 'person80', 'person81', 'person82', 'person83', 'person84', 'person85', 'person86', 'person87', 'person88', 'person89', 'person90', 'person91', 'person92', 'person93', 'person94', 'person95', 'person96', 'person97', 'person98', 'person99', 'person100', 'person101', 'person102', 'person103', 'person104', 'person105', 'person106', 'person107', 'person108', 'person109', 'person110', 'person111', 'person112', 'person113', 'person114', 'person115', 'person116', 'person117', 'person118', 'person119', 'person120', 'person121', 'person122', 'person123', 'person124', 'person125', 'person126', 'person127', 'person128', 'person129', 'person130', 'person131', 'person132', 'person133', 'person134', 'person135', 'person136', 'person137', 'person138', 'person139', 'person140', 'person141', 'person142', 'person143', 'person144', 'person145', 'person146', 'person147', 'person148', 'person149', 'person150', 'person151']

def summarize():
	inputFile = open(path +'/' +filename,'rU')
	reader = csv.reader(inputFile)
	inputFile.seek(0)
	root_path = '/Users/toshiyokoo/Desktop/15_result'
	outputFile = open(os.path.join(root_path,"summary_15")+'.csv','a')
	writer = csv.writer(outputFile, lineterminator='\n')
	print >> outputFile, ','.join(title)
	for row in islice(reader, 1, None):
		list = []
		personid = str(row[0])
		person = int(row[0])
		tripid = str(row[1])
		linkid = str(row[2])
		hour = str(row[3])
		streetlength = str(row[4])
		speedlimit = str(row[5])
		degree = str(row[6])
		percentage = str(row[7])
		speed_25 = str(row[8])
		speed_30 = str(row[9])
		speed_35 = str(row[10])
		speed_40 = str(row[11])
		speed_45 = str(row[12])
		speed_50 = str(row[13])
		speed_55 = str(row[14])
		speed_60 = str(row[15])
		speed_65 = str(row[16])
		morning = str(row[17])
		afternoon = str(row[18])
		night = str(row[19])
		o_gender = str(row[20])
		o_education = str(row[21])
		o_age = str(row[22])
		gender = str(row[23])
		education_1 = str(row[24])
		education_2 = str(row[25])
		age_25_to_34 = str(row[26])
		age_35_to_44 = str(row[27])
		age_45_to_54 = str(row[28])
		age_55_to_64 = str(row[29])
		age_65_to_74 = str(row[30])
		age_75_to_84 = str(row[31])
		age_85_and_over = str(row[32])
			
		#person
		person1 = 0
		person2 = 0
		person3 = 0
		person4 = 0
		person5 = 0
		person6 = 0
		person7 = 0
		person8 = 0
		person9 = 0
		person10 = 0
		person11 = 0
		person12 = 0
		person13 = 0
		person14 = 0
		person15 = 0
		person16 = 0
		person17 = 0
		person18 = 0
		person19 = 0
		person20 = 0
		person21 = 0
		person22 = 0
		person23 = 0
		person24 = 0
		person25 = 0
		person26 = 0
		person27 = 0
		person28 = 0
		person29 = 0
		person30 = 0
		person31 = 0
		person32 = 0
		person33 = 0
		person34 = 0
		person35 = 0
		person36 = 0
		person37 = 0
		person38 = 0
		person39 = 0
		person40 = 0
		person41 = 0
		person42 = 0
		person43 = 0
		person44 = 0
		person45 = 0
		person46 = 0
		person47 = 0
		person48 = 0
		person49 = 0
		person50 = 0
		person51 = 0
		person52 = 0
		person53 = 0
		person54 = 0
		person55 = 0
		person56 = 0
		person57 = 0
		person58 = 0
		person59 = 0
		person60 = 0
		person61 = 0
		person62 = 0
		person63 = 0
		person64 = 0
		person65 = 0
		person66 = 0
		person67 = 0
		person68 = 0
		person69 = 0
		person70 = 0
		person71 = 0
		person72 = 0
		person73 = 0
		person74 = 0
		person75 = 0
		person76 = 0
		person77 = 0
		person78 = 0
		person79 = 0
		person80 = 0
		person81 = 0
		person82 = 0
		person83 = 0
		person84 = 0
		person85 = 0
		person86 = 0
		person87 = 0
		person88 = 0
		person89 = 0
		person90 = 0
		person91 = 0
		person92 = 0
		person93 = 0
		person94 = 0
		person95 = 0
		person96 = 0
		person97 = 0
		person98 = 0
		person99 = 0
		person100 = 0
		person101 = 0
		person102 = 0
		person103 = 0
		person104 = 0
		person105 = 0
		person106 = 0
		person107 = 0
		person108 = 0
		person109 = 0
		person110 = 0
		person111 = 0
		person112 = 0
		person113 = 0
		person114 = 0
		person115 = 0
		person116 = 0
		person117 = 0
		person118 = 0
		person119 = 0
		person120 = 0
		person121 = 0
		person122 = 0
		person123 = 0
		person124 = 0
		person125 = 0
		person126 = 0
		person127 = 0
		person128 = 0
		person129 = 0
		person130 = 0
		person131 = 0
		person132 = 0
		person133 = 0
		person134 = 0
		person135 = 0
		person136 = 0
		person137 = 0
		person138 = 0
		person139 = 0
		person140 = 0
		person141 = 0
		person142 = 0
		person143 = 0
		person144 = 0
		person145 = 0
		person146 = 0
		person147 = 0
		person148 = 0
		person149 = 0
		person150 = 0
		person151 = 0
		#person152 = 0
		
		#if person == 1013360102:
		#	person1 = 1
		#elif person == 1022380102:
		#	person2 = 1
				
		#Input personID data
		PersonFile = open("/Users/toshiyokoo/Desktop/5133/Persondata.csv",'rU')
		idlist = csv.reader(PersonFile)
		PersonFile.seek(0)
		for dem in islice(idlist, 0, None):
			if person == int(dem[0]):
				person1 = 1
			elif person == int(dem[1]):
				person2 = 1
			elif person == int(dem[2]):
				person3 = 1
			elif person == int(dem[3]):
				person4 = 1
			elif person == int(dem[4]):
				person5 = 1
			elif person == int(dem[5]):
				person6 = 1
			elif person == int(dem[6]):
				person7 = 1
			elif person == int(dem[7]):
				person8 = 1
			elif person == int(dem[8]):
				person9 = 1
			elif person == int(dem[9]):
				person10 = 1
			elif person == int(dem[10]):
				person11 = 1
			elif person == int(dem[11]):
				person12 = 1
			elif person == int(dem[12]):
				person13 = 1
			elif person == int(dem[13]):
				person14 = 1
			elif person == int(dem[14]):
				person15 = 1
			elif person == int(dem[15]):
				person16 = 1
			elif person == int(dem[16]):
				person17 = 1
			elif person == int(dem[17]):
				person18 = 1
			elif person == int(dem[18]):
				person19 = 1	
			elif person == int(dem[19]):
				person20 = 1
			elif person == int(dem[20]):
				person21 = 1
			elif person == int(dem[21]):
				person22 = 1
			elif person == int(dem[22]):
				person23 = 1
			elif person == int(dem[23]):
				person24 = 1
			elif person == int(dem[24]):
				person25 = 1
			elif person == int(dem[25]):
				person26 = 1
			elif person == int(dem[26]):
				person27 = 1
			elif person == int(dem[27]):
				person28 = 1
			elif person == int(dem[28]):
				person29 = 1	
			elif person == int(dem[29]):
				person30 = 1
			elif person == int(dem[30]):
				person31 = 1
			elif person == int(dem[31]):
				person32 = 1
			elif person == int(dem[32]):
				person33 = 1
			elif person == int(dem[33]):
				person34 = 1
			elif person == int(dem[34]):
				person35 = 1
			elif person == int(dem[35]):
				person36 = 1
			elif person == int(dem[36]):
				person37 = 1
			elif person == int(dem[37]):
				person38 = 1
			elif person == int(dem[38]):
				person39 = 1	
			elif person == int(dem[39]):
				person40 = 1
			elif person == int(dem[40]):
				person41 = 1
			elif person == int(dem[41]):
				person42 = 1
			elif person == int(dem[42]):
				person43 = 1
			elif person == int(dem[43]):
				person44 = 1
			elif person == int(dem[44]):
				person45 = 1
			elif person == int(dem[45]):
				person46 = 1
			elif person == int(dem[46]):
				person47 = 1
			elif person == int(dem[47]):
				person48 = 1
			elif person == int(dem[48]):
				person49 = 1	
			elif person == int(dem[49]):
				person50 = 1
			elif person == int(dem[50]):
				person51 = 1
			elif person == int(dem[51]):
				person52 = 1
			elif person == int(dem[52]):
				person53 = 1
			elif person == int(dem[53]):
				person54 = 1
			elif person == int(dem[54]):
				person55 = 1
			elif person == int(dem[55]):
				person56 = 1
			elif person == int(dem[56]):
				person57 = 1
			elif person == int(dem[57]):
				person58 = 1
			elif person == int(dem[58]):
				person59 = 1	
			elif person == int(dem[59]):
				person60 = 1
			elif person == int(dem[60]):
				person61 = 1
			elif person == int(dem[61]):
				person62 = 1
			elif person == int(dem[62]):
				person63 = 1
			elif person == int(dem[63]):
				person64 = 1
			elif person == int(dem[64]):
				person65 = 1
			elif person == int(dem[65]):
				person66 = 1
			elif person == int(dem[66]):
				person67 = 1
			elif person == int(dem[67]):
				person68 = 1
			elif person == int(dem[68]):
				person69 = 1	
			elif person == int(dem[69]):
				person70 = 1
			elif person == int(dem[70]):
				person71 = 1
			elif person == int(dem[71]):
				person72 = 1
			elif person == int(dem[72]):
				person73 = 1
			elif person == int(dem[73]):
				person74 = 1
			elif person == int(dem[74]):
				person75 = 1
			elif person == int(dem[75]):
				person76 = 1
			elif person == int(dem[76]):
				person77 = 1
			elif person == int(dem[77]):
				person78 = 1
			elif person == int(dem[78]):
				person79 = 1	
			elif person == int(dem[79]):
				person80 = 1
			elif person == int(dem[80]):
				person81 = 1
			elif person == int(dem[81]):
				person82 = 1
			elif person == int(dem[82]):
				person83 = 1
			elif person == int(dem[83]):
				person84 = 1
			elif person == int(dem[84]):
				person85 = 1
			elif person == int(dem[85]):
				person86 = 1
			elif person == int(dem[86]):
				person87 = 1
			elif person == int(dem[87]):
				person88 = 1
			elif person == int(dem[88]):
				person89 = 1	
			elif person == int(dem[89]):
				person90 = 1
			elif person == int(dem[90]):
				person91 = 1
			elif person == int(dem[91]):
				person92 = 1
			elif person == int(dem[92]):
				person93 = 1
			elif person == int(dem[93]):
				person94 = 1
			elif person == int(dem[94]):
				person95 = 1
			elif person == int(dem[95]):
				person96 = 1
			elif person == int(dem[96]):
				person97 = 1
			elif person == int(dem[97]):
				person98 = 1
			elif person == int(dem[98]):
				person99 = 1	
			elif person == int(dem[99]):
				person100 = 1
			elif person == int(dem[100]):
				person101 = 1
			elif person == int(dem[101]):
				person102 = 1
			elif person == int(dem[102]):
				person103 = 1
			elif person == int(dem[103]):
				person104 = 1
			elif person == int(dem[104]):
				person105 = 1
			elif person == int(dem[105]):
				person106 = 1
			elif person == int(dem[106]):
				person107 = 1
			elif person == int(dem[107]):
				person108 = 1
			elif person == int(dem[108]):
				person109 = 1	
			elif person == int(dem[109]):
				person110 = 1
			elif person == int(dem[110]):
				person111 = 1
			elif person == int(dem[111]):
				person112 = 1
			elif person == int(dem[112]):
				person113 = 1
			elif person == int(dem[113]):
				person114 = 1
			elif person == int(dem[114]):
				person115 = 1
			elif person == int(dem[115]):
				person116 = 1
			elif person == int(dem[116]):
				person117 = 1
			elif person == int(dem[117]):
				person118 = 1
			elif person == int(dem[118]):
				person119 = 1	
			elif person == int(dem[119]):
				person120 = 1
			elif person == int(dem[120]):
				person121 = 1
			elif person == int(dem[121]):
				person122 = 1
			elif person == int(dem[122]):
				person123 = 1
			elif person == int(dem[123]):
				person124 = 1
			elif person == int(dem[124]):
				person125 = 1
			elif person == int(dem[125]):
				person126 = 1
			elif person == int(dem[126]):
				person127 = 1
			elif person == int(dem[127]):
				person128 = 1
			elif person == int(dem[128]):
				person129 = 1	
			elif person == int(dem[129]):
				person130 = 1
			elif person == int(dem[130]):
				person131 = 1
			elif person == int(dem[131]):
				person132 = 1
			elif person == int(dem[132]):
				person133 = 1
			elif person == int(dem[133]):
				person134 = 1
			elif person == int(dem[134]):
				person135 = 1
			elif person == int(dem[135]):
				person136 = 1
			elif person == int(dem[136]):
				person137 = 1
			elif person == int(dem[137]):
				person138 = 1
			elif person == int(dem[138]):
				person139 = 1
			elif person == int(dem[139]):
				person140 = 1
			elif person == int(dem[140]):
				person141 = 1
			elif person == int(dem[141]):
				person142 = 1
			elif person == int(dem[142]):
				person143 = 1
			elif person == int(dem[143]):
				person144 = 1
			elif person == int(dem[144]):
				person145 = 1
			elif person == int(dem[145]):
				person146 = 1
			elif person == int(dem[146]):
				person147 = 1
			elif person == int(dem[147]):
				person148 = 1
			elif person == int(dem[148]):
				person149 = 1
			elif person == int(dem[149]):
				person150 = 1
			elif person == int(dem[150]):
				person151 = 1
			#elif person == int(dem[151]):
			#	person152 = 1

		
		list.extend([personid, tripid, linkid, hour, streetlength, speedlimit, degree, percentage, speed_25, speed_30, speed_35, speed_40, speed_45, speed_50, speed_55, speed_60, speed_65, morning, afternoon, night, o_gender, o_education, o_age, gender, education_1, education_2, age_25_to_34, age_35_to_44, age_45_to_54, age_55_to_64, age_65_to_74, age_75_to_84, age_85_and_over, person1, person2, person3, person4, person5, person6, person7, person8, person9, person10, person11, person12, person13, person14, person15, person16, person17, person18, person19, person20, person21, person22, person23, person24, person25, person26, person27, person28, person29, person30, person31, person32, person33, person34, person35, person36, person37, person38, person39, person40, person41, person42, person43, person44, person45, person46, person47, person48, person49, person50, person51, person52, person53, person54, person55, person56, person57, person58, person59, person60, person61, person62, person63, person64, person65, person66, person67, person68, person69, person70, person71, person72, person73, person74, person75, person76, person77, person78, person79, person80, person81, person82, person83, person84, person85, person86, person87, person88, person89, person90, person91, person92, person93, person94, person95, person96, person97, person98, person99, person100, person101, person102, person103, person104, person105, person106, person107, person108, person109, person110, person111, person112, person113, person114, person115, person116, person117, person118, person119, person120, person121, person122, person123, person124, person125, person126, person127, person128, person129, person130, person131, person132, person133, person134, person135, person136, person137, person138, person139, person140, person141, person142, person143, person144, person145, person146, person147, person148, person149, person150, person151])
		writer.writerow(list)
	inputFile.close()
	print filename

path = "/Users/toshiyokoo/Desktop/aaafm"
for filename in os.listdir(path):
	global filename
	summarize()
