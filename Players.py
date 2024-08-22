import Cards
import random
import Deck

player_list = []
class Player:
    def __init__(self, name: str, camp_card= None, hand = None, active_cards = None,
                 water = 3):
        self.name = name
        self.camp_card = camp_card
        self.hand = hand
        self.active_cards = active_cards
        self.water = water

    def __str__(self):
        return f"Name: {self.name}\nCamp Card: {self.camp_card}\nHand: {self.hand}\n" \
               f"Active Cards: {self.active_cards}\nWater: {self.water}\n"


"""This class initiats the player objects with a name to start"""
def choose_names(players):
    player_count = 0
    while player_count < players:
        name = input('Enter Name: ')
        player = Player(name)
        player_list.append(player)
        player_count += 1

    return player_list


"""This class allows each player to choose their desired camps"""
def choose_camps():
    print(len(Deck.deck))
    #Itterate through each player
    player_count = 0
    while player_count < len(player_list):

        #Create a camp deck list from the deck list
        camp_deck = []
        for card in Deck.deck:
            if isinstance(card, Cards.Camp):
                camp_deck.append(card)

        #Create a list containing 6 random camps from the camp deck
        choice_deck = []
        while len(choice_deck) < 6:
            camp_card = random.choice(camp_deck)
            choice_deck.append(camp_card)

            #To make sure there are no duplicates
            camp_deck.remove(camp_card)

        for card in choice_deck:
            print(card)

        camps = []

        #User input for camp choices
        camps.append(input('Pick Camp Card #1: '))
        camps.append(input('Pick Camp Card #2: '))
        camps.append(input('Pick Camp Card #3: '))

        #Replace each index with the camp card listed
        for i, camp_name in enumerate(camps):
            for card in choice_deck:
                if card.name.lower() == camp_name.lower():
                    camps[i] = card
                    break

        #Adds camp cards to player object
        player_list[player_count].camp_card = camps


        player_count += 1

    #Remove all camp cards from deck
    to_remove = [card for card in Deck.deck if isinstance(card, Cards.Camp)]
    for card in to_remove:
        Deck.deck.remove(card)


def hand_setup():
    for player in player_list:
        hand = []
        starter_hand = 0
        for camp in player.camp_card:
            starter_hand += camp.camp_draw

        for i in range(starter_hand):
            draw_card = random.choice(Deck.deck)
            hand.append(draw_card)
            Deck.deck.remove(draw_card)

        player.hand = hand


def player_setup():
    players = int(input('How many players: '))
    player_list = choose_names(players)
    choose_camps()
    hand_setup()



