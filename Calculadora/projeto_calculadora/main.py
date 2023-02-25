import tkinter as tk

window = tk.Tk()
window.geometry("400x380")
window.resizable(0, 0)
window.title("Calculadora")

input_value = ""

display_text = tk.StringVar()


# Funcão para das update no input ao clicar em um número
def click_button(item):
    global input_value
    input_value = input_value + str(item)
    display_text.set(input_value)


# Função para limpar o display
def clear_button():
    global input_value
    input_value = ""
    display_text.set("")


# Função para fazer calculos matemáticos
def equal_button():
    global input_value
    try:
        result = str(eval(input_value))
        if result == 'inf':
            raise ZeroDivisionError("Division by zero")
        elif result == '..':
            raise ValueError("Invalid input")
        else:
            display_text.set(result)
    except ZeroDivisionError:
        display_text.set("Error: Division by zero")
    except ValueError:
        display_text.set("Error: Invalid input")
    except:
        display_text.set("Error: More than 1 dot")
    input_value = ""


def create_button(frame, text, fg, width, height, bd, bg, cursor, command, row, column, columnspan=1):
    return tk.Button(frame, text=text, fg=fg, width=width, height=height, bd=bd, bg=bg, cursor=cursor,
                     command=command).grid(row=row, column=column, columnspan=columnspan, padx=1, pady=1)


# Criando os Frames de cada bloquinho

input_frame = tk.Frame(window, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                       highlightthickness=2)

input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=display_text, width=50, bg="#eee", bd=0,
                       justify=tk.RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)  # 'ipady' para ajustar o padding dentro do frame

# -------------------------------------------------------
# Frame das linhas dos botões

buttons_frame = tk.Frame(window, width=400, height=272.5, bg="gray")

buttons_frame.pack()

# 1º Linha

create_button(buttons_frame, "C", "black", 45, 3, 0, "#eee", "hand2", lambda: clear_button(), 0, 0, 3)
create_button(buttons_frame, "/", "black", 10, 3, 0, "#eee", "hand2", lambda: click_button("/"), 0, 3)

# 2º Linha

create_button(buttons_frame, "7", "black", 10, 3, 0, "#fff", "hand2", lambda: click_button(7), 1, 0)
create_button(buttons_frame, "8", "black", 10, 3, 0, "#fff", "hand2", lambda: click_button(8), 1, 1)
create_button(buttons_frame, "9", "black", 10, 3, 0, "#fff", "hand2", lambda: click_button(9), 1, 2)
create_button(buttons_frame, "X", "black", 10, 3, 0, "#eee", "hand2", lambda: click_button("*"), 1, 3)

# 3º Linha

create_button(buttons_frame, "4", "black", 10, 3, 0, "#fff", "hand2", lambda: click_button(4), 2, 0)
create_button(buttons_frame, "5", "black", 10, 3, 0, "#fff", "hand2", lambda: click_button(5), 2, 1)
create_button(buttons_frame, "6", "black", 10, 3, 0, "#fff", "hand2", lambda: click_button(6), 2, 2)
create_button(buttons_frame, "-", "black", 10, 3, 0, "#eee", "hand2", lambda: click_button("-"), 2, 3)

# 4º Linha

create_button(buttons_frame, "1", "black", 10, 3, 0, "#fff", "hand2", lambda: click_button(1), 3, 0)
create_button(buttons_frame, "2", "black", 10, 3, 0, "#fff", "hand2", lambda: click_button(2), 3, 1)
create_button(buttons_frame, "3", "black", 10, 3, 0, "#fff", "hand2", lambda: click_button(3), 3, 2)
create_button(buttons_frame, "+", "black", 10, 3, 0, "#eee", "hand2", lambda: click_button("+"), 3, 3)

# 5º Linha

create_button(buttons_frame, "0", "black", 20, 3, 0, "#fff", "hand2", lambda: click_button(0), 4, 0)
create_button(buttons_frame, ".", "black", 10, 3, 0, "#eee", "hand2", lambda: click_button("."), 4, 2)
create_button(buttons_frame, "=", "black", 10, 3, 0, "#eee", "hand2", lambda: equal_button(), 4, 3)

# Run main loop
window.mainloop()
