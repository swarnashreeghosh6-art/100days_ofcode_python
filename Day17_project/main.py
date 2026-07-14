from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
l=len(question_data)
for i in range(l):
    q_text=question_data[i]["question"]
    q_answer = question_data[i]["correct_answer"]
    question=Question(q_text,q_answer)
    question_bank.append(question)

quiz=QuizBrain(question_bank)

while quiz.continue_questions():
    quiz.next_question()
print("YOU HAVE COMPLETED THE QUIZ!")
print(f"Your final score is {quiz.score}/{quiz.q_no}")
