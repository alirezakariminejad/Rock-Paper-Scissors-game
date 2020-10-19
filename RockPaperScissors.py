from config import RULES, RESULT
from random import choice

result = {"user": 0, "system": 0}


def user_select():
    user_input = ''
    user_input = input("insert r,p,s... : ")
    if user_input not in RULES:
        print("Oops..., please insert r,p,s...")
        user_select()
    else:
        return user_input


def system_select():
    system = choice(RULES)
    return system


def who_won(user, system):
    selected_input = {user, system}
    if len(selected_input) == 1:
        return "draw"
    else:
        win_msg = RESULT[tuple(sorted(selected_input))]
        if win_msg == user:
            result["user"] += 1
            print("Yon Win :)")
        elif win_msg != user:
            result["system"] += 1
            print("Yon Lost :(")
        return win_msg


def play():
    user = user_select()
    system = system_select()
    winner = who_won(user, system)
    print(user, system, winner)
    print(result["user"], result["system"])


while True:
    if result["user"] < 3 and result["system"] < 3:
        play()
    else:
        break;

# again = input("Would you like play this game? ")
# if again == "y":
#     play()
