from html import unescape

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = unescape(self.current_question.text)
        return q_text

    def check_answer(self, user_answer: str) -> bool:
        correct_answer = self.current_question.answer

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
