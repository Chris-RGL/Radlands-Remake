import random
import Cards
import Deck
import Players

def update(active_player):
    if active_player > len(Players.player_list) - 1:
        active_player = 0

    play_turn(Players.player_list[active_player])
    active_player += 1


def damage(target):
    target_type = target.strip().lower()
    for player in Players.player_list:
        print(player.name)
    target_player = input("Which player would you like to attack: ")

    for player in Players.list:
        if player.name.strip().lower == target_player.lower():
            print(player.active_cards)

def draw(amount):
    #TODO
    pass

def start_event():
    #TODO
    pass

def restore():
    #TODO
    pass

def gain_punk():
    #TODO
    pass

#NOT WORKING PROPERLY
def junk_card(card_name, deck, active_player):
    for card in deck:
        if card.name.strip().lower() == card_name:
            junk_effect = card.junk

            match junk_effect.strip().lower():
                case "gain extra water":
                    active_player.water += 1

                case "injure":
                    target = 'people'
                    damage(target)

                case "draw":
                    amount = 1
                    draw(amount)

                case "raid":
                    start_event()

                case "restore":
                    restore()

                case "gain punk":
                    gain_punk()


    print(f"The card could not be junked because it is not in your hand")




def play_turn(active_player):
    player_action = input("What is your move?\nPlay Card\nJunk Card\nUse Card Ability\nEnd Turn\n")
    if player_action.lower() == "end turn":
        update()

    match player_action.lower():
        case "junk card":
            for cards in active_player.hand:
                print(cards)
            player_action = input("Which card would you like to junk: ")

            junk_card(player_action, active_player.hand, active_player)


        case "play card":
            for cards in active_player.hand:
                print(cards)
            player_action = input("Which card would you like to play: ")



if __name__ == "__main__":
    Players.player_setup()
    active_player = random.choice([0,1])
    update(active_player)


