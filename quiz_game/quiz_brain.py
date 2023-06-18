# TODO: asking questions
# TODO: checking if answer correct
# TODO: check if at end of quiz

class QuizBrain:

    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_no < len(self.question_list)  # shorter way to run boolean; either True/False

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question.text} (True/False)?\n")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct):
        if (user_answer.lower() == correct.lower()) or (user_answer.lower() == correct[0].lower()):
            print("You got it right!")
            self.score += 1
        else:
            print("Whomp, whomp... that's not right.")
        print(f"The correct answer was {correct}.")
        if self.still_has_question():
            print(f"Your current score is: {self.score}/{self.question_no}\n")
        else:
            print("\nYou've completed the quiz!")
            print(f"Your final score is: {self.score}/{len(self.question_list)}")


