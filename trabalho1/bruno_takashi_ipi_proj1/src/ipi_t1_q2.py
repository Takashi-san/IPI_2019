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

# Abre imagem de Marte. OBS: colocar o diretorio correto da imagem aqui.
MRGB = cv.imread("img/Mars.bmp")

# Converte imagem para escala de cinza.
MGray = bgr_to_gray(MRGB)

# Equaliza o histograma da imagem em escala de cinza.
Mheq = cv.equalizeHist(MGray)

# Imagem para guardar a rota.
path_to_victory = cv.cvtColor(Mheq, cv.COLOR_GRAY2BGR)

# Setar valor de posicao de partida e posicao de chegada.
row = 260
col = 415
row_end = 815
col_end = 1000

# Algoritmo para percorrer o caminho.
while (row != row_end) and (col != col_end):
	# Variaveis para guardar a distancia e luminosidade das posicoes adjacentes.
	dst = np.zeros(9, dtype=float)
	lum = np.zeros(9, dtype=int)
	# Variavel para guardar as 3 posicoes de menor distancia com a chegada.
	short = np.zeros(3, dtype=int)
	
	# Obtem distancia e luminosidade das posicoes adjacentes.
	k = 0
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			dst[k] = np.linalg.norm([row+i - row_end, col+j - col_end])
			lum[k] = Mheq[row+i, col+j]
			k += 1

	# Ignora os valores da posicao em que esta.
	dst[4] = max(dst) + 1
	lum[4] = max(lum) + 1

	# Obtem as 3 posicoes de menor distancia com a chegada.
	for i in range(3):
		short[i] = list(dst).index(min(dst))
		# Ignora esta posicao ja selecionada da selecao.
		dst[short[i]] = max(dst) + 1
	
	# Ignora todas as posicoes que nao sao as 3 posicoes de menor distancia.
	for i in range(9):
		if i != short[0] and i != short[1] and i != short[2]:
			lum[i] = max(lum) + 1
	
	# Pega a posicao com menor luminosidade dentre as 3 selecionadas. Se existir valores iguais, tem prioridade a posicao de menor numeracao.
	way = list(lum).index(min([lum[short[0]], lum[short[1]], lum[short[2]]]))

	# Anda a posicao escolhida.
	k = 0
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			if k == way:
				row = row+i
				col = col+j
			k += 1

	# Registra o passo feito.
	path_to_victory[row, col] = [0, 0, 255]

# FIM ALGORITMO ======================================================================================================

#cv.imwrite('img/pathHeq.png', path_to_victory)	
#cv.imshow('path', path_to_victory)
#cv.imshow('MRGB', MRGB)
#cv.imshow('MGray', MGray)
#cv.imshow('Mheq', Mheq)

#cv.waitKey(0)
#cv.destroyAllWindows()
