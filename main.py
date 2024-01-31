import enigma
import tkinter as tk

app = tk.Tk()
app.option_add('*Label.foreground', 'white')
app.option_add('*Label.background', 'black')

def call_enigma():
    print("To build")

def appli():
    app.title("Enigma Machine")
    app.geometry("500x500")
    app.config(bg="black")

    lab1 = tk.Label(app, text="Rotors position:")

    bu_call = tk.Button(app, text="Send request to Enigma", command=call_enigma)

    #In build ...

if __name__ == "__main__":
    enigma.launch_machine()

    # A changer par:
    #appli()