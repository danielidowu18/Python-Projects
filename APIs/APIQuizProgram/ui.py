from tkinter import *
from quiz_brain import QuizBrain


theme_colour = "#375362"


class QuizUi():

    
    def __init__(self, quiz_object: QuizBrain):
        self.quiz_obj = quiz_object
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=theme_colour)
        
        self.score_label = Label(text=f"Score: {self.quiz_obj.score}", font=("Arial", 16), bg=theme_colour, fg="white")
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_canvas = self.canvas.create_text(150, 125,
                                                       text="Testing",
                                                       width=280,
                                                       font=("Arial", 20, "italic"),
                                                       fill=theme_colour)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_image = PhotoImage(file="./APIs/APIQuizProgram/images/true.png")
        false_image = PhotoImage(file="./APIs/APIQuizProgram/images/false.png")
        self.true_button = Button(image=true_image, bg=theme_colour, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0)
        
        self.false_button = Button(image=false_image, bg=theme_colour, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)
        
        self.get_new_question()
        
        self.window.mainloop()
        
        
    def get_new_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz_obj.score}")
        if self.quiz_obj.still_has_questions():
            q_text = self.quiz_obj.new_question()
            self.canvas.itemconfig(self.question_canvas, text=q_text)
        else:
            self.canvas.itemconfig(self.question_canvas,
                                   text=f"You've completed the quiz.\nYour final score is {self.quiz_obj.score}/{self.quiz_obj.question_number}.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    
    def true_answer(self):
        is_right = self.quiz_obj.check_answer("True")
        self.give_feedback(is_right)
        
        
    def false_answer(self):
        is_right = self.quiz_obj.check_answer("False")
        self.give_feedback(is_right)
        
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_new_question)
        

