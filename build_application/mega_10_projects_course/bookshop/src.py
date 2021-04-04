
import sqlite3


class Books:
    _conn = None
    _curr = None

    def __init__(self):
        pass

    @property
    def db(self):
        # if self._conn is None:
        self._conn = self.connect()
        self._curr = self._conn.cursor()
        return self._conn


    @staticmethod
    def connect():
        conn = sqlite3.connect("bookshop.db")
        return conn

    def drop_table(self):
        conn = self.db
        cur = conn.cursor()
        cur.execute("DROP TABLE book")
        conn.commit()
        conn.close()

    def create_table(self):
        conn = self.db
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        conn.commit()
        conn.close()

    def insert(self, title, author, year, isbn):
        conn = self.db
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        conn.commit()
        conn.close()

    def view(self):
        conn = self.db
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        results = cur.fetchall()
        conn.commit()
        conn.close()
        return results

    def search(self, title="", author="", year=0, isbn=""):
        conn = self.db
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",
                    (title, author, year, isbn))
        results = cur.fetchall()
        conn.commit()
        conn.close()
        return results

    def delete(self, bid):
        conn = self.db
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?", (bid, ))
        conn.commit()
        conn.close()

    def update_selected(self, bid, title, author, year, isbn):
        conn = self.db
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=?  WHERE id=?",
                    (title, author, year, isbn, bid,))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    # Books().drop_table()
    b = Books()
    Books().create_table()
    # b.insert("The sun", "John Smith", 1923, 91312336)
    print(b.view())
    print(b.search(year=1923))
