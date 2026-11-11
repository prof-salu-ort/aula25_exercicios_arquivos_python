'''Crie um programa em Python que utilize a instrução with e o modo 'w' para criar um arquivo de texto chamado mensagem.txt. 
   Escreva três linhas de texto nele com mensagens motivacionais de sua escolha. Lembre-se de incluir a quebra de linha (\n) ao final de cada uma.'''

with(open('mensagem.txt', 'w')) as arquivo:
    arquivo.write('Forca guerreiro, nao desista.\n')
    arquivo.write('Se nao compila, revise o codigo.\n')
    arquivo.write('Agora so precisa rezar pra rodar o codigo.\n')
