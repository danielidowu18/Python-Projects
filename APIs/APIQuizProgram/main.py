import question_model
from data import question_data
import quiz_brain
from ui import QuizUi


question_bank = []
for text in question_data:
    question = text["question"]
    answer = text["correct_answer"]
    new_question_in_list = question_model.Question(question, answer)
    question_bank.append(new_question_in_list)
    
    
quiz = quiz_brain.QuizBrain(question_bank)
interface = QuizUi(quiz)
