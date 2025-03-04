import tkinter as tk

#Create a class
class BasicCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("The Basic Calculator")  #Set the window title

        self.result = tk.StringVar()  #This will store the result

        #Set the background color of the main window to blue
        self.root.config(bg="blue")

        #Create a display for the result
        self.result_display = tk.Entry(self.root, textvariable=self.result,
        font=("Times new roman", 16), bd=8, relief="ridge", justify="left")
        self.result_display.grid(row=0, column=0, columnspan=4)
        self.result_display.config(bg="lightgray", fg="black")

        #Buttons for digits and operations
        buttons = [("7", 1, 0), ("8", 1, 1),
            ("9", 1, 2), ("4", 2, 0),
            ("5", 2, 1), ("6", 2, 2),
            ("1", 3, 0), ("2", 3, 1),
            ("3", 3, 2), ("0", 4, 1),
            ("+", 1, 3), ("-", 2, 3),
            ("*", 3, 3), ("/", 4, 3),
            ("C", 4, 0), ("=", 4, 2)]

        #Create buttons for the calculator
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=10, height=3,
            font=("Times new roman", 14),
            command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)
            button.config(bg="blue", fg="white")

    #Function to handle button click events
    def on_button_click(self, char):
        if char == "C":
            self.result.set("")  #Clear the display
        elif char == "=":
            try:
                #Evaluate the expression and show the result
                result = eval(self.result.get())
                self.result.set(result)
                
            except Exception as e:
                self.result.set("Error, try again")
        else:
            #Append the character to the current input
            current = self.result.get()
            self.result.set(current + char)
#Create the main window
root = tk.Tk()
#Create a BasicCalculator object
calc = BasicCalculator(root)
#Run the GUI
root.mainloop()
