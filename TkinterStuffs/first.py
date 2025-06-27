import tkinter


window = tkinter.Tk()
window.title("My first GUI")
window.minsize(500, 300)

my_label = tkinter.Label(text="I am a guy", font=("Arial", 20, "italic"))
my_label.pack()

def button_click():
    print("I got clicked")
    # my_label["text"] = entry.get()
    my_label.config(text=entry.get())

button = tkinter.Button(text="Click me", command=button_click)
button.pack()

entry = tkinter.Entry()
entry.pack()

window.mainloop()
