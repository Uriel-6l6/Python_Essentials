lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'hamster']

# print (lista_animal [1])
#
# lista_animal.remove('gato')
#
# if 'gato' in lista_animal:
#     print('existe um gato na lista')
# else:
#     print('não existe um gato na lista, mas á um lobo')
#     lista_animal.append('lobo')
#     print(lista_animal)
#
# lista_animal.pop(1)
# print(lista_animal)
#
# print(sum(lista))
# print(max(lista))
# print(min(lista))
# print(max(lista_animal)


#tuplas

tupla = (1, 10, 12, 14) #tupla é um lista imutável
print(len(tupla)) #cotagem de quantos valores tem na tupla
print(len(lista_animal))
tupla_animal = tuple(lista_animal) #conversão de lista para tupla
print(tupla_animal)

lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)