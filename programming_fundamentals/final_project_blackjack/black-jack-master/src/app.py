from .round import input_check_min, while_round

def give_me_cards():
    return [
        {"ACE":"ACE",
         "card_value":[1, 11]},
        {"2":"2",
         "card_value": 2},
        {"3":"3",
         "card_value": 3},
        {"4": "4",
         "card_value": 4},
        {"5": "5",
         "card_value": 5},
        {"6": "6",
         "card_value": 6},
        {"7": "7",
         "card_value": 7},
        {"8": "8",
         "card_value": 8},
        {"9": "9",
         "card_value": 9},
        {"J": "J",
         "card_value": 10},
        {"Q": "Q",
         "card_value": 10},
        {"K": "K",
         "card_value": 10},
    ]


def name_is_valid(name):
    if name == "" or name == "dealer":
        return ""
    else:
        return name


def player_settings(min_budget):
    name = input("Bienvenido al casino de Nazarick, ¿A quien nos dirijimos? ")
    while not name_is_valid(name):
        name = input("Su nombre no puede estar vacío, introduzca su nombre, porfavor: ")
    print(f"Bienvenido al casino de Nazarick, señor/a {name.capitalize()}")

    player_money = input(
        f"Si desea jugar en nuestro casino, denos un presupuesto con un valor númerico mayor o igual a {min_budget}: ")
    while not input_check_min(player_money, min_budget):
        player_money = input(
            f"Disculpe señor/a {name.capitalize()} usted esta diciendonos que {player_money} es su presupuesto y no cumple con nuestras condiciones para jugar, porfavor introduzca un presupuesto con un valor numerico mayor que {min_budget}: ")
    print(f"Dispone de {player_money} para jugar, bienvenido al casino señor/a {name}")

    return {"name": name, "player_money": int(player_money)}


def who_win(player, dealer):
    if player["value_cards"] > dealer["value_cards"]:
        player["player_money"]= player["player_money"]+ player["player_bet"]*2
        dealer["dealer_money"] = dealer["dealer_money"] - player["player_bet"]
        print(f"You win player {player["player_bet"] * 2} ,your current money for the next games is {player["player_money"]}")
        return dealer["dealer_money"],player["player_money"]
    else:
        player["player_money"] = player["player_money"] - player["player_bet"]
        dealer["dealer_money"] = dealer["dealer_money"] + player["player_bet"]
        print(f"You lose {player["player_bet"]} ,your current money for the next game is {player["player_money"]}")
        return dealer["dealer_money"],player["player_money"]


def exit_game(name):
    confirm = ""
    while not confirm in ["yes", "no"]:
        confirm = input(
            f"Oh vaya, tan pronto señor/a {name}? Esta seguro de marcharse en un momento tan dulce? \nyes/no ")
        if confirm == "yes":
            print(f"Esta bién que tenga un buen día, esperamos verlo pronto señor/a {name}")
            exit(0)
        if confirm == "no":
            print(f"Perfecto señor/a {name}, creemos que es la mejor decisión, sigamos jugando")
            return True


def continue_playing(user):
    choose=input(f"Si desea seguir jugando diga cualquier cosa, de lo contrario escriba exit: ")
    if choose == "exit".lower():
        return exit_game(user["name"])
    else: 
        return


def end_game(player,dealer,min_budget):
    if player["player_money"] < min_budget or dealer["dealer_money"] < min_budget:
        return True


def game(player,dealer,min_bet,table_deck,min_budget):
    while not end_game(player,dealer,min_budget):
        player, dealer = while_round(player,table_deck,dealer,min_bet)
        who_win(player, dealer)
        continue_playing(player)
    if player["player_money"] > dealer["dealer_money"]:
        print(f"Ehnorabuena señor/a {player["name"]} usted se retira como campeon del mundo con {player["player_money"]}")
    else:
        print(f"Lamentablemente señor/a {player["name"]} Nazarick gana de nuevo")
