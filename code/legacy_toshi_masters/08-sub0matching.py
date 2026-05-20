import csv,os, numpy, math
from itertools import islice
import processing
import time

def matching():
	#load GIS map
	#--- 1 Load map layer
	InGIS = "/Users/toshiyokoo/Desktop/Buffer0318/10m_buffer.shp"
	vlayer = QgsVectorLayer(InGIS, "10m_buffer", "ogr")
	
	#--- 2 Confirm something is loaded and valid
	vlayer.isValid()

	#--- 3 Display the layer into QGIS
	QgsMapLayerRegistry.instance().addMapLayer(vlayer)
	
	#Part1
	#load GPS data
	#--- 2 Set file name here
	InFlnm1=filename
	#--- 3 Build file name an path for uri
	InFlPth1="file:///"+InDrPth1+InFlnm1
	#gps_File = open(InDrPth1 +InFlnm1,'rU')
	#gps_File.seek(0)
	#--- 4 Set import Sting here note only need to set x and y other come for free
	uri1 = InFlPth1+"?delimiter=%s&xField=%s&yField=%s" % (",", "GX", "GY")
	# "Longitude", "Latitude" -> "GX", "GY"
	#--- 5 Load point layer
	bh1 = QgsVectorLayer(uri1, InFlnm1, "delimitedtext")
	#--- 6 Confirm something is loaded and valid
	bh1.isValid()
	#--- 7 Set CRS
	bh1.setCrs(QgsCoordinateReferenceSystem(26915, QgsCoordinateReferenceSystem.EpsgCrsId))
	#4326: WGS84, 26915: NAD83/UTM zone 15N
	#--- 8 Display the layer into QGIS
	QgsMapLayerRegistry.instance().addMapLayer(bh1)
	#--- select by location
	processing.runalg("qgis:selectbylocation", vlayer, uri1, 0)
	#----save vector layer as csv (True: selected, False: all)
	cLayer = qgis.utils.iface.mapCanvas().layers()[1]
	gi1 = 'GIS1_'+InFlnm1
	gis1 = 'Users/toshiyokoo/Desktop/5536/'+gi1
	QgsVectorFileWriter.writeAsVectorFormat(cLayer, gis1, "CP1250", None, "CSV", True)
	global InDrPth2, gis1, InFlnm1
	#execute algorithm_sub1
	#remove intersection & missing link GPS data
	execfile('Users/toshiyokoo/Desktop/Matching/sub1_remove_intersect.py')
	#Part2
	#load GPS data
	#--- 1 Set file name here
	InFlnm2=InFlnm1
	#--- 2  Set pathname here
	#InDrPth2='Users/toshiyokoo/Desktop/5880/'
	#--- 3 Build file name an path for uri
	InFlPth2="file:///"+InDrPth2+InFlnm2
	#--- 4 Set import Sting here note only need to set x and y other come for free
	uri2 = InFlPth2+"?delimiter=%s&xField=%s&yField=%s" % (",", "GX", "GY")
	# "Longitude", "Latitude" -> "GX", "GY"
	#--- 5 Load point layer
	bh2 = QgsVectorLayer(uri2, InFlnm2, "delimitedtext")
	#--- 6 Confirm something is loaded and valid
	bh2.isValid()
	#--- 7 Set CRS
	bh2.setCrs(QgsCoordinateReferenceSystem(26915, QgsCoordinateReferenceSystem.EpsgCrsId))
	#4326: WGS84, 26915: NAD83/UTM zone 15N
	#--- 8 Display the layer into QGIS
	QgsMapLayerRegistry.instance().addMapLayer(bh2)
	#--- select by location
	processing.runalg("qgis:selectbylocation", vlayer, uri2, 0)
	#----save vector layer as csv (True: selected, False: all)
	cLayer = qgis.utils.iface.mapCanvas().layers()[2]
	gi2 = 'GIS2_'+filename
	gis2 = 'Users/toshiyokoo/Desktop/5536/'+gi2
	global gis2, InFlnm2
	QgsVectorFileWriter.writeAsVectorFormat(cLayer, gis2, "CP1250", None, "CSV", True)
	#execute algorithm_sub2
	# find nearlestlink between GPS point and GIS map
	# calculate minimum height
	# link nearlest(Streetname and Speedlimit)
	execfile('Users/toshiyokoo/Desktop/Matching/sub2_matching.py')
	#remove GPS layer
	QgsMapLayerRegistry.instance().removeMapLayer( bh1.id() )
	QgsMapLayerRegistry.instance().removeMapLayer( bh2.id() )
	QgsMapLayerRegistry.instance().removeMapLayer( vlayer.id() )
	#reset selected layer
	#cLayer.setSelectedFeatures([0])
	#--- 1 Set file name here
	InFlnm3=InFlnm2
	InDrPth3='/Users/toshiyokoo/Desktop/box/'+InFlnm3
	#move file
	os.rename(gis1, "/Users/toshiyokoo/Desktop/comp1/"+gi1)
	os.rename(gis2, "/Users/toshiyokoo/Desktop/comp1/"+gi2)
	os.rename(InDrPth3 , "/Users/toshiyokoo/Desktop/comp1/"+InFlnm3)
	#gps_File.close()

for filename in os.listdir(InDrPth1):
	#global filename, InFlnm2, gi1, gi2, gis1, gis2
	matching()

