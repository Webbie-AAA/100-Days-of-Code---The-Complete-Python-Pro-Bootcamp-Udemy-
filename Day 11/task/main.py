import random
import sys
import art

user_name = "input goes here"

user_hand = {"name": user_name, "hand" : []}
dealer_hand = {"name": "Dealer", "hand" : []}

def generate_deck():
    suit = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    rank = ["S", "D", "C", "H"]
    deck_of_cards = []
    for r in rank:
        for s in suit:
            deck_of_cards.append(s+r)
    return deck_of_cards

def draw_card_from_deck():
    draw_card = random.choice(generate_deck())
    return draw_card

def hand_card_to_player(num_of_draws: int):
    for i in range(num_of_draws):
        user_hand["hand"].append(draw_card_from_deck())

def hand_card_to_dealer(num_of_draws: int):
    for i in range(num_of_draws):
        dealer_hand["hand"].append(draw_card_from_deck())

# def display_cards(enter_dict: dict):
#     hand_list = enter_dict["hand"]
#     displayed_hand = []
#     for x in hand_list:
#         displayed_hand += art.cards[x[:-1]]
#
#     print(displayed_hand)

def display_cards(enter_dict: dict):
    hand = enter_dict["hand"]
    displayed_hand = []
    for x in hand:
        # displayed_hand.append(art.cards[x[:-1]])
        print(art.cards[x[:-1]], end=" ")

    # print("".join(displayed_hand))


def count_total_points(enter_dict: dict):
    suits_points = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    points_list = enter_dict["hand"]
    total_points = 0
    for i in points_list:
        total_points += suits_points[i[:-1]]
    return total_points

game_play = True

def play():
    start_stop_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'?").lower()
    if start_stop_game == "y":
        print(art.logo)

        hand_card_to_player(2)
        hand_card_to_dealer(2)

    while count_total_points(user_hand) >= 21 or count_total_points(dealer_hand) >21:
        print(f"\nYour cards: {user_hand['hand']}, current score: {count_total_points(user_hand)}")
        # display_cards(user_hand)
        print(f"\nDealer's first card: {dealer_hand['hand'][0]}")
        # display_cards(dealer_hand)


play()


