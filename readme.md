# Trabalho 1 Conjuntos - Resolução de Problemas de Natureza Discreta

## Descrição
Este projeto foi desenvolvido em Python como Trabalho Discente Efetivo, da disciplina de Resolução de Problemas de Natureza Discreta, do curso de Bacharel em Ciência da Computação, da Pontifícia Universidade Católica do Paraná, lecionada pelo professor Andrey Cabral Meira e tem como objetivo calcular automaticamente  operações entre conjuntos fornecidos através de um arquivo de texto

## Requisitos
Para o programa ser executado da maneira correta, o arquivo de texto que servirá como entrada no código deve seguir o seguinte padrão conforme está escrito no enunciado do trabalho: O programa irá receber como entrada um arquivo de texto (.txt) contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e terceira linhas conterão os elementos dos conjuntos separados por virgulas. Exemplos estão presentes no código em forma de comentário e no repositório (conjuntos.txt, conjuntos1.txt, conjuntos2.txt e conjuntos3.txt)

## Instrução de Execução
Para executar o programa você deve seguir os seguntes passos:
1. Baixe os arquivos e armazene-os na mesma pasta(TDE_Conjuntos.py e conjuntos.txt)
2. Você pode rodar o programa em qualquer IDE (VSCode, Replit, Pycharm, etc)
3. Selecione o arquivo de texto que deseja executar na linha 50 do código
```bash
50  with open("nomeDoArquivo.txt", "r") as txt: #Ler o arquivo txt
51      txt = txt.readlines() #Armazenar como string em uma variável
```
4. Execute o Programa

## Resultados Esperados
O programa visa atender à todos os requisitos fornecidos pelo enunciado do trabalho que está apresentado nas primeiras 46 linhas de cógido em forma de comentário.  

Dito isso, ao ser executado, o programa deve apresentar no terminal n linhas de saída, onde n é fornecido na primeira linha do arquivo de texto e devem estar formatadas conforme o enunciado.  
Exemplo de formatação: União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}.  

As operações devem ser realizadas da maneira correta, sendo a União os elementos que estão presentes nos dois conjuntos, sem repetição; a Interseção os elementos que os dois conjuntos têm em comum; a Diferença sendo os elementos que estão presentes no primeiro conjunto, mas não no segundo; e o Produto Cartesiano sendo a formação de pares ordenados formados pelos elementos do primeiro conjunto e segundo conjunto.  

Exemplos:  
União: conjunto 1 {7, L, 2, C4, 7}, conjunto 2 {1, 2, 3, 4}.Resultado: {7, L, 2, C4, 1, 3, 4}  
Interseção: conjunto 1 {1, 2, 3, 4, 5, 1}, conjunto 2 {4, 5, 1, 1}.Resultado: {4, 5, 1}  
Diferença: conjunto 1 {1, A, C, 34}, conjunto 2 {A, C, D, 23}.Resultado: {1, 34}  
Produto Cartesiano: conjunto 1 {5, 6, 7, 8}, conjunto 2 {7, 8, 9}.Resultado: {(5, 7), (5, 8), (5, 9), (6, 7), (6, 8), (6, 9), (7, 7), (7, 8), (7, 9), (8, 7), (8, 8), (8, 9)}