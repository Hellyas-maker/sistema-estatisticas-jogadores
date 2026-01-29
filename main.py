dados = {}
gols = []
jogadores = []
while True:
    dados.clear()
    gols.clear()
    dados['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]}: '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(dados['Gols'])
    jogadores.append(dados.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while True:
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break
print('-=' * 30)
print(f'{"COD":<4}{"NOME":<10}{"GOLS":<10}{"TOTAL":>8}')
print('-' * 33)
for j, p in enumerate(jogadores):
    print(f'{j:<4}{p["Nome"]:<10}{str(p["Gols"]):<10}{p["Total"]:>8}')
print('-' * 33)
while True:
    jog = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if jog == 999:
        break
    if jog >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {jog}!')
    else:
        print(f'-- LEVANTAMENDO DO JOGADOR {jogadores[jog]["Nome"]:}')
        for p, g in enumerate(jogadores[jog]["Gols"]):
            print(f'      No jogo {p+1} fez {g} gols')
    print('-' * 33)
print('<< VOLTE SEMPRE >>')
