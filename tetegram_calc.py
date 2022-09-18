import telebot
import emoji


bot = telebot.TeleBot('5592292280:AAGa5atz2PtjzK-wiYh1JL4_-FSMper_-7Y')
@bot.message_handler(commands=['help'])
def print_menu(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=f'Привет, {msg.from_user.full_name}.\nЯ - бот-калькулятор.\U0001F9EE\nЯ умею производить 4 арифметических действия над двумя числами.\nЧисла могут быть целыми или дробными.\n Наберите "/start" и следуйте указаниям ')

@bot.message_handler(commands=['start'])
def print_menu(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=f'Бот - калькулятор приветсвует Вас, {msg.from_user.full_name}! \U0001F91D')
    bot.send_message(chat_id=msg.from_user.id, text='Выберите, с какими числами будем работать? \n 1. Целые числа \n 2. Дробные числа')
    bot.send_message(chat_id=msg.from_user.id, text='Введите 1 или 2:')
    bot.register_next_step_handler(msg, take_type_numbers)


type_of_numbers = ''
type_of_operation = ''
print_operation = ''


def take_type_numbers(msg: telebot.types.Message):
    if msg.text in {'1', '2'}:
        global type_of_numbers
        type_of_numbers = int(msg.text)
        bot.send_message(chat_id=msg.from_user.id, text='Выберите арифметическое действие: " + - * / "')
        bot.register_next_step_handler(msg, take_type_operation)
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка. Введите 1 или 2 \U0001F64F')
        bot.register_next_step_handler(msg, take_type_numbers)


def take_type_operation(msg: telebot.types.Message):
    if msg.text in {'+': 1, '-': 2, '*': 3, '/': 4}:
        global type_of_operation
        type_of_operation = {'+': 1, '-': 2, '*': 3, '/': 4}[msg.text]
        if type_of_numbers == 1:
            bot.send_message(chat_id=msg.from_user.id, text='Введите 2 целых числа через пробел:')
            bot.register_next_step_handler(msg, take_numbers_i)
        else:
            bot.send_message(chat_id=msg.from_user.id, text='Введите 2 дробных числа через пробел (0 вводить нельзя!):')
            bot.register_next_step_handler(msg, take_numbers_f)
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка. Введите арифметическое действие " + - * / " \U0001F64F')
        bot.register_next_step_handler(msg, take_type_operation)


def check(vhod):
    new_chislo = []
    vhod = vhod.replace(',','.').replace(' ','') #заменяем на точки и убиарем пробелы
    koef = ''
    tochka = 0
    tire = 0
    for i in vhod:
        if i == '-':
            if tire:
                return None
            koef = '-'
            tire += 1
        elif i.isdigit():
            new_chislo.append(koef + i)
            if koef == '-':
                koef = ''
        elif i == '.':
            tochka += 1
            if tochka < 2:
                new_chislo.append(i)
            else:
                break
        else:
            return None
    chislo = ''.join(new_chislo)
    if chislo != '':
        return float(chislo)
    else:
        return None


def take_numbers_i(msg: telebot.types.Message):
    tmp = msg.text.split()
    if len(tmp) == 2 and tmp[0].isdigit() and tmp[1].isdigit():
        if division(msg):
            res = calcul(int(tmp[0]), int(tmp[1]), type_of_operation)
            bot.send_message(chat_id=msg.from_user.id, text=f'{print_operation} {res}')
            bot.send_message(chat_id=msg.from_user.id, text='Для продолжения введите любой символ')
            bot.register_next_step_handler(msg, take_message)
        else:
            bot.send_message(chat_id=msg.from_user.id, text=f'Деление на 0 не поддерживается, вызывайте помощь \U0001F691')
            bot.send_message(chat_id=msg.from_user.id, text='Для продолжения введите любой символ')
            bot.register_next_step_handler(msg, take_message)
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка. Введите 2 целых числа через пробел: \U0001F64F')
        bot.register_next_step_handler(msg, take_numbers_i)


def take_numbers_f(msg: telebot.types.Message):
    tmp = msg.text.split()
    if len(tmp) == 2:
        tmp1 = check(tmp[0])
        tmp2 = check(tmp[1])
        if tmp1 and tmp2:
            res = calcul(tmp1, tmp2, type_of_operation)
            bot.send_message(chat_id=msg.from_user.id, text=f'{print_operation} {res}')
            bot.send_message(chat_id=msg.from_user.id, text=f'Для продолжения введите любой символ')
            bot.register_next_step_handler(msg, take_message)
        else:
            bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка. Введите два дробных числа через пробел: \U0001F64F')
            bot.register_next_step_handler(msg, take_numbers_f)
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка. Введите два дробных числа через пробел (0 вводить нельзя!): \U0001F64F')
        bot.register_next_step_handler(msg, take_numbers_f)


def calcul(number_1, number_2, operation):
    if operation == 1:
        result = str(number_1 + number_2)
        global print_operation
        print_operation = 'Сумма двух чисел ='
    elif operation == 2:
        result = str(number_1 - number_2)
        print_operation = 'Разница двух чисел ='
    elif operation == 3:
        result = str(number_1 * number_2)
        print_operation = 'Произведение двух чисел ='
    elif operation == 4:
        result = str(number_1 / number_2)
        print_operation = 'Частное от деления двух чисел ='

    return (result)


def division(msg: telebot.types.Message):
    tmp = msg.text.split()
    if type_of_operation == 4:
        try:
            int(tmp[0]) / int(tmp[1])
            return True
        except ZeroDivisionError:
            return False
    else:
        return True

def take_message(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Выберите, с какими числами будем работать? \n 1. Целые числа \n 2. Дробные числа')
    bot.send_message(chat_id=msg.from_user.id, text='Введите 1 или 2:')
    bot.register_next_step_handler(msg, take_type_numbers)

bot.polling()
