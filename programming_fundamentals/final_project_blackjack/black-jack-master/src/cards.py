import random

def randomize_card(deck):
    suits = list(deck.keys())
    card_random_suit = suits[random.randrange(0, len(suits))]
    card_list = deck[card_random_suit]
    random_card_index = random.randrange(0, len(card_list))
    random_card = deck[card_random_suit][random_card_index]
    key_value_list = list(random_card.keys())
    random_card_name = key_value_list[0]
    return {
        "card_name": random_card[random_card_name],
        "card_value": random_card["card_value"],
        "card_suit": card_random_suit
    }
# Aquí arriba en mi flujo debo comprobar si es un ace primero y que solo introduzca ace como parametro


def ace_choose(card,user):
    card_name = card["card_value"]
    suit_name = list(card.values())[2]
    print(f"Has obtenido un {card["name"]} of {suit_name}! Tu valor de cartas actual es: {user["value_cards"]}")
    choose = input(f"Puede darle 1 o 11 como valor ¿Que valor desea para su {card_name} of {suit_name} ?: ")
    while not choose == "1" or choose == "11":
        choose = input(f"Valor incorrecto, porfavor de 1 o 11 al valor de su {card_name} of {suit_name}: ")
    print(f"Ehnorabuena, usted ha escogido {choose} como valor para su {card_name} of {suit_name}")
    card["card_value"] = int(choose)

    return card


def remove_card_from_deck(deck,card):
    card_suit_list = deck[card["card_suit"]]
    card_name = card["card_name"]
    card_value = card["card_value"]
    if card_name == "ACE":
        card_suit_list.pop(0)
        return deck
    if not card_name == "ACE":
        card_index = card_suit_list.index({card_name:card_name,"card_value":card_value})
        card_suit_list.pop(card_index)
        return deck


def cards(user,card):
    user["cards"].append(card)
    return user


def set_value_cards(user):
    cards_list = user["cards"]
    user["value_cards"] = 0
    cards_value = user["value_cards"]
    for i in cards_list:
        cards_value += i["card_value"]
    user["value_cards"] = cards_value

    return user

def best_ace(user,ace):
    user = set_value_cards(user)
    if 10 < user["value_cards"]:
        ace["card_value"] = 1
    else:
        ace["card_value"] = 11
    return ace

def taking_cards(user,deck):
    if user["name"] == "dealer":
        message = "La carta para la casa"
    else:
        message = "Su carta"
    card = randomize_card(deck)
    if card["card_name"] == "ACE" and user["name"] == "dealer":
        card = best_ace(card,user)
    if card["card_name"] == "ACE" and user["name"] != "dealer":
        card = ace_choose(card,user)
    print(f"{message} es el {card["card_name"]} de {card["card_suit"]}")
    user["cards"].append(card)
    user = set_value_cards(user)
    deck = remove_card_from_deck(deck, card)
    return user,deck
