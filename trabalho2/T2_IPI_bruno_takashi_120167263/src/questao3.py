# Projeto 2 de Introducao ao Processamento de Imagens - UnB
# Questao 3
# Aluno: Bruno Takashi Tengan
# Matricula: 12/0167263

import cv2 as cv
import numpy as np

# Carrega a imagem que vamos utilizar.
cookie = cv.imread("img/cookies.tif", cv.IMREAD_GRAYSCALE)
cv.imwrite('img/resultados/questao3/cookies.png', cookie)

# Binariza a imagem de acordo com um threshold determinado experimentalmente.
ret, binario = cv.threshold(cookie, 55, 255, cv.THRESH_BINARY)
cv.imwrite('img/resultados/questao3/bin_raw.png', binario)

# Realiza operacoes morfologicas de abertura e fechamento pra remover elementos indesejados.
mascara = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
binario = cv.morphologyEx(binario, cv.MORPH_OPEN, mascara)
binario = cv.morphologyEx(binario, cv.MORPH_CLOSE, mascara)
cv.imwrite('img/resultados/questao3/bin_openclose.png', binario)

# Transformada hit-or-miss
mini = binario[8:161, 9:156]		# Obtem formato da regiao que queremos pra usar de mascara.
binario1 = cv.erode(binario, mini)
binario2 = cv.dilate(binario, ~mini)
binario = cv.subtract(binario1, binario2)
cv.imwrite('img/resultados/questao3/bin_hitormiss.png', binario)
cv.imwrite('img/resultados/questao3/mascara.png', mini)

# Dilatação com o resultado do hit-or-miss e realizado a remocao do biscoito da imagem original com a mascara obtida.
binario = cv.dilate(binario, mini)
cv.imwrite('img/resultados/questao3/cookie_mascara.png', binario)

nbinario = cookie & ~binario
binario = cookie & binario

cv.imwrite('img/resultados/questao3/cookie.png', binario)
cv.imwrite('img/resultados/questao3/cookie_inv.png', nbinario)

cv.imshow('cookies', cookie)
cv.imshow('masked', binario)
cv.imshow('~masked', nbinario)
cv.imshow('mascara', mini)
cv.waitKey(0)
cv.destroyAllWindows()