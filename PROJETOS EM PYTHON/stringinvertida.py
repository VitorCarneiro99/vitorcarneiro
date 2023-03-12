
string = input('Digite uma string para inverter: ')


lista = []
for char in string:
    lista.append(char)


i = 0
j = len(lista) - 1
while i < j:
    temp = lista[i]
    lista[i] = lista[j]
    lista[j] = temp
    i += 1
    j -= 1

string_invertida = ''
for char in lista:
    string_invertida += char

print('A string invertida é:', string_invertida)