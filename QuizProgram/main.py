import question_model
from data import question_data
import quiz_brain



question_bank = []
for question in question_data:
    tex = question["text"]
    ans = question["answer"]
    new_question_in_list = question_model.Question(tex, ans)
    question_bank.append(new_question_in_list)
    

quiz = quiz_brain.QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.new_question()

print(f"You've completed the quiz.\nYour final score is {quiz.score}/{quiz.question_number}.")    