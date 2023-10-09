# Atividade 1 
## Objetivos
- Criar uma classe própria para salvar imagens.
- Gerar pelo menos 3 imagens.

## Execução
- Criação das matrizes
  - Utilização da biblioteca numpy para criação das cordenadas das figuras(circulo, quadrado e triângulo) através dos métodos 'np.zeros' e 'np.array'.
  - Para finalizar a composição das matrizes nas determinadas figuras utilizou-se a biblioteca opencv através dos metodos 'cv2.circle', 'cv2.rectangle' e 'cv2.fillPoly'.
 
- Função para salvar imagens
  - Recebe 3 parâmetros : matriz, nome do arquivo e formato do arquivo.
  - Atráves do método 'cv2.convertScaleAbs' converte a matriz em uma imagem.
  - Com o método 'cv2.imWrite' salva a imagem com o nome e formato solicitado.
 
## Documentação
- A documentação foi gerada através da ferramenta Sphinx.
- Está disponivel no diretório './documentacao/_build/html/index.html'. Basta fazer download do projeto e executar o arquivo index.html para vizualização da página da documentação.




