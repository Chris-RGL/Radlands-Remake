"""This is the game board.
Both the game board and deck are initialized here"""
import pandas as pd
import Cards

#Load the card CSV file
file_path = "Cards\Radlands_Cards.csv"
cards = pd.read_csv(file_path)

deck = []

"""This creats a list of cards that we use as the deck.
Each card is created as an object before being added to the deck"""
for _, row in cards.iterrows():
    card_type = row['Card Type']

    count = 0
    while count < row['Qty']:
        if card_type == 'Camp':
            card = Cards.Camp(
                name = row['Card Name'],
                type = row['Card Type'],
                ability = row['Card Ability'],
                trait = row['Card Trait'],
                ability_cost = row['Water Ability Cost'],
                camp_draw = row['Camp Draw']
            )

        elif card_type == 'Event':
            card = Cards.Event(
                name = row['Card Name'],
                type = row['Card Type'],
                ability = row['Card Ability'],
                junk=row['Junk Effect'],
                play_cost=row['Water Play Cost'],
                event_queue=row['Event Queue']
            )
        elif card_type == 'People':
            card = Cards.People(
                name = row['Card Name'],
                type = row['Card Type'],
                ability = row['Card Ability'],
                junk=row['Junk Effect'],
                trait=row['Card Trait'],
                play_cost=row['Water Play Cost'],
                ability_cost = row['Water Ability Cost']
            )
        elif card_type == 'Special Event':
            card = Cards.Special(
                name = row['Card Name'],
                type = row['Card Type'],
                ability = row['Card Ability'],
                junk=row['Junk Effect'],
                trait=row['Card Trait'],
                purchase_cost=row['Purchase Cost']
            )
        else:
            continue

        deck.append(card)
        count += 1







