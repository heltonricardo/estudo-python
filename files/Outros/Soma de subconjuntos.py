def somas(lista, alvo, parcial=[]):
    s = sum(parcial)
    if s == alvo: print('sum({}) = {}'.format(parcial, alvo))
    if s >= alvo: return
    for i in range(len(lista)):
        n = lista[i]
        sobra = lista[i+1:]
        somas(sobra, alvo, parcial+[n]) 

somas([3, 9 , 8 , 4 , 5 , 7 , 10], 15, [])
