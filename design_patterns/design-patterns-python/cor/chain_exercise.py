from abc import ABC
from enum import Enum


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Creature(ABC):
    def __init__(self, game, attack, defense):
        self.initial_defense = defense
        self.initial_attack = attack
        self.game = game

    def __str__(self):
        return f'{self.__class__.__name__} ({self.attack}/{self.defense})'

    @property
    def attack(self): pass

    @property
    def defense(self): pass

    def query(self, source, query): pass


class Goblin(Creature):

    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)

    @property
    def attack(self):
        q = Query(self.initial_attack, WhatToQuery.ATTACK)
        for c in self.game.creatures:
            c.query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.initial_defense, WhatToQuery.DEFENSE)
        for c in self.game.creatures:
            c.query(self, q)
        return q.value

    def query(self, source, query):
        if self != source and query.what_to_query == WhatToQuery.DEFENSE:
            query.value += 1


class GoblinKing(Goblin):

    def __init__(self, game):
        super().__init__(game, 3, 3)

    def query(self, source, query):
        if self != source and query.what_to_query == WhatToQuery.ATTACK:
            query.value += 1
        else:
            super().query(source, query)


class Query:
    def __init__(self, default_value, what_to_query):
        self.value = default_value
        self.what_to_query = what_to_query
        # self.creature_name = creature_name


class Game:
    def __init__(self):
        self.creatures = []


if __name__ == '__main__':
    game1 = Game()
    g1 = Goblin(game1)
    game1.creatures.append(g1)
    g2 = Goblin(game1)
    game1.creatures.append(g2)
    g3 = Goblin(game1)
    game1.creatures.append(g3)
    print(g1, g2, g3)
    gbking = GoblinKing(game1)
    game1.creatures.append(gbking)
    print("goblin", g1, g2, g3)
    print("gbking", gbking)

