from __future__ import division
from urllib import urlopen
import numpy as np
import thread, os

def Long2Pixel(long, zoom):
	return int((long + 180) * (256<<zoom)/360)
def Pixel2Long(pix, zoom):
	return pix * 360 / (256<<zoom) - 180
def Lat2Pixel(lat, zoom):
	siny = np.sin(lat * np.pi / 180)
	y = np.log((1+siny)/(1-siny))
	return int((128<<zoom) * (1- y / (2*np.pi)))
def Pixel2Lat(pix, zoom):
	y = 2*np.pi*(1-pix/(128<<zoom))
	z = np.exp(y)
	siny = (z-1)/(z+1)
	return np.arcsin(siny) * 180 /np.pi
if __name__ == '__main__':
	center = [40.143957,94.6297456]
	zoom = 14
	x = Long2Pixel(center[1], zoom)
	x += 512
	y = Lat2Pixel(center[0], zoom)
	y += 512
	long = Pixel2Long(x,zoom)
	lat = Pixel2Lat(y, zoom)
	print '%f,%f' % (lat, center[1])