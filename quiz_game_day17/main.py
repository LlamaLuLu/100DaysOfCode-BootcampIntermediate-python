# 13/6/2023

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# converting str -> obj
question_bank = []
for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))  # adds new question

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

