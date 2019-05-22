# Projeto 2 de Introducao ao Processamento de Imagens - UnB
# Questao 2
# Aluno: Bruno Takashi Tengan
# Matricula: 12/0167263

import cv2 as cv
import numpy as np

# Carrega a imagem que vamos utilizar.
orig = cv.imread("img/moire.tif", cv.IMREAD_GRAYSCALE)