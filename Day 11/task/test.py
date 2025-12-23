from main import generate_deck, display_cards, count_total_points, hand_card_to_player, hand_card_to_dealer
import art

def test_generate_deck():
    complete_deck = [
        'AS',
        '2S',
        '3S',
        '4S',
        '5S',
        '6S',
        '7S',
        '8S',
        '9S',
        '10S',
        'JS',
        'QS',
        'KS',
        'AD',
        '2D',
        '3D',
        '4D',
        '5D',
        '6D',
        '7D',
        '8D',
        '9D',
        '10D',
        'JD',
        'QD',
        'KD',
        'AC',
        '2C',
        '3C',
        '4C',
        '5C',
        '6C',
        '7C',
        '8C',
        '9C',
        '10C',
        'JC',
        'QC',
        'KC',
        'AH',
        '2H',
        '3H',
        '4H',
        '5H',
        '6H',
        '7H',
        '8H',
        '9H',
        '10H',
        'JH',
        'QH',
        'KH'
    ]
    assert generate_deck() == complete_deck

# def test_display_cards():
#     #Arrange
#     user_dict = {"name": "name", "hand": ["7S", "KC", "8H"]}
#     # Act
#     result = art.cards['7'] + " " +  art.cards['K'] + " " + art.cards['8']
#     # Assert
#     assert display_cards(user_dict) == result

# def test_dealer_gets_two_cards():
#     # Arrange
#     dealer_hand = {"name": "name", "hand": []}
#     # Act
#     hand_card_to_dealer(2)
#     result =  len(dealer_hand["hand"]) + 2
#     # Assert
#     assert len(dealer_hand["hand"]) == result

def test_count_total_points_results():
    #Arrange
    user_dict = {"name": "name", "hand": ["7S", "KC", "8H"]}
    # Act
    result = 25
    # Assert
    assert count_total_points(user_dict) == result

def test_count_result_when_suit_is_10():
    # Arrange
    user_dict = {"name": "name", "hand": ["7S", "KC", "8H", "10H"]}
    # Act
    result = 35
    # Assert
    assert count_total_points(user_dict) == result

def test_ace_equal_1_when_over_21():
    #Arrange
    test_dict = {"name": "name", "hand": ["AC", "8H", "10H"]}
    #Act
    result = 19
    #Assert
    assert count_total_points(test_dict) == result




