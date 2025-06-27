import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

def labels(text, font, r, c):
    label = tkinter.Label(text=text, font=font)
    label.grid(row=r, column=c)
    
def button_click():
    number = int(entry.get())
    km = round(number * 1.609, 1)
    answer["text"] = km

entry = tkinter.Entry(font=("Arial", 15), width=10)
entry.grid(row=0, column=1)

labels(text="is equal to", font=("Arial", 15), r=1, c=0)
labels(text="Miles", font=("Arial", 15), r=0, c=2)
answer = tkinter.Label(text="0", font=("Arial", 15))
answer.grid(row=1, column=1)
labels(text="Km", font=("Arial", 15), r=1, c=2)

button = tkinter.Button(text="Calculate", font=("Arial", 15), command=button_click)
button.grid(row=2, column=1)

window.mainloop()