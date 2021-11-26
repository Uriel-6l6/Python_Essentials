lista = [1, 10]
try:
    #divisão = 10 /0 #forçando erros
    #numero = lista[3]
    x = a
except ZeroDivisionError:
    print(' Não é possível realiar um divisão por Zero! ')

except IndexError:
    print(' Error ao acessar um indice inválido da lista ')

except BaseException as ex: #base padrão de erros usando variavel ex para mostrar o erro
    print(' Erro desconhecido. ERROR: {} '.format(ex))

else:
    print(' Executa quando não ocorre exceção ')

finally:
    print(' Sempre Executa ')
