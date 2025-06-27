class QuizBrain:
    score = 0 
    
    def __init__(self, list_question):
        self.question_number = 0
        self.question_list = list_question
    
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    
    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            print("That's correct.")
            QuizBrain.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer is: {correct_answer}.\nYour current score is {QuizBrain.score}/{self.question_number}.")        
    
    def new_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(user_answer, (question.answer))
        print("\n")
        
    
