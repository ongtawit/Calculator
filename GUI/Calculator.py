from tkinter import *


def press(char):
    if char == ' = ':
        equalpress()  # Call equalpress when '=' is pressed
    elif char == 'Clear':
        clear()
    else:
        equation.set(equation.get() + char)


def equalpress():
    try:
        # evaluate the expression using the eval function
        total = str(eval(equation.get()))

        equation.set(total)
    except:
        equation.set("error")


def clear():
    equation.set("")


if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    # create Buttons and place them using grid
    buttons = []

    for i in range(1, 10):
        button = Button(gui, text=f' {i} ', fg='black', bg='red', command=lambda num=i: press(str(num)), height=1, width=7)
        button.grid(row=(i - 1) // 3 + 2, column=(i - 1) % 3, sticky="nsew")
        buttons.append(button)

    # Additional buttons
    additional_buttons = [
        (' 0 ', 5, 0),
        (' + ', 2, 3),
        (' - ', 3, 3),
        (' * ', 4, 3),
        (' / ', 5, 3),
        (' = ', 5, 2),
        ('Clear', 5, 1),
        ('.', 6, 0)
    ]

    for text, row, column in additional_buttons:
        button = Button(gui, text=text, fg='black', bg='red', command=lambda t=text: press(t), height=1, width=7)
        button.grid(row=row, column=column, sticky="nsew")
        buttons.append(button)

    # Configure grid to resize buttons along with window
    for i in range(6):
        gui.grid_columnconfigure(i, weight=1)

    for i in range(7):
        gui.grid_rowconfigure(i, weight=1)

    # start the GUI
    gui.mainloop()
