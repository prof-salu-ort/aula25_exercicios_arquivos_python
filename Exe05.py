'''
Crie um dicionário em Python que armazene informações de um jogo (por exemplo: nome_jogador, nivel, pontos e uma lista de conquistas).
Utilize o módulo json (pesquisar) para salvar esse dicionário em um arquivo chamado save_game.json, utilizando indent=4 para garantir a 
legibilidade. Depois, abra novamente o arquivo save_game.json para ler os dados convertendo-os de volta para um dicionário Python e 
exiba o valor de uma das chaves na tela.
'''

import json

jogador = {
    'nome_jogador' : 'juca', 'nivel' : 25, 'pontos' : 1000, 'conquistas' : ['lvl 10', 'lvl 20']
}

with(open('save_game.json', 'w', newline='')) as arquivo:
    json.dump(jogador, arquivo)

with(open('save_game.json', 'r', newline='')) as arquivo:
    dados = json.load(arquivo)
    print(dados)