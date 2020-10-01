varGlobal = 'Objeto global'

def texto():
    varLocal = 'Objeto local'
    print(varGlobal)
    print(varLocal)

print('=== PROCEDIMENTO texto() ===')
texto()

print('=== PROGRAMA PRINCIPAL ===')
print(varGlobal)
print(varLocal) # erro para demonstrar escopo

input()
