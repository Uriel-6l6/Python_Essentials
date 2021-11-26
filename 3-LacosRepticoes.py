#WHILE

nota = int(input('Entre com a nota'))
while nota > 10:
    nota = int(input('Entre com um nota de 0 á 10'))

# a = 0
# while a <= 10:
#     print(a)
#     a += 1


#todos os numeros primos de 0 á 100 (FOR)
# for num in range(101):
#     div = 0
#     for x in range (1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div = div + 1
#     if div == 2:
#         print (num)
#

# achando números primos (números que só se devidem por eles mesmo ou por 1) (FOR)
# a = int(input(' entre com um número: '))
# div = 0
# for x in range (1, a + 1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div = div + 1
# if div == 2:
#     print (' número {} é primo:'.format(a))
# else:
#     print('número {} não é primo'.format(a))
