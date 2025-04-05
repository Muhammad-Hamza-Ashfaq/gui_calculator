# CodexCue Python Internship -- Project-1__GUI_CALCULATOR
# Muhammad Hamza Ashfaq -- h.ashfaq16@gmail.com
import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python GUI Calculator")
        self.root.geometry("350x350+500+100")
        self.root.resizable(False, False)
        self.entry = tk.Entry(root, font=("Arial", 20), justify='right', bd=10)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0

        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, font=("Arial", 14),
            command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            
            col += 1
            if col > 3:
                col = 0
                row += 1



    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        
        elif char == '=':
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")

        else:
            self.entry.insert(tk.END, char)        

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
