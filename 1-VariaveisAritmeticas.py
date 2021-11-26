a = int(input(' Entre com o primeior valor: '))
b = int(input(' Entre com o segundo valor: '))

soma = a + b
subtracao  = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print('soma é igual a: ' + str(soma))  #forma de Concatenação com tipos diferentes não recomendada
print('a subtracao é igual a:' + str(subtracao))
print(' a multiplicacao é igual a:' + str(multiplicacao))
# forma de Concatenação recomendada
print('divisão é igual á: {}'.format(divisao))
print(resto)

# outra forma
print('Soma: {soma}. \nSubtração: {subtracao}.'
      f'\nMultiplicação:{multiplicacao}'
      f'\nDivisão: {divisao}'
      f'\nResto: {resto}'.format(
        soma=soma,
        subtracao=subtracao,
        resto= resto,
        multiplicacao=multiplicacao,
        divisao=divisao ))







