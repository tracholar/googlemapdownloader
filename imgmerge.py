# coding:utf-8
import  os, re
from PIL import Image
import numpy as np
from googlemap import *

n_X = len(range(L_x,R_x+imsize,imsize))
n_Y = len(range(T_y, B_y + imsize, imsize))

im_size = (n_X * imsize,n_Y * imsize)
im = Image.new("RGB",im_size)

for x in range(L_x,R_x+imsize,imsize):
	for y in range(T_y, B_y + imsize, imsize):
		long, lat = Pixel2Long(x, zoom), Pixel2Lat(y, zoom)
		im_name = 'map_%f_%f' % (lat,long)
		im_name = im_name.replace('.','') + '.png'
		
		I = Image.open(im_name)
		
		L = int((x - L_x)/imsize)
		T = int((y - T_y)/imsize) 
		im.paste(I,(L*imsize,T*imsize))
		
im.save('bigimg.bmp')
