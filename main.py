from tkinter import *
import Counter
import Field
import time
import UI
# import Block
# import Block_groups

t1 = time.time()
field_counter = Counter.Counter()
field_counter.count = 1
solution_counter = Counter.Counter()
solutions = []


def plot(field):
    print("Values in Field " + str(field.id) + ":")
    field.plot("value")
    print("\n")


def run(field):
    assert field.check_start_field()
    fields = []
    c = Counter.Counter()
    field.counter.add()


    while field.counter.count > 0:
        field.counter.reset()
        for a in range(81):
            field.update_pv(a)

            if field.block_list[a].state == False and field.block_list[a].possible_values == "":
                return


    if field.check():
        plot(field)
        t2 = time.time()
        print(t2 - t1)

    else:

        start_fields = field.export()

        for a in start_fields:
            fields.append(Field.Field(field_counter.count, a))
            field_counter.add()

        for a in fields:
            run(a)
            c.add()

        assert c.count == len(fields)


def output_ui(ui):
    solution = ""
    solutions.clear()
    value_counter = Counter.Counter()
    field = Field.Field(0, ui.build_string())
    for a in ui.build_string():
        if a != "0":
            value_counter.add()

    if value_counter.count < 15:
        If.field.delete(0, END)
        If.field.insert(0, "Zu wenige Eingaben")
        return


    if not field.check_start_field():
        If.field.delete(0, END)
        If.field.insert(0, "Keine Lösung")
        return

    run_ui(field)
    if len(solutions) > 0:
        solution = solutions[0]
        ui.write(solution)
        ui.field.delete(0, END)
        ui.field.insert(0, "Lösung 1 / " + str(len(solutions)))


def run_ui(field):
    fields = []
    c = Counter.Counter()
    field.counter.add()

    while field.counter.count > 0:
        field.counter.reset()
        for a in range(81):
            field.update_pv(a)

            if field.block_list[a].state == False and field.block_list[a].possible_values == "":
                return

    if field.check():
        solutions.append(field.export_solution())

    else:

        start_fields = field.export()

        for a in start_fields:
            fields.append(Field.Field(field_counter.count, a))
            field_counter.add()

        for a in fields:
            run_ui(a)
            c.add()

        assert c.count == len(fields)


def next_output(ui):
    if len(solutions) > 1:

        if solution_counter.count < len(solutions) - 1:
            solution_counter.add()
            ui.write(solutions[solution_counter.count])
            ui.field.delete(0, END)
            ui.field.insert(0, "Lösung " + str(solution_counter.count + 1) + " / " + str(len(solutions)))


def previous_output(ui):
    if solution_counter.count > 0:
        solution_counter.sub()
        ui.write(solutions[solution_counter.count])
        ui.field.delete(0, END)
        ui.field.insert(0, "Lösung " + str(solution_counter.count + 1) + " / " + str(len(solutions)))


start_field1 = "000300002000592084050006000306910007070008900508240600900000000200800306000460010"
start_field2 = "408030005070000002010007000004000300890700060600095000980304500302800910100200080"
start_field2_1 = "408000005070000002010007000004000300890700060600095000980304500302800910100200080"
start_field3 = "093070060080000000000600001800000030034009005100040000000005200067090010400000000"
start_field4 = "005008069060240001000001073000000000150382000084906050001020906070804030000000700"

"""
f1 = Field.Field(0, start_field3)
plot(f1)
if f1.check_start_field():
    run(f1)
else:
    print("No possible solution")
"""

If = UI.Input_Field()
If.write(start_field2_1)
If.solve_button = Button(If.root, text="lösen", command=lambda: output_ui(If))
If.solve_button.grid(row=10, column=3, columnspan=3)
If.next_button = Button(If.root, text=">>", command=lambda: next_output(If))
If.next_button.grid(row=10, column=9)
If.previous_button = Button(If.root, text="<<", command=lambda: previous_output(If))
If.previous_button.grid(row=10, column=0)
If.clear = Button(If.root, text="löschen", command=If.clear)
If.clear.grid(row=10, column=2, columnspan=2)
If.field = Entry(If.root)
If.field.insert(0, "nicht gelöst")
If.field.grid(row=10, column=6, columnspan=3)
If.root.mainloop()
