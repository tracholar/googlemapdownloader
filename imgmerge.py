# coding:utf-8
import  os, re
from PIL import Image
import numpy as np
import pickle
from googlemap import *

f = open('conf','rb')
x_range, y_range, dx, dy, L_x, T_y, R_x, B_y, zoom = pickle.load(f)
f.close()

n_X = len(x_range)
n_Y = len(y_range)

im_size = (n_X * dx,n_Y * dy)
im = Image.new("RGB",im_size)

for x in x_range:
	for y in y_range:
		long, lat = Pixel2Long(x, zoom), Pixel2Lat(y, zoom)
		im_name = 'map_%f_%f' % (lat,long)
		im_name = im_name.replace('.','') + '.png'
		
		try:
			I = Image.open(im_name)
			
			L = int((x - L_x)/dx)
			T = int((y - T_y)/dy) 
			im.paste(I,(L*dx,T*dy))
		except Exception:
			pass
im.save('bigimg.bmp')
