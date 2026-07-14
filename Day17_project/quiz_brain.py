class QuizBrain:
    def __init__(self,q_list):
        self.q_no=0
        self.q_list=q_list
        self.score=0

    def next_question(self):
        current_ques=self.q_list[self.q_no]
        self.q_no+=1
        user_ans=input(f"Q.{self.q_no}: {current_ques.text} (True/False): ")
        self.check_answer(user_ans,current_ques.answer)
        print("\n")

    def continue_questions(self):
        return self.q_no < len(self.q_list)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()== correct_answer.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("Oops!You got it wrong")
            print(f"Correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.q_no}")




