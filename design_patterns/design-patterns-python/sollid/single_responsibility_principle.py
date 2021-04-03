"""Example of the concepts."""


class Journal:

    def __init__(self):
        self.entries = []
        self.count = 0

    def add(self, item: str):
        self.count += 1
        self.entries.append(f'{self.count}: {item}')

    def remove(self, pos: int):
        self.count -= 1
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as f:
            f.write(str(journal))

    def load(self, filename):
        """read the filename and create object."""

    def load_from_web(self, uri):
        pass


if __name__ == '__main__':
    j = Journal()
    j.add("I called the CTO today.")
    j.add("He didn't respond.")
    print(f'Journal Entries: \n{j}')

    filename = 'journal2020.txt'
    PersistenceManager.save_to_file(j, filename)