import Block
import Block_groups
import Counter

class Field:
    def __init__(self, id, start):
        assert type(id) == int
        assert type(start) == str and len(start) == 81
        self.id = id
        self.block_list = []
        self.rows = []
        self.squares = []
        self.columns = []
        self.counter = Counter.Counter()

        for a in range(0, 81):
            self.block_list.append(Block.Block(a, start[a]))

        for a in range(9):
            self.rows.append(Block_groups.Row(self.setup_row(a), a))
            self.columns.append(Block_groups.Column(self.setup_column(a), a))
            self.squares.append(Block_groups.Square(self.setup_square(a), a))

    def setup_row(self, index):
        row = []
        for a in range(81):
            if self.block_list[a].row == index:
                row.append(self.block_list[a])

        return row

    def setup_column(self, index):
        column = []
        for a in range(81):
            if self.block_list[a].column == index:
                column.append(self.block_list[a])
        return column

    def setup_square(self, index):
        square = []
        for a in range(81):
            if self.block_list[a].square == index:
                square.append(self.block_list[a])
        return square

    def update_pv(self, index):

        block = self.block_list[index]
        state = block.state
        row = self.rows[block.row].row
        column = self.columns[block.column].column
        square = self.squares[block.square].square

        if state == False:
            for a in range(9):
                if row[a].state:
                    block.delete_pv(str(row[a].value))

                if column[a].state:
                    block.delete_pv(str(column[a].value))

                if square[a].state:
                    block.delete_pv(str(square[a].value))

                if block.counter.count > 0:
                    block.counter.reset()
                    self.counter.add()

            if len(block.possible_values) == 1:
                block.set(int(block.possible_values))


        """else:
            value = str(block.value)
            for a in range(9):
                if row[a].state == False:
                    row[a].delete_pv(value)
                    if row[a].counter.count > 0:
                        row[a].counter.reset()
                        self.counter.add()


                if column[a].state == False:
                    column[a].delete_pv(value)
                    if column[a].counter.count > 0:
                        column[a].counter.reset()
                        self.counter.add()


                if square[a].state == False:
                    square[a].delete_pv(value)
                    if square[a].counter.count > 0:
                        square[a].counter.reset()
                        self.counter.add()"""

    def last_value(self, index):
        block = self.block_list[index]

        if len(block.possible_values) == 1:
            block.set(int(block.possible_values))
            block.possible_values = ""

    def set_v(self, index):
        block = self.block_list[index]
        block_row = self.rows[block.row].row
        block_column = self.columns[block.column].column
        block_square = self.squares[block.square].square

        for a in block.possible_values:
            for b in range(9):
                for c in block_row[b].possible_values:
                    if a == c:
                        return

                for c in block_column[b].possible_values:
                    if a == c:
                        return

                for c in block_square[b].possible_values:
                    if a == c:
                        return

            #block.value = str(a)
            #block.counter.add()

    def check_false(self):
        for a in self.block_list:
            if a.state == False:
                return False

        return True

    def plot(self, type):
        for a in range(9):
            row = []
            for b in range(9):
                if type == "id":
                    row.append(self.rows[a].row[b].id)

                elif type == "pv":
                    row.append(self.rows[a].row[b].possible_values)

                elif type == "value":
                    row.append((self.rows[a].row[b].value))

                elif type == "row":
                    row.append((self.rows[a].row[b].row))

                elif type == "column":
                    row.append((self.rows[a].row[b].column))

                elif type == "square":
                    row.append((self.rows[a].row[b].square))

                elif type == "state":
                    row.append((self.rows[a].row[b].state))

            print(row)

    def export(self):
        output = []
        for a in self.block_list:
            if a.state == False:
                for b in a.possible_values:
                    new_field = ""
                    for c in self.block_list:
                        if a == c:
                            new_field = new_field + b

                        else:
                            new_field = new_field + str(c.value)

                    output.append(new_field)

                assert len(a.possible_values) == len(output)

                return output




        return output

    def export_solution(self):
        solution = ""
        for a in self.block_list:
            solution = solution + str(a.value)

        return solution

    def check(self):
        row = self.rows
        column = self.columns
        square = self.squares

        for a in range(9):
            for b in range(9):
                r = row[a].row[b].value
                c = column[a].column[b].value
                s = square[a].square[b].value
                for d in range(9):
                    if d != b:
                        r2 = row[a].row[d].value
                        c2 = column[a].column[d].value
                        s2 = square[a].square[d].value

                        if r == r2 or c == c2 or s == s2 or r == 0 or c == 0 or s == 0:
                            return False

        return True

    def check_start_field(self):
        row = self.rows
        column = self.columns
        square = self.squares

        for a in range(9):
            for b in range(9):
                r = row[a].row[b].value
                c = column[a].column[b].value
                s = square[a].square[b].value
                for d in range(9):
                    if d != b:
                        r2 = row[a].row[d].value
                        c2 = column[a].column[d].value
                        s2 = square[a].square[d].value

                        if (r == r2 or c == c2 or s == s2) and r != 0 and c != 0 and s != 0:
                            return False

        return True

    def check_sudoku(self):
        row = self.rows
        column = self.columns
        square = self.squares

        for a in range(9):
            for b in range(9):
                r = row[a].row[b].value
                c = column[a].column[b].value
                s = square[a].square[b].value
                for d in range(9):
                    if d != b:
                        r2 = row[a].row[d].value
                        c2 = column[a].column[d].value
                        s2 = square[a].square[d].value

                        if (r == r2 or c == c2 or s == s2) and r != 0 and c != 0 and s != 0:
                            if r == r2:
                                print("similar values in: " + str(row[a].row[b].column) + " " + str(
                                    row[a].row[b].row) + " and " + str(row[a].row[d].column) + " " + str(
                                    row[a].row[d].row))

                            elif c == c2:
                                print("similar values in: " + str(column[a].column[b].column) + " " + str(
                                    column[a].column[b].row) + " and " + str(column[a].column[d].column) + " " + str(
                                    column[a].column[d].row))

                            elif s == s2:
                                print("similar values in: " + str(square[a].square[b].column) + " " + str(
                                    square[a].square[b].row) + " and " + str(square[a].square[d].column) + " " + str(
                                    square[a].square[d].row))

                            return False

        return True




