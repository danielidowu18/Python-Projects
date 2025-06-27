import html


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
    
    
    def check_answer(self, user_input):
        if user_input == self.question.correct_answer:
            self.score += 1
            return True
        else:
            return False
    
    
    def new_question(self):
        self.question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(self.question.question)} (True/False)?: "
        
