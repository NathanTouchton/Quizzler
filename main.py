from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    QUESTION_TEXT = question["question"]
    QUESTION_ANSWER = question["correct_answer"]
    new_question = Question(QUESTION_TEXT, QUESTION_ANSWER)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
