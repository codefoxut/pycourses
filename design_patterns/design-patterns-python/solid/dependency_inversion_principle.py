# Dependency Inversion Principle
"""
Not to be confused with dependency injection,
dependency inversion specifies that high-level modules should not depend on low-level ones;
both should depend on abstractions.
"""

from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class OldResearch:
    def __init__(self, relationships):
        relations = relationships.relations
        for r in relations:
            if r[1] == Relationship.PARENT:
                print(f'{r[0].name} has a child called {r[2].name}.')


class Research:

    def __init__(self, browser: RelationshipBrowser):
        for item in browser.find_all_children_of('John'):
            print(f'John has a child called {item}.')


if __name__ == '__main__':
    parent1 = Person('John')
    child1 = Person('Chris')
    child2 = Person('Jonny')

    relationships_obj = Relationships()
    relationships_obj.add_parent_and_child(parent1, child1)
    relationships_obj.add_parent_and_child(parent1, child2)

    print("old way research!!!")
    OldResearch(relationships_obj)
    print("new way research!!!")
    Research(relationships_obj)
