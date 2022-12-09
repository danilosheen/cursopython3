# Exercício - sistema de perguntas e respostas
import os
import time

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

errou = "\u274C"
acertou = "\u2705"
acertos = 0

for i in range(len(perguntas)):
    questao = list(perguntas[i].values())
    pergunta = questao[0]
    alternativas = questao[1]
    #verifica índice da alternativa correta
    for r in range(len(alternativas)):
        resposta_teste = alternativas[r]
        if resposta_teste == questao[2]:
            resposta = str(r)
    #resposta = questao[2]
    print(pergunta)
    for j in range(len(alternativas)):
        print(f'{j}) - {alternativas[j]}')

    resposta_user = input('Informe a alternativa: ')
    if resposta_user != resposta:
        print(f'você errou {errou}')
        time.sleep(2)
        os.system('clear')

    else:
        print(f'Parabéns! você acertou {acertou}\n')
        acertos += 1
        time.sleep(2)
        os.system('clear')

print(f'Você acertou {acertos} de {len(perguntas)} questões')
    