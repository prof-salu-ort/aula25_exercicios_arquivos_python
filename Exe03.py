'''
Crie um script que abra o arquivo mensagem.txt utilizando o modo de adição ('a'). Adicione uma nova frase no final do arquivo que diga: 
"Persista sempre, o sucesso é uma jornada!". Em seguida, leia o arquivo inteiro com o método .read() e imprima o conteúdo atualizado.
'''

with(open('mensagem.txt', 'a')) as arquivo:
    arquivo.write('Persista sempre, o sucesso e uma jornada!\n')

with(open('mensagem.txt', 'r')) as arquivo:
    for linha in arquivo.readlines():
        print(linha, end='')
