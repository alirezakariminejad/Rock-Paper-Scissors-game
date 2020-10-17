from config import RULES, RESULT
from random import choice


def user_select():
    user_input = ''
    user_input = input("insert r,p,s... : ")
    if user_input not in RULES:
        print("Oops..., please insert r,p,s...")
        user_select()
    else:
        return user_input


def system_select():
    system_select = choice(RULES)
    return system_select


def who_won(user, system):
    result = {user, system}

    if len(result) == 1:
        return "draw"
    else:
        return RESULT[tuple(sorted(result))]


def play(user, system):
    print(user, system)


user_select = user_select()
system_select = system_select()
winner = who_won(user_select, system_select)
print(user_select, system_select, winner)
