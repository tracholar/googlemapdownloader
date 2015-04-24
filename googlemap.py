# coding:utf-8

import urllib,urllib2
import numpy as np
import threading, os
from maps import *
import time
from optparse import OptionParser
import pickle


url = ''
# baidu map
# url = r'http://api.map.baidu.com/staticimage?center={long},{lat}&zoom=%d&width=%d&height=%d&copyright=1' % (zoom,imsize,imsize)
# center = [40.143957,94.6297456]

pos = []

def DownloadMap():
	while True:
		if len(pos)==0:
			return
		long,lat = pos.pop()
		mapurl = url.replace('{long}', '%f' % long).replace('{lat}', '%f' % lat)
		

		
		ext = '%f_%f' % (lat,long)
		ext = ext.replace('.','')
		fn = 'map_%s.png' % ext
		if os.path.exists(fn) and not options.clear:
			continue
		
		
		# mapurl = 'http://www.baidu.com'
		req = urllib2.Request(mapurl, headers=headers)
		img = urllib2.urlopen(req).read()
		
		
		f = open(fn,'wb')
		f.write(img)
		f.close()
		print lat,long
		
		if len(pos)==0:
			return
		time.sleep(15)
	
if __name__ == '__main__':
		
	parser = OptionParser()
	parser.add_option("-z", "--zoom", type="int", dest="zoom",
					  help="zoom", default=10)
	parser.add_option("-r", "--region", type="string", dest="region",
					  help="donwload region with(Left Top, Right Bottom). e.g 40.4,94.55,40.0,94.95", 
						default = "40.4,94.55,40.0,94.95")
	parser.add_option("-t", "--maptype", type="choice", dest="maptype",
					  help="map type", default="satellite", 
					  choices=["satellite","roadmap"])
	parser.add_option("-f",  action="store_true", dest="clear",
					  help="force download ignore the file have donwloaded.", default=False)

	(options, args) = parser.parse_args()
	imsize = 512
	zoom = options.zoom
	maptype = options.maptype
	
	url = r'https://maps.googleapis.com/maps/api/staticmap?center={lat},{long}&zoom=%d&size=%dx%d&maptype=%s&sensor=false' % (zoom,imsize,imsize,maptype)
	
	T_lat, L_long, B_lat, R_long = tuple([float(i) for i in options.region.split(',')])

	# L_long = 94.55
	# R_long = 94.95
	# T_lat = 40.4
	# B_lat = 40.0

	L_x = Long2Pixel(L_long, zoom)
	R_x = Long2Pixel(R_long, zoom)

	T_y = Lat2Pixel(T_lat, zoom)
	B_y = Lat2Pixel(B_lat, zoom)

	dx = imsize
	x_range = range(L_x,R_x+imsize/2,dx)
	dy = imsize - 35
	y_range = range(T_y, B_y + imsize/2, dy)

	# save config
	conf = (x_range, y_range, dx, dy, L_x, T_y, R_x, B_y, zoom)
	f = open('conf','wb')
	pickle.dump(conf, f)
	f.close()

	

	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	}

	
	for x in x_range:
		for y in y_range:
			long, lat = Pixel2Long(x, zoom), Pixel2Lat(y, zoom)
			pos.append((long,lat))
	
		
		
	
	for i in range(10):
		threading.Thread(target=DownloadMap).start()
		
		