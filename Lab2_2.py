#!/usr/bin/env python3

import random

# Глобальні константи
DEF_CHOICE = 8
MENU = ['spam', 'egg', 'sausage', 'bacon']
MENU_MULTI = MENU + ['eggs', 'sausages']
JOINTS = [', and ', ', ', ' and ', ' with ', ' and double portion of ']
PREFERRED = MENU[0]
FORBIDDEN = {'not', 'without', 'no'}

# Генерація пісні
SONG = ', '.join([PREFERRED.capitalize()] + [PREFERRED] * DEF_CHOICE) + '!'

# Тексти повідомлень
D_WELCOME = 'Welcome to the Vikings restaurant.\nWhat would you like to eat?'
D_CHOICE = '> '
D_PROMOTE = "We highly recommend {dishes}" + f', and {PREFERRED}...'
D_GOOD = "That's a perfect choice. Let's have more {dishes}" + f', and {PREFERRED}!'
D_BAD = "Disgusting. Who eats {dishes}?"
D_UNAVAILABLE = "That's not on our menu.\nWe have {dishes}."

TIP = """Next time call "{script} num" to set the number of dishes."""


# Функція для формування випадкової комбінації страв
def get_dishes(number):
    sel = list(MENU)
    res = []

    for i in range(number):
        rnd = random.choice(sel)
        res.extend([rnd, random.choice(JOINTS)])

    return ''.join(res[:-1])  # Видаляємо останній елемент


# Функція для виведення повідомлення та повернення вибору користувача
def user_input():
    print(D_WELCOME)
    entry = input(D_CHOICE).strip().lower()
    return entry.split()


# Функція для просування популярних страв
def promote():
    print(D_PROMOTE.format(dishes=get_dishes(DEF_CHOICE)))


# Функція для обробки вибору користувача
def process_choice(words):
    if set(words) & set(MENU_MULTI):
        if set(words) & FORBIDDEN:
            print(D_BAD.format(dishes=' '.join(words)))
            promote()
        else:
            print(D_GOOD.format(dishes=' '.join(words)))
            print(f'Vikings: "{SONG}"')
    elif not words:
        promote()
    else:
        print(D_UNAVAILABLE.format(dishes=get_dishes(DEF_CHOICE)))


# Основна функція
def main(args):
    script, *args = args

    if len(args) > 1:
        exit('Too many arguments. ' + TIP.format(script=script))

    num = DEF_CHOICE if not args else int(args[0])

    words = user_input()
    process_choice(words)

    if not args:
        print('\tTip:', TIP.format(script=script))


if __name__ == '__main__':
    import sys

    main(sys.argv)
