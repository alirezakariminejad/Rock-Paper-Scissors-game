from config import RULES
from random import choice


def user_select():
    user_input = ''
    user_input = input("insert r,p,s... : ")
    if user_input not in RULES:
        print("Oops...")
        user_select()
    else:
        return user_input


def system_select():
    system_select = choice(RULES)
    return system_select


def play(user, system):
    print(user, system)


user_select = user_select()
system_select = system_select()


play(user_select, system_select)
