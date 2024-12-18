from .cards import taking_cards

def instant_end(player_value_cards,dealer_value_cards):
    if player_value_cards >= 21 or dealer_value_cards >= 21:
        return True
    return False


def input_check_min(user_input: str, threshold: int) -> int:
    if user_input.isnumeric():
        if  int(user_input) >= threshold:
            return int(user_input)
        else:
            return 0
    if not user_input.isnumeric():
        return 0


def input_check_max(user_input: str, threshold: int) -> int:
    if user_input.isnumeric():
        if int(user_input) <= threshold:
            return int(user_input)
        else:
            return 0
    if not user_input.isnumeric():
        return 0


def bet_round(player,min_bet):
    #Comprobar si el saldo supera a la apuesta minima, porque sino, el usuario es pobre no puede entrar en nazarick
    player_money = player["player_money"]
    name = player["name"]
    bet = input(f"Bienvenido al 21 BlackJack señor/a {name} usted tiene actualmente {player_money} para apostar, cuanto desea emplear en esta ronda? ")
    while True:
        if not input_check_min(bet,min_bet) and not input_check_max(bet, player_money):
            print(f"señor/a {name}, la apuesta que intenta realizar no cumple nuestros requisitos. Su apuesta debe ser un número entre {min_bet} y {player_money} ambos inclusive ")
            bet = input("Introduzca una apuesta valida: ")
        if input_check_min(bet,min_bet) and input_check_max(bet, player_money):
            bet = int(bet)
            break
    print("Perfecto, su apuesta cumple con los requisitos, el juego puede comenzar")
    return {"name":name,"player_money":player_money,"player_bet":bet,"value_cards":0,"cards":[]}


def end_round(user):
    while True:
        choose = input(
            "Diga la acción que desea realizar: consultar valor | consultar cartas | terminar ronda | otra carta: ").lower()
        if choose == "consultar valor":
            print(f"El valor de sus cartas es: {user["value_cards"]}")
        if choose == "consultar cartas":
            print(f"Sus cartas son: {user["cards"]}")
        if choose == "otra carta":
            return "otra carta"
        if choose == "terminar ronda":
            return "terminar ronda"


def while_round(player,table_deck,dealer,min_bet):
    print(f"Señor/a {player["name"]}, la ronda va a comenzar")
    player = bet_round(player, min_bet)
    while True:
        print(f"Comienza una nueva ronda señor/a {player["name"]}")
        player, table_deck = taking_cards(player, table_deck)
        print(f"The house plays")
        dealer, table_deck = taking_cards(dealer, table_deck)
        ending_round = end_round(player)
        main_ending_round = instant_end(player["value_cards"], dealer["value_cards"])
        if main_ending_round:
            break
        if ending_round == "otra carta":
            continue
        if ending_round == "terminar ronda":
            break
    return player, dealer