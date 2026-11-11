'''
Escreva um programa que abra o arquivo mensagem.txt criado no exercício anterior no modo de leitura ('r'). 
Utilize a forma mais eficiente ensinada no material (iterando diretamente sobre o objeto do arquivo em um laço for) para 
exibir cada linha na tela precedida por um hífen e sem espaços em branco extras.
'''

with(open('mensagem.txt', 'r')) as arquivo:
    texto = arquivo.readlines()
    for linha in texto:
        print(f'- {linha}', end='')
        print(f'- {linha.strip()}')