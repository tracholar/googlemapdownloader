# coding:utf-8

import urllib,urllib2
import numpy as np
import threading, os
from maps import *
import time

imsize = 512
zoom = 14
url = r'https://maps.googleapis.com/maps/api/staticmap?center={center}&zoom=%d&size=%dx%d&maptype=roadmap&sensor=false' % (zoom,imsize,imsize)

center = [40.143957,94.6297456]


L_long = 94.55
R_long = 94.95
T_lat = 40.4
B_lat = 40.0

L_x = Long2Pixel(L_long, zoom)
R_x = Long2Pixel(R_long, zoom)

T_y = Lat2Pixel(T_lat, zoom)
B_y = Lat2Pixel(B_lat, zoom)

dx = imsize
x_range = range(L_x,R_x+imsize,dx)
dy = imsize - 35
y_range = range(T_y, B_y + imsize, dy)
pos = []

def DownloadMap():
	# print 'df'
	while True:
		if len(pos)==0:
			return
		long,lat = pos.pop()
		mapurl = url.replace('{center}', '%f,%f' % (lat,long))
		ext = '%f_%f' % (lat,long)
		ext = ext.replace('.','')
		fn = 'map_%s.png' % ext
		if os.path.exists(fn):
			continue
		
		img = urllib.urlopen(mapurl).read()
		
		
		f = open(fn,'wb')
		f.write(img)
		f.close()
		print lat,long
		time.sleep(10)
	
if __name__ == '__main__':
	
	
	for x in x_range:
		for y in y_range:
			long, lat = Pixel2Long(x, zoom), Pixel2Lat(y, zoom)
			pos.append((long,lat))
	
		
		
	
	for i in range(10):
		threading.Thread(target=DownloadMap).start()
		
		