

#Step 1: Import Tkinter libraries to create the graphical interface. goto:#Tag1
#Step 2: Import math functions for calculations.
#Step 3: Create functions for the calculator.
  #Function to update the display: Adds new characters to the current expression.
  #Function to perform calculations: Calculates the current expression and displays the result.
  #Function to update history: Saves the history of your calculations.
  #Function to clear the display: Clears the display.
  #Function to delete the last character: Removes the last character from the display.
#Step 4: Main application window - Create the main window of Tkinter.
#Step 5: Create variables to store the current expression.
#Step 6: Display and History
  #Create a label to display the current expression.
  #Create a text box for the calculation history.
#Step 7: Create buttons
  #Create buttons for all numbers, operators, and special functions.
#Step 8: Place buttons
  #Place all the buttons on the main window in a grid.
#Step 9: Run the application
  #Run the main Tkinter loop to display the application window.
#Step 10: Testing
  #Test my application with various examples.




import tkinter as tk
from tkinter import PhotoImage #add my photo
from math import sin, cos, tan, exp, log, sqrt, pi


#function to update the display
def update_display(value):
    current = display_var.get()
    display_var.set(current + value)

#function to perform calculations
def calculate():
    try:
        expression = display_var.get()
        result = eval(expression)
        display_var.set(result)
        update_history(expression, result)
    except:
        display_var.set("Error")

#function to update the history
def update_history(expression, result):
    history_text.insert(tk.END, f"{expression} = {result}\n")
    history_text.see(tk.END)

#function to clear the display
def clear_display():
    display_var.set("")

#function to remove the last digit
def remove_digit():
    current = display_var.get()
    display_var.set(current[:-1])

#function to calculate the sine of a number
def calculate_sin():
    try:
        value = float(display_var.get())
        result = sin(value)
        display_var.set(result)
        update_history(f"sin({value})", result)
    except:
        display_var.set("Error")

#function to add a closing bracket
def add_closing_bracket():
    current = display_var.get()
    display_var.set(current + ")")

#define commands for buttons
def add_seven(): update_display("7")
def add_eight(): update_display("8")
def add_nine(): update_display("9")
def add_divide(): update_display("/")
def add_four(): update_display("4")
def add_five(): update_display("5")
def add_six(): update_display("6")
def add_multiply(): update_display("*")
def add_one(): update_display("1")
def add_two(): update_display("2")
def add_three(): update_display("3")
def add_minus(): update_display("-")
def add_zero(): update_display("0")
def add_dot(): update_display(".")
def add_plus(): update_display("+")
def add_cos(): update_display("cos(")
def add_tan(): update_display("tan(")
def add_power(): update_display("**")
def add_exp(): update_display("exp(")
def add_log(): update_display("log(")
def add_sqrt(): update_display("sqrt(")
def add_pi(): update_display(str(pi))
def add_open_bracket(): update_display("(")

#add my photo to see the author by click on the name of the calc
def show_my_photo(event): 
    new_window = tk.Toplevel(app)
    new_window.title("My Photo")
    photo = tk.PhotoImage(file="my_photo.png") 
    photo_label = tk.Label(new_window, image=photo)
    photo_label.photo = photo
    photo_label.pack()

#main application window
app = tk.Tk()
app.title("Bosenko Calculator Project")

# Create the title label
title_label = tk.Label(app, text="Calculator by Bosenko Nick", font=("Arial", 16, 'bold'))
title_label.grid(row=0, column=0, columnspan=4, padx=10, pady=5, )
title_label.bind("<Button-1>", show_my_photo)  # show my photo - click on the name of the calc

#variable to hold the display value
display_var = tk.StringVar()
display_var.set("")

#create the display label
display_label = tk.Label(app, textvariable=display_var, font=("Helvetica", 20))
display_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

#text widget to display history
history_text = tk.Text(app, height=5, width=35, font=("Helvetica", 12))
history_text.grid(row=2, column=0, columnspan=5, padx=10, pady=10)

buttons = [
      ("7", add_seven), 
    ("8", add_eight),
    ("9", add_nine), 
    ("/", add_divide),
    ("4", add_four), 
    ("5", add_five),
    ("6", add_six), 
    ("*", add_multiply),
    ("1", add_one), 
    ("2", add_two),
    ("3", add_three), 
    ("-", add_minus),
    ("0", add_zero), 
    (".", add_dot),
    ("=", calculate), 
    ("+", add_plus),
    ("sin", calculate_sin), 
    ("cos", add_cos),
    ("tan", add_tan), 
    ("^", add_power),
    ("exp", add_exp), 
    ("log", add_log),
    ("sqrt", add_sqrt), 
    ("pi", add_pi),
    ("(", add_open_bracket), 
    (")", add_closing_bracket),
    ("Clear", clear_display), 
    ("<-", remove_digit),
]

#place buttons in a grid
row_num, col_num = 3, 0
for (text, command) in buttons:
    button = tk.Button(app, text=text, command=command, padx=20, pady=20, font=("Helvetica", 15),
    width=4, height=2)
    button.grid(row=row_num, column=col_num, padx=2)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 2

#start the Tkinter main loop
app.mainloop()