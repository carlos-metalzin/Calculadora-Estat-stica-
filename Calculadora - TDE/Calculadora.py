'''
author: Carlos Augusto  Rodrigues de Oliveira
Orientadoras: Mariana Pojar & Eliane de Fátima Chinaglia
Redes sociais: @gustc_carlos / Email: uniecaoliveira@fei.edu.br
date: 07/26/2021
version: 3.1

Programa desenvolvido para utilização na analíse de dados dentro do Laboratório de Física I
e para introdução a linguagem de programação, podendo ter outras utilidades.

Instruções:
- Para utilizar o programa utilize o comando (run);
- O programa foi feito com o intuito de introduzir o usúario dentro da Programação,
assim é recomendado que efetue a leitura de toda a estrutura do código,
onde há outras instruções para alterações no funcionamento,
buscando o máximo contato do usúario com a linguagem Python;
- Lembre-se de dedicar o arquivo desse programa a uma pasta separada,
para que possa adicionar seus arquivos de dados com maior facilidade;

Qualquer dúvida entre em contato com o autor do projeto,
sugestões de melhoraria também são sempre bem vindas.
'''

#Importando as bibliotecas utilizadas

import numpy as np
import statistics as st
import pandas as pd


#Criando funções


def titulo(txt, type=1):
    '''
    Função para exibição de título estilizado
    :parameter txt: Título a ser exibido
    :parameter type: opção de estilo
    :return: exibição do título
    '''
    tam = len(txt)+4
    if type == 1:
        print('='*tam)
        print(f'  {txt.upper().strip()}')
        print('='*tam)
    elif type == 2:
        print('~' * tam)
        print(f'  {txt.upper().strip()}')
        print('~' * tam)


def create_statistics(list, r ):
    '''
    Lê uma lista e retorna com os dados estatísticos em um dicionário
    :parameter list: lista de dados a serem analisados
    :parameter r: resolução estatística
    :return: dicionário com respostas estatísticas
    '''
    list = np.array(list)
    IE = st.stdev(list) / (len(list) ** (1 / 2))
    IP = (IE ** 2 + (r/2) ** 2) ** (1 / 2)
    answer = {'N° de itens': len(list), 'Maior valor': max(list), 'Menor valor': min(list),
              'Média': list.mean(), 'Desvio padrão': st.stdev(list),
              'Incerteza estatística': IE, 'Incerteza Padrão': IP}
    print('='*45)
    cont = 0
    for x, y in answer.items():
        if cont == 0:
            print(f'{x:<21}', ' ' * 10, f'{y:>10}')
        else:
            '''
            Na linha abaixo é possível alterar o número de casas decimais exibidas:
            coloque o número desejado antes do (f)
            '''
            print(f'{x:<21}', ' '*10, f'{y:>10.4f}')
    print('='*45)


def read():
    '''
    Função para ler arquivo de dados externos.
    O Programa está configurado para ler apenas arquivos (.csv), nesta função é possivel alterar o tipo de arquivo lido;
    É importante ressaltar que o arquivo é funcional apenas para dados de, apenas,  uma dimensão.
    Observação: Para que o arquivo possa ser utilizado dentro do programa lembre-se de deixa-los na mesma pasta.
    :return: retorna uma lista com os valores do arquivo
    '''
    valores = []
    '''
    Na linha abaixo é possivel alterar o arquivo utilizado pelo programa, 
    para isso altere a informação dentro das aspas colocando o nome do arquivo que deseja,
    lembre-se de colocar a extensão do arquivo
    '''
    arquivo_de_dados = pd.read_csv('Apague essa mensagem e insira seu arquivo de dados', sep=';')
    '''
    Caso precise ler outros tipos de arquivo altere após o underscore (_) em ('pd.read_'), 
    para mais informações recomenda-se a leitura da documentação da biblioteca Pandas 
    '''
    for y in arquivo_de_dados:
        try:
            y = str(y).replace(',', '.')
            float(y)
        except:
            print()
        else:
            valores.append(float(y))
        for x in arquivo_de_dados[y]:
            try:
                x = str(x).replace(',', '.')
                float(x)
            except:
                print('O dado a seguir estava no seu arquivo de dados e foi ignorado por não ser um valor: ')
                print(x, ' = ', type(x))
                print('-' * 30)
            else:
                valores.append(float(x))
    return valores


#variaveis

dados = []

# Display para decisões

titulo('bem vindo a calculadora estatística')
print('[1] para inserir os dados manualmente\n'
      '[2] para ler arquivo de dados')
print('-'*30)
resposta = input('Insira a opção desejada: ')
while resposta not in '12':
    resposta = input('Não foi possivel ler sua opção\nTente novamente: ')
titulo('processando',type=2)

#Lendo os dados de maneira manual

if resposta == '1':
    contador = 0
    qnt = int(input('Quantos valores serão informados? '))
    while contador != qnt:
        contador += 1
        dados.append(float(input(f'{contador}° valor: ')))
    dados = np.array(dados)

#Respondendo o usuario

    titulo('calculando')
    create_statistics(dados, r=float(input('Qual a resolução do seu instrumento? ')))

#lendo os dados em arquivo externo

if resposta == '2':
    titulo('calculando')
    create_statistics(read(), r=float(input('Qual a resolução do seu instrumento? ')))
