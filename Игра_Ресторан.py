from itertools import product
import random, webbrowser


database_menu = {
    'ЛОБСТЕР В ЧЕСНОЧНОМ СОУСЕ': '6300 руб.',
    'КОНФИ ИЗ УТКИ (CONFIT DE CANARD)': '3000 руб.',
    'ГАЛЕТЫ (GALETTE)': '600 руб.',
    'ШУКРУТ (CHOUCROUTE)': '400 руб.',
    'ФУА ГРА (FOIE GRAS)': '4000 руб.',
    'ЭСКАРГО ИЛИ БУРГУНДСКИЕ УЛИТКИ (ESCARGOTS DE BOURGOGNE)': '5000 руб.',
    "ЛУКОВЫЙ СУП (SOUPE A L'OIGNON)": '800 руб.'
}

def process_menu():
    print(f'Прошу Вас ознакомиться с нашим меню. \n')
    for key, value in database_menu.items():
        print(key, ':', value)
    print(f'\n')
    database_menu_list = list(database_menu.keys())
    print(f'Какое блюдо Вы готовы сегодня отведать? \n')
    for dish in database_menu_list:
        dish = input()
        if dish == 'ЛОБСТЕР В ЧЕСНОЧНОМ СОУСЕ':
            print(f'{name},Ваш заказ {dish} принят! Приятного вечера:=)')
        elif dish == 'КОНФИ ИЗ УТКИ (CONFIT DE CANARD)':
            print(f'{name}, Ваш заказ {dish} принят! Приятного вечера:=)')
        elif dish == 'ГАЛЕТЫ (GALETTE)':
            print(f'{name}, Ваш заказ {dish} принят! Приятного вечера:=)')
        elif dish == 'ШУКРУТ (CHOUCROUTE)':
            print(f'{name}, Ваш заказ {dish} принят! Приятного вечера:=)')
        elif dish == 'ФУА ГРА (FOIE GRAS)':
            print(f'{name}, Ваш заказ {dish} принят! Приятного вечера:=)')
        elif dish == 'ЭСКАРГО ИЛИ БУРГУНДСКИЕ УЛИТКИ (ESCARGOTS DE BOURGOGNE)':
            print(f'{name}, Ваш заказ {dish} принят! Приятного вечера:=)')
        elif dish == "ЛУКОВЫЙ СУП (SOUPE A L'OIGNON)":
            print(f'{name}, Ваш заказ {dish} принят! Приятного вечера:=)')
        raise SystemExit()

def reserved_name():
    print(f'Прошу пройти за мной Василий и Климентина. Ваш столик на 19:30 уже готов! \n')
    process_menu()

def input_name():
    print(f'На какое имя Вы бронировали столик? \n')
    global name
    name = input()
    if name =='Василий':
        reserved_name()
    elif name == 'Тарас':
        print(f'{name}, после прошлой драки с битьем посуды вход в наш ресторан вам запрещен!!! \n')
        raise SystemExit()
    elif name == 'МС Початок':
        print(f'О, Великий {name}! Для Вас у нас эксклюзивное предложение и VIP места! \n')
        raise SystemExit()
    else:
        print(f'{name}, Вас нет в списке и кажется, что сегодня вечером у нас все столики заняты:=( \n')
        bakhshish()

def bakhshish():
    money = int(input(f'*{name}, Сколько вы готовы дать метродотелю на чай?* \n'))
    if money:
        print(f"""{name}, Прошу прощения, мне сообщили, что один столик может освободиться через сорок минут, 
                          но я мог бы для вас еще, что-то придумать:=) \n""")
    else:
        print(f'Всего хорошего, {name}. Дверь находится позади Вас!')
        raise SystemExit(0)

    print(f'*Молодой человек ищет мелочь по карманам*')
    money_man = [int(s) for s in input().split()]
    print(f'*Девушка ищет мелочь по карманам*')
    money_woman = [int(i) for i in input().split()]

    for s, i in product(money_man, money_woman):
        if s + i == 250:
            print(f'Очень хорошо,{name}, прошу вас пройти за мной! \n')
            process_menu()

    for s, i in product(money_man, money_woman):
        if s + i != 250:
            print(f'Всего хорошего, {name}. Дверь находится позади Вас!')
            raise SystemExit()


def metrodotel():
    print(f'\n')
    print('Добрый вечер, Господа! У Вас был забронирован столик? \n')
    reserved = input()
    if reserved == 'Да':
        input_name()
    elif reserved == 'Нет':
        print(f'Как я могу к Вам обращаться? \n')
        global name
        name = input()
        print(f'{name}, Кажется, что сегодня вечером у нас все столики заняты:=( \n')
        bakhshish()

def process_welcome():
    print('Добро пожаловать в Шато-де-Перекуси! \n')
    print('Позвольте измерить Вашу температуру. У нас действуют антикоронавирусные меры. \n')
    t = round(random.uniform(36.6, 38.0),1)
    if t >= 36.6 and t <= 37.5:
        print(f'Ваша температруа {t} градусов. Кажется, что Вы еще здоровы. Вас проводит наш метродотель.')
        metrodotel()
    elif t >= 37.6 and t <= 38.0:
        print(f'Ваша температруа {t} градусов. Вы явно нездоровы и мы просим Вас покинуть наш ресторан.')
        raise SystemExit()

def kartinka():
    webbrowser.open(r'C:\Users\AD\Desktop\питон2021\restoran\shateu_de_perekusi.jpg')


def main():
    kartinka()
    process_welcome()


if __name__ == "__main__":
	main()