from data import question_data

class Question:
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer


q1=question_data[0]['text']
ans1=question_data[0]['answer']
print(q1,ans1)
ques=Question(q1,ans1)