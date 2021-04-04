
import tkinter as tk
from src import Books


class BookShop(tk.Frame):

    def __init__(self, master=None, cnf=None, **kw):
        cnf = cnf if cnf is not None else {}
        super().__init__(master=master, cnf=cnf, **kw)
        self.master = master
        self.books = Books()
        self.lb1, self.e1, self.e2, self.e3, self.e4 = None, None, None, None, None
        self.title_text = tk.Variable()
        self.author_text = tk.Variable()
        self.year_text = tk.Variable()
        self.isbn_text = tk.Variable()
        self.selected_tuple = None
        self.create_widgets()

    def create_widgets(self):
        # labels
        l1 = tk.Label(self.master, text='Title')
        l1.grid(row=0, column=0)

        l2 = tk.Label(self.master, text='Author')
        l2.grid(row=0, column=2)

        l3 = tk.Label(self.master, text='Year')
        l3.grid(row=1, column=0)

        l4 = tk.Label(self.master, text='ISBN')
        l4.grid(row=1, column=2)

        # entry input
        self.title_text = tk.StringVar()
        self.e1 = tk.Entry(self.master, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text = tk.StringVar()
        self.e2 = tk.Entry(self.master, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text = tk.StringVar()
        self.e3 = tk.Entry(self.master, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.isbn_text = tk.StringVar()
        self.e4 = tk.Entry(self.master, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)

        # listbox and scrollbar
        self.lb1 = tk.Listbox(self.master, height=6, width=35)
        self.lb1.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb1 = tk.Scrollbar(self.master)
        sb1.grid(row=2, column=2, rowspan=6)

        self.lb1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.lb1.yview)

        self.lb1.bind('<<ListboxSelect>>', self.get_selected_row)

        # buttons
        b1 = tk.Button(self.master, text="View All", width=12, command=self.view_command)
        b1.grid(row=2, column=3)

        b2 = tk.Button(self.master, text="Search Entry", width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3 = tk.Button(self.master, text="Add Entry", width=12, command=self.add_command)
        b3.grid(row=4, column=3)

        b4 = tk.Button(self.master, text="Update Entry", width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        b5 = tk.Button(self.master, text="Delete Entry", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6 = tk.Button(self.master, text="Close", width=12, command=self.master.destroy)
        b6.grid(row=7, column=3)

    def get_selected_row(self, event):
        if self.lb1.size() == 0:
            return
        index = self.lb1.curselection()[0]
        self.selected_tuple = self.lb1.get(index)
        print(index, self.selected_tuple)
        self.e1.delete(0, tk.END)
        self.e1.insert(tk.END, self.selected_tuple[1])
        self.e2.delete(0, tk.END)
        self.e2.insert(tk.END, self.selected_tuple[2])
        self.e3.delete(0, tk.END)
        self.e3.insert(tk.END, self.selected_tuple[3])
        self.e4.delete(0, tk.END)
        self.e4.insert(tk.END, self.selected_tuple[4])
        return self.selected_tuple

    def view_command(self):
        self.lb1.delete(0, tk.END)
        for row in self.books.view():
            self.lb1.insert(tk.END, row)

    def search_command(self):
        self.lb1.delete(0, tk.END)
        title = self.title_text.get()
        author = self.author_text.get()
        year = self.year_text.get()
        isbn = self.isbn_text.get()
        for row in self.books.search(title, author, year, isbn):
            self.lb1.insert(tk.END, row)

    def add_command(self):
        title = self.title_text.get()
        author = self.author_text.get()
        year = self.year_text.get()
        isbn = self.isbn_text.get()
        self.books.insert(title, author, year, isbn)
        self.lb1.delete(0, tk.END)
        self.lb1.insert(tk.END, (title, author, year, isbn))

    def delete_command(self):
        self.books.delete(bid=self.selected_tuple[0])

    def update_command(self):
        title = self.title_text.get()
        author = self.author_text.get()
        year = self.year_text.get()
        isbn = self.isbn_text.get()
        self.books.update_selected(self.selected_tuple[0], title, author, year, isbn)


    @staticmethod
    def run():
        root = tk.Tk()
        app = BookShop(master=root)
        app.master.wm_title("BookStore")
        app.mainloop()


if __name__ == '__main__':
    BookShop.run()
