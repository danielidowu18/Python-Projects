from math import floor
import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_click():
    canvas.after_cancel(timer)
    timer_label.config(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
    check_label.config(text="")
    canvas.itemconfig(count_text, text="00:00")
    global reps
    reps = 0 
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_click():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)        
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)        
        count_down(work_sec)    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    
    if count > 0:
        global timer
        timer = canvas.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 1:
            check_label.config(text="✔️")
        else:    
            check_label.config(text="")
        start_click()
    canvas.itemconfig(count_text, text=f"{count_min}:{count_sec}")
    

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
# window.minsize(300, 200)
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = tkinter.Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato = tkinter.PhotoImage(file="./TkinterStuffs/pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato)
count_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", font=(FONT_NAME, 15, "bold"), width=5, height=1, command=start_click)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 15, "bold"), width=5, height=1, command=reset_click)
reset_button.grid(row=2, column=2)

check_label = tkinter.Label(text="", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
check_label.place(y=300, x=150)

window.mainloop()
