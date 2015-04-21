# coding:utf-8
import  os, re
from PIL import Image
import numpy as np
from googlemap import *

n_X = len(x_range)
n_Y = len(y_range)

im_size = (n_X * dx,n_Y * dy)
im = Image.new("RGB",im_size)

for x in x_range:
	for y in y_range:
		long, lat = Pixel2Long(x, zoom), Pixel2Lat(y, zoom)
		im_name = 'map_%f_%f' % (lat,long)
		im_name = im_name.replace('.','') + '.png'
		
		I = Image.open(im_name)
		
		L = int((x - L_x)/dx)
		T = int((y - T_y)/dy) 
		im.paste(I,(L*dx,T*dy))
		
im.save('bigimg.bmp')
