from data import question_data
from question_model import Question
from quiz_brain import Quiz
questionBank=[]
q1='query'
for i in range(len(question_data)):
    txt=question_data[i]["text"]
    ans=question_data[i]["answer"]
    item=Question(txt,ans)
    questionBank.append(item)

score=0
q1=0
quiz=Quiz(questionBank)
totalQues=len(questionBank)
while quiz.still_has_Question():
    answer=quiz.next_Question()


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.questionNum}")
