import Counter
class Block:
    def __init__(self, id, value):
        assert type(id) == int and 0 <= id <= 81
        assert type(value) == str


        self.id = id
        self.value = int(value)
        self.counter = Counter.Counter()
        assert 0 <= self.value <= 9

        if self.value == 0:
            self.state = False
            self.possible_values = "123456789"

        else:
            self.state = True
            self.possible_values = ""

        self.row = self.id // 9
        self.column = self.id % 9

        if 0 <= self.row < 3:
            if 0 <= self.column < 3:
                self.square = 0

            elif 3 <= self.column < 6:
                self.square = 1

            else:
                self.square = 2

        elif 3 <= self.row < 6:
            if 0 <= self.column < 3:
                self.square = 3

            elif 3 <= self.column < 6:
                self.square = 4

            else:
                self.square = 5

        else:
            if 0 <= self.column < 3:
                self.square = 6

            elif 3 <= self.column < 6:
                self.square = 7

            else:
                self.square = 8

    def set(self, value):
        assert 0 < value <= 9
        assert self.state == False
        self.value = value
        self.state = True
        self.possible_values = ""

    def is_valid(self):
        if type(self.id) == int and 0 <= self.id <= 81:
            return True
        return False

    def delete_pv(self, pv):

        assert type(pv) == str
        assert self.state == False

        old_pv = self.possible_values
        new_pv = ""
        for a in old_pv:
            if a != pv:
                new_pv = new_pv + a

        if self.possible_values != new_pv:
            self.counter.add()

        self.possible_values = new_pv
