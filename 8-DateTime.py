from datetime import date, time , datetime

# data_atual = date.today()
# print(data_atual.strftime('%d/%m/%y'))   #formata para padrão de data brasileiro
#
# data_atual = date.today()
# print(data_atual.strftime('%A %B %y')) #traz o dia da semana e o mês

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y  %H:%M:%S')) #conversão dos padrões requeiridos



def trabalhando_com_date():    #descomentar no main para rodar
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d - %m - %y')
    print(type(data_atual))
    print(data_atual_str)
    print(data_atual_str)

def trabalhando_com_time():  #descomentar mo main para rodar
    horario = time(hour=15, minute=18, second=30)
    print(horario)  #como time
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)    #como String
    print(type(horario_str))


if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()