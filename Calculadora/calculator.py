import tkinter as tk
import math


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Entry widget for displaying calculation results
        self.display = tk.Entry(master, width=40, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Create button layout for basic math functions
        self.basic_buttons = [
            "7", "8", "9", "+", "C",
            "4", "5", "6", "-", "(",
            "1", "2", "3", "*", ")",
            "0", ".", "/", "="
        ]

        # Create button layout for scientific math functions
        self.scientific_buttons = [
            "π", "sin", "cos", "tan", "log",
            "e", "asin", "acos", "atan", "ln",
            "x²", "x³", "xʸ", "√", "!",
            "(", ")", "C", "±", "AC"
        ]

        # Create and place basic math function buttons
        self.create_buttons(self.basic_buttons, 1, 0)

        # Create and place scientific math function buttons
        self.create_buttons(self.scientific_buttons, 1, 5)

        # Bind buttons to the button_click method
        for button in self.buttons:
            button.bind('<Button-1>', self.button_click)

    def create_buttons(self, buttons, row, column):
        self.buttons = []
        for i in range(len(buttons)):
            self.buttons.append(
                tk.Button(self.master, text=buttons[i], padx=20, pady=10, font=('Helvetica', 10, 'bold')))
            self.buttons[-1].grid(row=i // 5 + row, column=i % 5 + column)

    def button_click(self, event):
        button = event.widget
        text = button['text']

        # If the user clicks the "=" button, evaluate the expression in the display
        if text == "=":
            try:
                result = str(eval(self.display.get()))
                if result == 'inf':
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "Error: Division by zero")
                else:
                    self.display.delete(0, tk.END)
                    self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")

        # If the user clicks the "C" button, clear the display
        elif text == "C":
            self.display.delete(0, tk.END)

        # If the user clicks the "AC" button, clear the display and the memory
        elif text == "AC":
            self.display.delete(0, tk.END)

        # If the user clicks any other button, add its text to the display
        else:
            self.display.insert(tk.END, text)


# Create the main Tkinter window and Calculator object
root = tk.Tk()
my_calculator = Calculator(root)

# Start the main event loop
root.mainloop()
