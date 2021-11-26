class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -=1


#Sessão comentada para utilizar classe em módulo (import)
# televisao = Televisao()
# print('Televisão está ligada: {}'.format(televisao.ligada))
# televisao.power()
# print('Televisão está ligada: {}'.format(televisao.ligada))
# televisao.power()
# print('Televisão está ligada: {}'.format(televisao.ligada))
# print('Canal: {}' .format(televisao.canal))
# televisao.power()
# print('Televisão está ligada: {}'.format(televisao.ligada))
# televisao.aumenta_canal()
# televisao.aumenta_canal()
# print('Canal: {}'.format(televisao.canal))
# televisao.diminui_canal()
# print('Canal: {}'.format(televisao.canal))

#outra forma utilizando o MAIN

if __name__ == '__main__': #excuta código identato apenas quando ele é chamado no prórprio arquivo

    televisao = Televisao()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    print('Canal: {}' .format(televisao.canal))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))