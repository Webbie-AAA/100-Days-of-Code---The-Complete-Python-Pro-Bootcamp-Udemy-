import random
import art

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

def display_cards(enter_dict: dict):
    hand = enter_dict["hand"]
    card_lines = [art.cards[card[:-1]].splitlines() for card in hand]
    for row in range(len(card_lines[0])):
        for card in card_lines:
            print(card[row], end=" ")
        print()

def count_total_points(enter_dict: dict):
    aces = ["AC", "AD", "AH", "AS"]
    suits_points = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    points_list = enter_dict["hand"]
    total_points = 0
    for i in points_list:
        total_points += suits_points[i[:-1]]
    for ace in aces:
        if ace in enter_dict["hand"] and total_points > 21:
            total_points -= 10
    return total_points

def win_loss_message():
    print(f"Dealer's cards: {dealer_hand['hand']}\nDealers current score: {count_total_points(dealer_hand)}")
    display_cards(dealer_hand)
    print(f"Your cards: {user_hand['hand']}\nYour current score: {count_total_points(user_hand)}")
    display_cards(user_hand)

def calculate_win_or_loss(user_total_points, dealer_total_points):
    if user_total_points == 21:
        win_loss_message()
        print(f"{user_name} wins")
    elif user_total_points > 21:
        win_loss_message()
        print(f"{user_name} loses")
    elif user_total_points < 21 and user_total_points > dealer_total_points:
        win_loss_message()
        print(f"{user_name} wins")
    elif user_total_points == dealer_total_points:
        win_loss_message()
        print(f"It's a draw {user_name}")
    else:
        win_loss_message()
        print(f"{user_name} lose")


def play():
    print(art.logo)

    hand_card_to_player(2)
    hand_card_to_dealer(2)

    print(f"\nYour cards: {user_hand['hand']}, current score: {count_total_points(user_hand)}")
    display_cards(user_hand)
    print(f"\nDealer's first card: {dealer_hand['hand'][0]}")
    while count_total_points(user_hand) < 21:
        hit_or_stick = input("\nType 'y' to hit, or type 'n' to stick:\t")
        if hit_or_stick == 'y':
            hand_card_to_player(1)
            print(f"\nYour cards: {user_hand['hand']}, current score: {count_total_points(user_hand)}")
            display_cards(user_hand)
            while count_total_points(dealer_hand) < 17:
                hand_card_to_dealer(1)
            print(f"\nDealer's first card: {dealer_hand['hand'][0]}")

        else:
            break
    calculate_win_or_loss(count_total_points(user_hand), count_total_points(dealer_hand))




game_play = True
while game_play:
    start_stop_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n'?:  ").lower().strip()

    if start_stop_game == "y":
        user_name = input("Type your name to begin:\t")
        user_hand = {"name": user_name, "hand": []}
        dealer_hand = {"name": "Dealer", "hand": []}
        play()
    else:
        game_play = False

