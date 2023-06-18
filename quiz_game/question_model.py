from data import *
import random

# class Question:
#
#     def __init__(self):
#         quiz = random.choice(question_data)
#         self.question = quiz["text"]  # text
#         self.answer = quiz["answer"]  # answer
#
# new_q = Question()
# print(new_q.question)

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

new_q = Question("slay queen", True)
print(new_q.text)
