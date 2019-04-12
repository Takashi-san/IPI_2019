# Projeto 1 de Introducao ao Processamento de Imagens - UnB
# Questao 2
# Aluno: Bruno Takashi Tengan
# Matricula: 12/0167263

import cv2 as cv
import numpy as np

def bgr_to_gray(img):
	#output = img.astype(int).sum(axis=2)/3
	output = img[:,:,0].astype(int) + img[:,:,1].astype(int) + img[:,:,2].astype(int)
	output = output//3
	return output.astype(np.uint8)

MRGB = cv.imread("img/Mars.bmp")

MGray = bgr_to_gray(MRGB)

Mheq = cv.equalizeHist(MGray)


cv.imshow('ori', MRGB)
cv.imshow('hnd', MGray)
cv.imshow('heq', Mheq)
cv.waitKey(0)
cv.destroyAllWindows()
