# a = int(input (' Primeiro valor: '))
# b = int(input(' Segundo valor: '))
# c = int(input(' Terceiro valor: '))
#
# if a > b and a > c:
#     print(' O maior número é {}'.format(a))
#
# elif b > a and b > c:
#     print(' O maior número é {}'.format(b))
#
# else:
#     print(' O maior número é {}'.format(c))
#
# print(' Final do programa')

#-----------------------------------------------------------

# a = int(input(' Entre com o primeiro valor: '))
# b = int(input(' Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = a % 2
# if resto_a == 0 or resto_b == 0:
#     print(' foi digitado um número par ')
# else:
#     print(' Nenhum número par foi digitado ')

#-----------------------------------------------------------

a = int(input(' Informe a nota  do Primeiro bimestre: '))
if a > 10:
    a = int(input(' Dado inválido, Digita novamente de 0 á 10:'))
b = int(input(' Informe a nota do Segundo bimestre: '))
if b > 10:
    b = int(input(' Dado inválido, Digita novamente de 0 á 10:'))
c = int(input(' Informe a nota do Terceiro bimestre: '))
if c > 10:
    c = int(input(' Dado inválido, Digita novamente de 0 á 10:'))
d = int(input(' Informe a nota  do Quarto bimestre: '))
if d > 10:
    d = int(input(' Dado inválido, Digita novamente de 0 á 10:'))

media = (a + b + c + d) / 4
print(' Média: {}'.format(media))

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print(' média: {} ' .format(media))
# else:
#     print(' Foi informado alguma nota errada')

