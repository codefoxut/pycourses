
from abc import ABC


class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        first = self.creatures[c1_index]
        second = self.creatures[c2_index]
        does_c2_die = self.hit(first, second)
        does_c1_die = self.hit(second, first)

        if does_c1_die and does_c2_die:
            resp = -1
        elif does_c1_die:
            resp = c2_index
        elif does_c2_die:
            resp = c1_index
        else:
            resp = -1

        return resp

    def hit(self, attacker, defender):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        return attacker.attack >= defender.health


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        resp = attacker.attack >= defender.health
        defender.health -= attacker.attack
        return resp


if __name__ == '__main__':
    c1 = Creature(1, 2)
    c2 = Creature(1, 2)
    game = TemporaryDamageCardGame([c1, c2])
    assert -1 == game.combat(0, 1), 'Combat should yield -1 since nobody died.'
    assert -1 == game.combat(0, 1), 'Combat should yield -1 since nobody died.'

    # test 2
    c1 = Creature(1, 1)
    c2 = Creature(2, 2)
    game = TemporaryDamageCardGame([c1, c2])
    assert 1 == game.combat(0, 1)

    # test 3
    c1 = Creature(2, 1)
    c2 = Creature(2, 2)
    game = TemporaryDamageCardGame([c1, c2])
    assert -1 == game.combat(0, 1)

    c1 = Creature(1, 2)
    c2 = Creature(1, 3)
    game = PermanentDamageCardGame([c1, c2])
    assert -1 == game.combat(0, 1), 'Nobody should win this battle.'
    assert 1 == c1.health
    assert 2 == c2.health
    assert 1 == game.combat(0, 1), 'Creature at index 1 should win this'
