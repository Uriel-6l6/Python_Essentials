class Error(Exception): #Herda excecão
    pass

class InputError(Error): #Herda Error
    def __init__(self, message):
        self.message = message

while True: #Executa repetitivamento o código
    try:
        x = int(input(' Entre com uma nota de 0 a 10: ')) #entre com um Letra
        print(x)
        if x > 10:
            raise InputError(' Nota não pode ser maior que 10 ')  #Força um Exceção/personalização
        elif x < 0:
            raise InputError(' Nota não pode ser menor que 0 ')
        break # se passar pela tratativa ele para o Loop
    except ValueError:
        print('Valor inválido. Deve-ser digitar um número!')
    except InputError as ex:
        print(ex)