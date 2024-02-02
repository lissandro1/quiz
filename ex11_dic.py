txt = ' Quiz '
print(f'{txt:#^14}')

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

qtd_acertos = 0
for pergunta in perguntas:
    print(f'Pergunta: {pergunta['Pergunta']}')
    print()

    print('Opções:')
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    
    escolha = input('Escolha uma opção: ')
    acertou = False
    escolha_int = None
    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < len(opcoes):
            if opcoes[escolha_int] == pergunta["Resposta"]:
                acertou = True
    if acertou:
        print('Você acertou!')
        qtd_acertos += 1
    else:
        print('Você errou!')

    print()

print(f'Você acertou {qtd_acertos} resposta(s) de {len(perguntas)} perguntas.')

    





