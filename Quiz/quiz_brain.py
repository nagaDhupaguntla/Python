class Quiz:
    def __init__(self, question_list):
        self.questionNum = 0
        self.listOfQues = question_list
        self.score=0
    def still_has_Question(self):
        return self.questionNum<len(self.listOfQues)
    def next_Question(self):
        current_Question = self.listOfQues[self.questionNum]
        self.questionNum +=1
        answer=input(f'Q{self.questionNum},{current_Question.text},?  True/False  :')
        self.check_answer(answer, current_Question.answer)



    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.questionNum}")
        print("\n")

