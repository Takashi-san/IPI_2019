# Projeto 1 de Introducao ao Processamento de Imagens - UnB
# Questao 2
# Aluno: Bruno Takashi Tengan
# Matricula: 12/0167263

import cv2 as cv
import numpy as np

# Funcao que converte imagem bgr para grayscale.
def bgr_to_gray(img):
	output = img.astype(int).sum(axis=2)/3
	return output.astype(np.uint8)

# Abre imagem de Marte.
MRGB = cv.imread("img/Mars.bmp")

# Converte imagem para escala de cinza.
MGray = bgr_to_gray(MRGB)

# Equaliza o histograma da imagem em escala de cinza.
Mheq = cv.equalizeHist(MGray)

# 
path_to_victory = cv.cvtColor(Mheq, cv.COLOR_GRAY2BGR)

row = 260
col = 415
row_end = 815
col_end = 1000

while (row != row_end) and (col != col_end):
	dst = np.zeros(9, dtype=float)
	lum = np.zeros(9, dtype=int)
	short = np.zeros(3, dtype=int)
	k = 0
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			dst[k] = np.linalg.norm([row+i - row_end, col+j - col_end])
			lum[k] = Mheq[row+i, col+j]
			k += 1

	dst[4] = max(dst)
	lum[4] = max(lum)
	for i in range(3):
		short[i] = list(dst).index(min(dst))
		dst[short[i]] = max(dst) + 1
	
	for i in range(9):
		if i != short[0] and i != short[1] and i != short[2]:
			lum[i] = max(lum) + 1
	
	way = list(lum).index(min([lum[short[0]], lum[short[1]], lum[short[2]]]))

	k = 0
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			if k == way:
				row = row+i
				col = col+j
			k += 1

	path_to_victory[row, col] = [0, 0, 255]
	
cv.imwrite('img/path.png', path_to_victory)	
#cv.imshow('path', path_to_victory)
#cv.imshow('ori', MRGB)
#cv.imshow('hnd', MGray)
#cv.imshow('heq', Mheq)
cv.waitKey(0)
cv.destroyAllWindows()