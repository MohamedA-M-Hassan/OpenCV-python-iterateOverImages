import numpy as np
import cv2

import os
import re

directory = 'output/'

def sort_humanly( l ):
	""" Sort the given list in the way that humans expect.
	"""
	convert = lambda text: int(text) if text.isdigit() else text
	alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
	l.sort( key=alphanum_key )
	return l
files = sort_humanly(os.listdir(directory))

for file_name in files:
	name = directory + file_name
	img = cv2.imread(name, 0)
	
	cv2.imshow('frame',img)
	cv2.waitKey(0)


cv2.destroyAllWindows()