n = input('Digite algo: ')
print('O tipo da entrada é {}'.format(type(n)))
print('É alfanumérico?  ', n.isalnum())
print('É alfabético?    ', n.isalpha())
print('É decimal?       ', n.isdecimal())
print('É dígito?        ', n.isdigit())
print('É identificador? ', n.isidentifier())
print('É minúsculo?     ', n.islower())
print('É numérico?      ', n.isnumeric())
print('É printável?     ', n.isprintable())
print('É espaço?        ', n.isspace())
print('É título?        ', n.istitle())
print('É maiúsculo?     ', n.isupper())