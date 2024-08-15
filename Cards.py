class Cards:
    """Base Class"""
    # WOMEN SCARy
    def __init__(self, name = None, type = None, ability = None):
        self.name = name
        self.type = type
        self.ability = ability

class Camp(Cards):
    def __init__(self, name: str, type: str, ability: str,
                 trait: str, ability_cost: int, camp_draw: int):
        super().__init__(name = name, type = type, ability = ability)

        self.trait = trait
        self.ability_cost = ability_cost
        self.camp_draw = camp_draw

    def __str__(self) -> str:
        return f"Name: {self.name}\nType: {self.type}\nTrait: {self.trait}\n" \
               f"Ability: {self.ability}\nCamp Draw: {self.camp_draw}\nAbility Cost: {self.ability_cost}\n"

class Event(Cards):
    def __init__(self, name: str, type: str, ability: str,
                 junk: str, play_cost: int, event_queue: int):
        super().__init__(name = name, type = type, ability = ability)

        self.junk = junk
        self.play_cost = play_cost
        self.event_queue = event_queue

    def __str__(self) -> str:
        return f"Name: {self.name}\nType: {self.type}\nJunk: {self.junk}\n" \
               f"Ability: {self.ability}\nPlay Cost: {self.play_cost}\nEvent Queue: {self.event_queue}\n"

class People(Cards):
    def __init__(self, name: str, type: str, ability: str, junk: str,
                 trait: str, play_cost: int, ability_cost: int):
        super().__init__(name = name, type = type, ability = ability)

        self.junk = junk
        self.trait = trait
        self.play_cost = play_cost
        self.ability_cost = ability_cost

    def __str__(self) -> str:
        return f"Name: {self.name}\nType: {self.type}\nJunk: {self.junk}\nTrait: {self.trait}\n" \
               f"Ability: {self.ability}\nPlay Cost: {self.play_cost}\nAbility Cost: {self.ability_cost}\n"

class Special(Cards):
    def __init__(self, name: str, type: str, ability: str,
                 junk: str, trait: str, purchase_cost: int):
        super().__init__(name = name, type = type, ability = ability)

        self.junk = junk
        self.trait = trait
        self.purchase_cost = purchase_cost

    def __str__(self) -> str:
        return f"Name: {self.name}\nType: {self.type}\nJunk: {self.junk}\nTrait: {self.trait}\n" \
               f"Ability: {self.ability}\nPurchase Cost: {self.purchase_cost}\n"

person = People("Chris", "Human", "Intellegence", "Water", None, 3, 4)
print(person)
