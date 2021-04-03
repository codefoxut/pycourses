
class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room = None

    def say(self, message):
        self.room.broadcast(self.name, message)

    def receive(self, sender, message):
        s = f'{sender}: {message}'
        print(f'[{self.name}\'s chat session] {s}')
        self.chat_log.append(s)

    def private_message(self, who, message):
        self.room.message(self.name, who, message)


class ChatRoom:
    def __init__(self):
        self.people = []

    def join(self, person):
        join_msg = f'{person.name} joins the chat.'
        self.broadcast('room', join_msg)
        person.room = self
        self.people.append(person)

    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)


if __name__ == '__main__':
    john = Person('John')
    jane = Person('Jane')

    room = ChatRoom()

    room.join(john)
    room.join(jane)

    john.say('hi room!')
    jane.say('oh,  hey john')

    simon = Person('Simon')
    room.join(simon)
    simon.say('Hi all!')

    simon.private_message('Jane', 'glad to see you')
    jane.private_message('Simon', 'glad! finally! you are here')