# Projeto 1 de Introducao ao Processamento de Imagens - UnB
# Questao 1
# Aluno: Bruno Takashi Tengan
# Matricula: 12/0167263

import cv2 as cv
import numpy as np

# im_chscaledepth (img, bit_out, dim)
# INPUT:
#	img = Matriz da imagem obtida ao abrir a imagem com o OpenCV.
#	bit_out = Quantidade de bit que a imagem de saida vai ter para sua intensidade/cor. 
#		Valores: 1 <= bit_out <= 8.
#	dim = Fator de redimensionamento da imagem. 
#		Valores: 0 < dim.
#
# OUTPUT:
#	output = Matriz de imagem do OpenCV.

def im_chscaledepth (img, bit_out, dim):
	output = img.copy() # Copiando a imagem original para uma variavel de saida.

	# Pega informacoes do tamanho da imagem dependendo se eh em bgr ou grayscale.
	if (len(img.shape) == 3):
		# BGR.
		row, col, ch = img.shape
	else:
		# GRAYSCALE.
		row, col = img.shape

	# Calcula diferenca de pixels entre a nova dimensao e a original.
	dif_row = abs(row - int(row*dim))
	dif_col = abs(col - int(col*dim))

	# Se for uma reducao da dimensao da imagem, a realiza agora.
	if (dim < 1 and dim > 0 and (dif_row != 0 or dif_col != 0)):
		# Calcula o intervalo de remocao de linhas e colunas.
		period_row = row/dif_row
		period_col = col/dif_col
		k = 0
		i = 0
		# Remove linhas da imagem de acordo com o intervalo de linhas.
		while i < row:
			output = np.delete(output, int(i)-k, 0)
			k += 1
			i += period_row
		k = 0
		i = 0
		# Remove colunas da imagem de acordo com o intervalo de colunas.
		while i < col:
			output = np.delete(output, int(i)-k, 1)
			k += 1
			i += period_col

	# Realiza a conversao do nivel de brilho/cor.
	period = int(256/2**bit_out)
	step = int(255//(2**bit_out-1))
	output = (output//period)*step

	# Se for aumento da dimensao da imagem, o realiza agora.
	if (dim > 1 and (dif_row != 0 or dif_col != 0)):
		# Calcula o intervalo de adicao de linhas e colunas.
		period_row = row/dif_row
		period_col = col/dif_col
		# Imagem bgr ou grayscale.
		if (len(img.shape) == 3):
			# BGR.
			k = 0
			i = 0
			# Adiciona linhas na imagem de acordo com o intervalo de linhas.
			while i < row:
				output = np.insert(output, int(i)+k, output[int(i)+k,:,:], axis=0)
				k += 1
				i += period_row
			k = 0
			i = 0
			# Adiciona colunas na imagem de acordo com o intervalo de colunas.
			while i < col:
				output = np.insert(output, int(i)+k, output[:,int(i)+k,:], axis=1)
				k += 1
				i += period_col
		else:
			# GRAYSCALE.
			k = 0
			i = 0
			# Adiciona linhas na imagem de acordo com o intervalo de linhas.
			while i < row:
				output = np.insert(output, int(i)+k, output[int(i)+k,:], axis=0)
				k += 1
				i += period_row
			k = 0
			i = 0
			# Adiciona colunas na imagem de acordo com o intervalo de colunas.
			while i < col:
				output = np.insert(output, int(i)+k, output[:,int(i)+k], axis=1)
				k += 1
				i += period_col

	return output
# FIM im_chscaledepth (img, bit_out, dim) =========================================================================