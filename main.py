import random

ct = {
    1: {
        "value": 1,
        "fancy": "♣A"
    },
    2: {
        "value": 2,
        "fancy": "♣2"
    },
    3: {
        "value": 3,
        "fancy": "♣3"
    },
    4: {
        "value": 4,
        "fancy": "♣4"
    },
    5: {
        "value": 5,
        "fancy": "♣5"
    },
    6: {
        "value": 6,
        "fancy": "♣6"
    },
    7: {
        "value": 7,
        "fancy": "♣7"
    },
    8: {
        "value": 8,
        "fancy": "♣8"
    },
    9: {
        "value": 9,
        "fancy": "♣9"
    },
    10: {
        "value": 10,
        "fancy": "♣10"
    },
    11: {
        "value": 10,
        "fancy": "♣K"
    },
    12: {
        "value": 10,
        "fancy": "♣Q"
    },
    13: {
        "value": 10,
        "fancy": "♣J"
    },
    14: {
        "value": 1,
        "fancy": "♥A"
    },
    15: {
        "value": 2,
        "fancy": "♥2"
    },
    16: {
        "value": 3,
        "fancy": "♥3"
    },
    17: {
        "value": 4,
        "fancy": "♥4"
    },
    18: {
        "value": 5,
        "fancy": "♥5"
    },
    19: {
        "value": 6,
        "fancy": "♥6"
    },
    20: {
        "value": 7,
        "fancy": "♥7"
    },
    21: {
        "value": 8,
        "fancy": "♥8"
    },
    22: {
        "value": 9,
        "fancy": "♥9"
    },
    23: {
        "value": 10,
        "fancy": "♥10"
    },
    24: {
        "value": 10,
        "fancy": "♥K"
    },
    25: {
        "value": 10,
        "fancy": "♥Q"
    },
    26: {
        "value": 10,
        "fancy": "♥J"
    },
    27: {
        "value": 1,
        "fancy": "♠A"
    },
    28: {
        "value": 2,
        "fancy": "♠2"
    },
    29: {
        "value": 3,
        "fancy": "♠3"
    },
    30: {
        "value": 4,
        "fancy": "♠4"
    },
    31: {
        "value": 5,
        "fancy": "♠5"
    },
    32: {
        "value": 6,
        "fancy": "♠6"
    },
    33: {
        "value": 7,
        "fancy": "♠7"
    },
    34: {
        "value": 8,
        "fancy": "♠8"
    },
    35: {
        "value": 9,
        "fancy": "♠9"
    },
    36: {
        "value": 10,
        "fancy": "♠10"
    },
    37: {
        "value": 10,
        "fancy": "♠K"
    },
    38: {
        "value": 10,
        "fancy": "♠Q"
    },
    39: {
        "value": 10,
        "fancy": "♠J"
    },
    40: {
        "value": 1,
        "fancy": "♦A"
    },
    41: {
        "value": 2,
        "fancy": "♦2"
    },
    42: {
        "value": 3,
        "fancy": "♦3"
    },
    43: {
        "value": 4,
        "fancy": "♦4"
    },
    44: {
        "value": 5,
        "fancy": "♦5"
    },
    45: {
        "value": 6,
        "fancy": "♦6"
    },
    46: {
        "value": 7,
        "fancy": "♦7"
    },
    47: {
        "value": 8,
        "fancy": "♦8"
    },
    48: {
        "value": 9,
        "fancy": "♦9"
    },
    49: {
        "value": 10,
        "fancy": "♦10"
    },
    50: {
        "value": 10,
        "fancy": "♦K"
    },
    51: {
        "value": 10,
        "fancy": "♦Q"
    },
    52: {
        "value": 10,
        "fancy": "♦J"
    },
    53: {
        "value": 10,
        "fancy": "♣A"
    },
    54: {
        "value": 10,
        "fancy": "♥A"
    },
    55: {
        "value": 10,
        "fancy": "♠A"
    },
    56: {
        "value": 40,
        "fancy": "♦4"
    },
}


def gayme():
    # Bunch of variables
    cardnos = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
        22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
        40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51
    ]
    cardnocopy = cardnos.copy()
    # initalize player and dealer hands/scores variables
    dealer_hand = []
    player_hand = []
    player_score = []
    dealer_score = []
    player_total = 0
    dealer_total = 0
    # Deal 2 cards to both!
    card1 = randomNoRep(cardnocopy)
    card2 = randomNoRep(cardnocopy)
    card3 = randomNoRep(cardnocopy)
    card4 = randomNoRep(cardnocopy)
    player_hand.append(ct[card1]["fancy"])
    player_hand.append(ct[card2]["fancy"])
    player_score.append(ct[card1]["value"])
    player_score.append(ct[card2]["value"])
    dealer_hand.append(ct[card3]["fancy"])
    dealer_hand.append(ct[card4]["fancy"])
    dealer_score.append(ct[card3]["value"])
    dealer_score.append(ct[card4]["value"])
    # Game init (the while loop is broken idk why hence the if statement)
    while player_total < 21 or dealer_total < 21:
        player_total = sum(player_score)
        dealer_total = sum(dealer_score)
        print(
            f"Your hand {player_hand}\nDealers hand ['{dealer_hand[1]}, '?'..]\nYour score {player_total}\n"
        )
        choice = input("Input \"h\" or \"s\" to hit or stand.\n-> ")
        if choice.lower() == "h":
            player_hand.append(ct[randomNoRep(cardnocopy)]["fancy"])
            player_score.append(ct[randomNoRep(cardnocopy)]["value"])
        elif choice.lower() == "s":
            dealer_hand.append(ct[randomNoRep(cardnocopy)]["fancy"])
            dealer_score.append(ct[randomNoRep(cardnocopy)]["value"])
            print('Ended')
            print(
                f"Your Hand: {player_hand}\nYour Score: {player_total}\nDealers Hand {dealer_hand}\n Dealers Score {dealer_total}")

            if min(dealer_total, player_total) == player_total:
                print("You Lose...")
                exit()
            elif min(dealer_total, player_total) == dealer_total:
                print("You Win!\n")
                exit()
            else:
                print("Draw!\n")
                exit()
        else:
            print("Im sorry I do not understand try again")
        player_total = sum(player_score)
        dealer_total = sum(dealer_score)
        if player_total == 21:
            print(
                f"Your Hand: {player_hand}\nYour Score: {player_total}\nDealers Hand: {dealer_hand}\nDealers Score: {dealer_total}\nYou Win!")
            exit()
        elif player_total > 21:
            print(
                f"Your Hand: {player_hand}\nYour Score: {player_total}\nDealers Hand: {dealer_hand}\nDealers Score:  {dealer_total}\nYou Lose...")
            exit()
        elif dealer_total == 21:
            print(
                f"Your Hand: {player_hand}\nYour Score: {player_total}\nDealers Hand: {dealer_hand}\nDealers Score: {dealer_total}\nYou Lose...")
            exit()
        elif dealer_total > 21:
            print(
                f"Your Hand: {player_hand}\nYour Score: {player_total}\nDealers Hand: {dealer_hand}\nDealers Score: {dealer_total}\nYou Win!")
            exit()
