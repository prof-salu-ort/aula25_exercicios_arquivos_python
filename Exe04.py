'''
Utilizando o módulo csv (pesquisar) do Python, escreva um programa que:
Crie um arquivo chamado produtos.csv com um cabeçalho contendo Nome e Preço.
Adicione pelo menos três produtos fictícios e seus respectivos preços (ex: Teclado, Mouse, Monitor).
Em seguida, reabra o arquivo para leitura, utilize o csv.reader para percorrer as linhas e exiba cada linha formatada na tela.
'''

import csv

with(open('produtos.csv', 'w', newline='')) as arquivo:
    cabecalho = ['nome', 'preco']
    writer = csv.DictWriter(arquivo, fieldnames=cabecalho)
    writer.writeheader()
    dados = [
        {'nome' : 'teclado', 'preco' : 200},
        {'nome' : 'mouse', 'preco' : 100},
        {'nome' : 'monitor', 'preco' : 500}
    ]
    writer.writerows(dados)

with(open('produtos.csv', 'r')) as arquivo:
    dados = csv.reader(arquivo)
    for linha in dados:
        print(linha)