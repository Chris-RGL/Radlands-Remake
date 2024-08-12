class Cards:
    """Abstract base class"""
    def __init__(self):
        raise NotImplementedError("Cannot create card object here")
        self.type = None
        self.junk = None
        self.name = None
        self.trait = None
        self.ability = None
        self.camp_draw = 0
        self.play_cost = 0
        self.ability_cost = 0
        self.event_queue = 0
        self.purchase_cost = 0

class Camp(Cards):
    def __init__(self, type: str, name: str, trait: str, ability: str,
                 camp_draw: int, ability_cost: int):
        self.type = type
        self.name = name
        self.trait = trait
        self.ability = ability
        self.camp_draw = camp_draw
        self.ability_cost = ability_cost

    def __str__(self) -> str:
        return f"Name: {self.name}\nType: {self.type}\nTrait: {self.trait}\n" \
               f"Ability: {self.ability}\nCamp Draw: {self.camp_draw}\nAbility Cost: {self.ability_cost}\n"

class Event(Cards):
    def __init__(self, type: str, name: str, ability: str,
                 play_cost: int, junk: str, event_queue: int):
        self.type = type
        self.junk = junk
        self.name = name
        self.ability = ability
        self.play_cost = play_cost
        self.event_queue = event_queue

    def __str__(self) -> str:
        return f"Name: {self.name}\nType: {self.type}\nJunk: {self.junk}\n" \
               f"Ability: {self.ability}\nPlay Cost: {self.play_cost}\nEvent Queue: {self.event_queue}\n"

class People(Cards):
    def __init__(self, type: str, junk: str, name: str, trait: str,
                 ability: str, play_cost: int, ability_cost: int):
        self.type = type
        self.junk = junk
        self.name = name
        self.trait = trait
        self.ability = ability
        self.play_cost = play_cost
        self.ability_cost = ability_cost

    def __str__(self) -> str:
        return f"Name: {self.name}\nType: {self.type}\nJunk: {self.junk}\nTrait: {self.trait}\n" \
               f"Ability: {self.ability}\nPlay Cost: {self.play_cost}\nAbility Cost: {self.ability_cost}\n"

class Special(Cards):
    def __init__(self, type: str, name: str, purchase_cost: int, ability: str,
                 trait: str, junk: str):
        self.type = type
        self.junk = junk
        self.name = name
        self.trait = trait
        self.ability = ability
        self.purchase_cost = purchase_cost

    def __str__(self) -> str:
        return f"Name: {self.name}\nType: {self.type}\nJunk: {self.junk}\nTrait: {self.trait}\n" \
               f"Ability: {self.ability}\nPurchase Cost: {self.purchase_cost}\n"



