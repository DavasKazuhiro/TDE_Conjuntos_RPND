#Davi Kazuhiro Natume

#ENUNCIADO:
#   Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
#linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
#operações que serão realizadas entre dois conjuntos de dados.
#    O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
#contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
#em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
#segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
#operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
#seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
#operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
#terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
#das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
#   4
#   U
#   3, 5, 67, 7
#   1, 2, 3, 4
#   I
#   1, 2, 3, 4, 5
#   4, 5
#   D
#   1, A, C, 34
#   A, C, D, 23
#   C
#   3, 4, 5, 5, A, B, R
#   1, B, C, D, 1
#   Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
#produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
#{𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
#   A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
#dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
#a informação e a formatação mostrada a seguir:
#   União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
#   Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
#um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
#de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
#minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
#   No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
#pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
#implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.
#   Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
#contendo um número diferente de operações, operações com dados diferentes, e operações em ordem
#diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no
#ambiente repl.it quanto no ambiente Github.
#   Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com,
#no mínimo um arquivo de testes criado pelo próprio professor.

with open("conjuntos3.txt", "r") as txt: #Ler o arquivo txt
    txt = txt.readlines() #Armazenar como string em uma variável

qtd = int(txt[0]) #Armazena o valor da primeira linha como variável

def selecionarOperacoes(txt):
    operacoes = [] #Cria um vetor para armazenar o tipo de operação
    for i in range(len(txt)):
        if (i + 2) % 3 == 0: #Verifica se a linha representa uma operação
            operacoes.append(txt[i]) #Adiciona a a string da operação no vetor ('O\n')
    return operacoes

def formatarConjuntos(txt):
    conjuntos = [] #Cria a matriz para armazenar os conjuntos onde uma linha contém dois conjuntos
    for i in range(len(txt)):
        conjunto =[] #Cria o vetor para armazenar os conjuntos
        if (i + 1) % 3 == 0: #Verifica se a linha apresenta o primeiro conjunto da operação
            for j in range(2): #Laço de repetição com range 2 para pegar os dois conjuntos da operação
                vetor = [] #Vetor para armazenar um conjunto
                linha = txt[i + j] #Variável que representa qual conjunto vai ser selecionado 
                virgula1 = 0 #Armazena o índice de referência da primeira virgula (começo do valor)
                for k in range(linha.count(',') + 1): #Laço de repetição para a quantidade de itens de cada conjunto
                    virgula2 = linha.find(',', virgula1) #Variável que armazena o local da próxima virgula (final do valor)
                    if virgula2 == -1: #Função para solucionar o problema do ultimo valor da ultima linha
                        virgula2 = len(linha)
                    vetor.append(linha[virgula1:virgula2].strip()) #Armazena no vetor o valor entre as duas virgulas(dado) (.strip remove \n e espaços)
                    virgula1 = virgula2 + 1 #Muda o ponto de referência do primeiro valor
                conjunto.append(vetor) #Armazena o conjunto em uma linha
            conjuntos.append(conjunto) #Armazena a linha na matriz
    return conjuntos

#FORMATO DA MATRIZ conjuntos:
#[[['3', '5', '67', '7'] -> vetor, ['1', '2', '3', '4']] -> conjunto,
#[['1', '2', '3', '4', '5'], ['4', '5']],
#[['1', 'A', 'C', '34'], ['A', 'C', 'D', '23']],
#[['3', '4', '5', '5', 'A', 'B', 'R'], ['1', 'B', 'C', 'D', '1']]] -> conjuntos,

def calcular(conjuntos, operacoes):
    resultados = [] #Vetor para armazenar o resultado das operações
    for i in range(qtd): #Laço de repetição de quantidade de operações
        resultado = [] #Cria o vetor para armazenar um resultado
        if 'U' in operacoes[i]:
            for j in range(2): #Laço de repetição para percorrer os dois conjuntos
                for k in range(len(conjuntos[i][j])): #Laço de repetição para percorrer todos os itens do conjunto
                    if conjuntos[i][j][k] not in resultado: #Verifica se o valor já foi armazenado
                        resultado.append(conjuntos[i][j][k]) #Armazena o valor
            resultados.append(resultado) #Armazena um resultado no vetor

        elif 'I' in operacoes[i]:
            if conjuntos[i][0] > conjuntos[i][1]: #Verifica qual dos dois conjuntos é maior
                m = 0 #m indica o indice do conjunto maior
                n = 1 #n indica o indice do conjunto menor
            else:
                m = 1
                n = 0
            for j in range(len(conjuntos[i][m])): #Percorre todos os valores do conjunto maior
                if conjuntos[i][m][j] in conjuntos[i][n] and conjuntos[i][m][j] not in resultado: #Verifica se o valor está presente nos dois conjuntos
                    resultado.append(conjuntos[i][m][j]) #Adiciona o valor no vetor
            resultados.append(resultado) #Armazena um resultado no vetor

        elif 'D' in operacoes[i]:
            for j in range(len(conjuntos[i][0])): #Percorre todos os valores no primeiro conjunto
                if conjuntos[i][0][j] not in conjuntos[i][1]: #Verifica quais valores não estão presentes no segundo conjunto
                    resultado.append(conjuntos[i][0][j])
            resultados.append(resultado)

        elif 'C' in operacoes[i]:
            for j in range(len(conjuntos[i][0])): #Percorre todos os valores no primeiro conjunto
                for k in range(len(conjuntos[i][1])): #Percorre todos os valores no segundo conjunto
                    r = f'({conjuntos[i][0][j]}, {conjuntos[i][1][k]})' #Junta o valor do primeiro com o segundo
                    if r not in resultado: #Verifica se o valor já foi adicionado
                        resultado.append(r)
            resultados.append(resultado)
    return resultados

def imprimirResultados(conjuntos, resultados):
    for i in range(qtd):
        conjunto1 = str(conjuntos[i][0]) #Transforma o primeiro conjunto em uma string
        conjunto1 = conjunto1.replace('[', '{') #substitui os valores para a formatação correta
        conjunto1 = conjunto1.replace(']', '}')
        conjunto1 = conjunto1.replace("'", '')

        conjunto2 = str(conjuntos[i][1])
        conjunto2 = conjunto2.replace('[', '{')
        conjunto2 = conjunto2.replace("'", '')
        conjunto2 = conjunto2.replace(']', '}')

        resultado = str(resultados[i])
        resultado = resultado.replace('[', '{')
        resultado = resultado.replace("'", '')
        resultado = resultado.replace(']', '}')
        if 'U' in operacoes[i]:
            print(f'União: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}') #Imprime os valores na formatação correta

        elif 'I' in operacoes[i]:
            print(f'Interseção: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}')

        elif 'D' in operacoes[i]:
            
            print(f'Diferença: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}')

        elif 'C' in operacoes[i]:
            print(f'Produto Cartesiano: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}')

operacoes = selecionarOperacoes(txt)
conjuntos = formatarConjuntos(txt)
resultados = calcular(conjuntos, operacoes)
imprimirResultados(conjuntos, resultados)