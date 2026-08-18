from tkinter import *

class Input_Field:
    def __init__(self):
        self.root = Tk()
        self.root.title("Sudoku Löser")
        self.input_fields = []
        for a in range(81):
            self.input_fields.append(Entry(self.root, width=5))

        for a in range(81):
            self.input_fields[a].grid(row=(a // 9), column=(a % 9), padx=10, pady=10)

    def build_string(self):
        startfield = ""
        for a in range(81):
            value = self.input_fields[a].get()
            #assert 0 < int(value) < 10 or str(value) == ""
            if value == "":
                startfield = startfield + "0"

            else:
                startfield = startfield + value

        assert len(startfield) == 81

        return startfield

    def write(self, field):
        for a in range(81):
            self.input_fields[a].delete(0, END)
            if field[a] != "0":
                self.input_fields[a].insert(0, str(field[a]))

    def clear(self):
        for a in self.input_fields:
            a.delete(0, END)
