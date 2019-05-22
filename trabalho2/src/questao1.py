# Projeto 2 de Introducao ao Processamento de Imagens - UnB
# Questao 1
# Aluno: Bruno Takashi Tengan
# Matricula: 12/0167263

import cv2 as cv
import numpy as np

# Carrega a imagem que vamos utilizar e seu negativo.
orig = cv.imread("img/morf_test.png", cv.IMREAD_GRAYSCALE)
orig_n = cv.bitwise_not(orig)

# Binariza a imagem com o treshold baseado no histograma da imagem.
ret, bin_orig = cv.threshold(orig, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
cv.imwrite('img/resultados/questao1/bin_raw.png', bin_orig)

# Mostrar a binarizacao pura sem tratamentos.
cv.imshow('Original', orig)
cv.imshow('Binarização de Otsu', bin_orig)
cv.waitKey(0)
cv.destroyAllWindows()

# Cria a mascara a ser usada nas operacoes de abertura e fechamento.
mascara = cv.getStructuringElement(cv.MORPH_RECT,(7,7))		# Mascara quadrada.
#mascara = cv.getStructuringElement(cv.MORPH_ELLIPSE,(7,7))		# Mascara eliptica.

# Aplica um top-hat na versao negativada da imagem por conta da efetividade do top-hat.
abertura_n = cv.morphologyEx(orig_n, cv.MORPH_OPEN, mascara)
topHat = cv.bitwise_not(cv.subtract(orig_n, abertura_n))

# Aplica o bottom-hat na imagem original.
fechamento = cv.morphologyEx(orig, cv.MORPH_CLOSE, mascara)
bottomHat = cv.bitwise_not(cv.subtract(fechamento, orig))

'''
# Mostra os resultados do top-hat e bottom-hat.
cv.imshow('Original', orig)
cv.imshow('Top-hat', topHat)
cv.imshow('Bottom-hat', bottomHat)
#cv.imwrite('img/resultados/questao1/tophat_raw.png', topHat)
#cv.imwrite('img/resultados/questao1/bottomhat_raw.png', bottomHat)
cv.waitKey(0)
cv.destroyAllWindows()
'''

# Binarizacao do top-hat e bottom-hat.
ret, bin_topHat = cv.threshold(topHat, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
ret, bin_bottomHat = cv.threshold(bottomHat, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
cv.imwrite('img/resultados/questao1/bin_tophat_7r.png', bin_topHat)
cv.imwrite('img/resultados/questao1/bin_bottomhat_7r.png', bin_bottomHat)

# (Q1.1) Mostra os resultados do top-hat e bottom-hat binarizados e a diferenca entre seus resultados.
cv.imshow('Original', bin_orig)
cv.imshow('Top-hat', bin_topHat)
cv.imshow('Bottom-hat', bin_bottomHat)
cv.imshow('diferenca top - bottom', bin_topHat - bin_bottomHat)
cv.waitKey(0)
cv.destroyAllWindows()

# Passado um filtro de mediana para tentar sumir com o ruido de salt-pepper.
filtrado = cv.medianBlur(orig, 3)

'''
# Mostra imagem filtrada.
cv.imshow('Original', orig)
cv.imshow('Filtrado', filtrado)
#cv.imwrite('img/resultados/questao1/filtrado.png', filtrado)
cv.waitKey(0)
cv.destroyAllWindows()
'''

# Aplica o bottom-hat na imagem filtrada e binariza ela.
mascara = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
fechamentof = cv.morphologyEx(filtrado, cv.MORPH_CLOSE, mascara)
bottomHatf = cv.bitwise_not(cv.subtract(fechamentof, filtrado))
ret, bin_bottomHatf = cv.threshold(bottomHatf, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
cv.imwrite('img/resultados/questao1/bin_bottomhat_5rf.png', bin_bottomHatf)

# (Q1.3) Mostra resultado com o filtrado e não filtrado.
cv.imshow('Original', bin_orig)
cv.imshow('Bottom-hat filtrado', bin_bottomHatf)
cv.imshow('Bottom-hat', bin_bottomHat)
cv.waitKey(0)
cv.destroyAllWindows()

final = ~bin_bottomHat
finalf = ~bin_bottomHatf

# Para a imagem nao filtrada eh feito uma abertura e fechamento afim de remover o ruido e reconectar as descontinuidades.
mascara = cv.getStructuringElement(cv.MORPH_RECT,(2,2))
final = cv.morphologyEx(final, cv.MORPH_OPEN, mascara)
mascara = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
final = cv.morphologyEx(final, cv.MORPH_CLOSE, mascara)
final = ~final

# Para a imagem filtrada se faz apenas o fechamento para tentar fechar as descontinuidades dos numeros.
mascara = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
finalf = cv.morphologyEx(finalf, cv.MORPH_CLOSE, mascara)
finalf = ~finalf

cv.imwrite('img/resultados/questao1/final.png', final)
cv.imwrite('img/resultados/questao1/finalF.png', finalf)

# (Q1.4) Resultado final com tentativas de abertura e fechamento.
cv.imshow('Bottom-hat filtrado', bin_bottomHatf)
cv.imshow('Bottom-hat', bin_bottomHat)
cv.imshow('Final', final)
cv.imshow('Final filtrado', finalf)
cv.waitKey(0)
cv.destroyAllWindows()