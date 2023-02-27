class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_question(self):
        return not (self.question_number > len(self.question_list)-1)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f'Q.{self.question_number}: {current_question.text} (True/ False): ')
        self.check_answer(user_ans, current_question)

    def check_answer(self, user_ans, current_question):
        if user_ans.lower() == current_question.answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"Current score = {self.score}/{self.question_number}\n")



