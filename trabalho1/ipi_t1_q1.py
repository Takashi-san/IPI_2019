import cv2 as cv
import numpy as np

def im_chscaledepth (img, bit_out, dim):
	if (len(img.shape) == 3):
		row, col, ch = img.shape
	else:
		row, col = img.shape
		#n_row = row*dim
		#n_col = col*dim
	period = int(256/2**bit_out)
	step = int(255//(2**bit_out-1))
	output = img.copy()
	output = (output//period)*step
	print(bit_out)

	cv.imshow('image', output)
	cv.waitKey(0)
	#cv.destroyAllWindows()

	return output



test1 = cv.imread("img/im1.jpg")
test2 = cv.imread("img/im1.jpg", cv.IMREAD_GRAYSCALE)

im_chscaledepth(test2,8,0)
im_chscaledepth(test2,7,0)
im_chscaledepth(test2,6,0)
im_chscaledepth(test2,5,0)
im_chscaledepth(test2,4,0)
im_chscaledepth(test2,3,0)
im_chscaledepth(test2,2,0)
im_chscaledepth(test2,1,0)
cv.destroyAllWindows()