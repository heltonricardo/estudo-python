jog = {}
jog['nome'] =     input('Nome.....................: ')
jog['qntp'] = int(input('Partidas jogadas.........: '))
gol = []
for i in range(jog['qntp']):
    gol.append(int(input(f'Quantos gols na partida {i+1}? ')))
jog['gols'] = gol[:]
jog['totl'] = sum(gol)
print(f'O jogador {jog["nome"]} jogou {jog["qntp"]} partida(s).')
for p, g in enumerate(jog['gols']): print(f'Na partida {p+1} fez {g} gol(s).')
print(f'Total de gols: {jog["totl"]}.')
