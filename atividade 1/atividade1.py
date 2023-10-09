import cv2
import numpy as np

def salvar_imagem(matriz, nome_arquivo, formato='png'):
    """
    Salva uma matriz como uma imagem com o nome fornecido e o formato especificado.

    Args:
        matriz: Uma matriz que representa a imagem a ser salva.
        nome_arquivo: O nome do arquivo a ser salvo.
        formato: O formato do arquivo a ser salvo. O padrão é 'png'.

    Returns:
        None
    """
    # Converter a matriz em uma imagem com OpenCV
    imagem = cv2.convertScaleAbs(matriz)

    # Salvar a imagem com o nome fornecido e o formato especificado
    nome_com_extensao = f"{nome_arquivo}.{formato}"
    cv2.imwrite(nome_com_extensao, imagem)

#Criar uma matriz para um triangulo
altura, largura = 500, 500
triangulo = np.zeros((altura, largura), dtype=np.uint8)
vertices = np.array([[250, 100], [100, 400], [400, 400]])
cv2.fillPoly(triangulo, [vertices], 255)

#Criar uma matriz para um circulo
altura, largura = 500, 500
circulo = np.zeros((altura, largura), dtype=np.uint8)
raio = 200
centro = (250,250)
cv2.circle(circulo, centro, raio, 255, -1)

#Criar uma matriz para um quadrado
altura, largura = 500, 500
quadrado = np.zeros((altura, largura), dtype=np.uint8)
cv2.rectangle(quadrado, (100, 100), (400, 400), 255, -1)


#Salvar as imagens
salvar_imagem(triangulo, "triangulo")
salvar_imagem(circulo, "circulo")
salvar_imagem(quadrado, "quadrado")