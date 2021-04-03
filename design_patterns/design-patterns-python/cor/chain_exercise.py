from abc import ABC
from enum import Enum


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature_name, what_to_query, default_value):
        self.value = default_value
        self.what_to_query = what_to_query
        self.creature_name = creature_name


class Creature:
    def __init__(self, game, attack, defense):
        self.game = game
        self.attack = attack
        self.defense = defense


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack=attack, defense=defense)
        self.game.creatures.append(self)


class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game, attack=3, defense=3)


class CreatureModifier(ABC):
    def __init__(self, game, creature):
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        pass


class GoblinModifier(CreatureModifier):

    def handle(self, sender, query):
        pass


class GoblinKingModifier(CreatureModifier):

    def handle(self, sender, query):
        pass


class Game:
    def __init__(self):
        self.creatures = []

    @property
    def num_of_goblin(self):
        return len([x for x in self.creatures if isinstance(x, Goblin)])

    def is_king_in_play(self):
        return any([isinstance(x, GoblinKing) for x in self.creatures])


if __name__ == '__main__':
    game1 = Game()
    goblin = Goblin(game1)
    game1.creatures.append(goblin)

