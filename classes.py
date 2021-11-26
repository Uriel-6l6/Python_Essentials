#classe (Sempre com letra maiuscula)

class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2
    def soma (self):  # função (tudo aquilo que tem retorno)
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao (self):
        return self.a / self.b

if __name__ == '__main__':

    calculadora = Calculadora (10, 2) # istanciar classe
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())


#outra forma
# class Calculadora:
#     def soma (self,valor_a,valor_b):
#         return valor_a + valor_b
#
#     def subtracao(self,valor_a,valor_b):
#         return valor_a - valor_b
#
#     def multiplicacao(self,valor_a,valor_b):
#         return valor_a * valor_b
#
#     def divisao (self,valor_a,valor_b):
#         return valor_a / valor_b
#
# calculadora = Calculadora () # istanciar classe
# print(calculadora.soma(10,2))
# print(calculadora.subtracao(5,3))
# print(calculadora.multiplicacao(10,5))
# print(calculadora.divisao(100,2))





    # print(soma(1, 2))
    # print(subtracao(10,2))
    # print(multiplicacao(25,150))
    # print(divisao(5,15))
