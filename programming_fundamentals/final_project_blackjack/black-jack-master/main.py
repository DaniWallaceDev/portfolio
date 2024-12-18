from src.app import player_settings, game, give_me_cards

if __name__ == "__main__":
    dealer = {"name": "dealer",
              "dealer_money": 10000,
              "cards": [],
              "value_cards": 0}
    table_deck = {"hearts": give_me_cards(),
                  "spades": give_me_cards(),
                  "diamonds": give_me_cards(),
                  "clubs": give_me_cards()}
    min_budget = 10
    min_bet = 1
    player = player_settings(min_budget)
    game(player, dealer, min_bet, table_deck, min_budget)
