class QuizBrain:
    def __init__(self, question_list):
        # Self referenziert immer auf das aktuelle Objekt.
        self.question_number = 0
        self.question_list = question_list
        self.correct_answer = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.still_has_questions() == True:
            question_Object = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {question_Object.text} (True/False)?: ")

            self.check_answer(user_answer, question_Object)
        else:
            raise Exception("No more questions left!")   
          

    def check_answer(self, current_answer, question_Object):
        if current_answer.lower() == question_Object.answer.lower(): 
            self.correct_answer += 1
            print("You got it right!")
            print(f"The correct answer was: {question_Object.answer}")
            print(f"Your current score is: {self.correct_answer} / {self.question_number}\n")   
        else:    
            print("You got it wrong!")
            print(f"Your current score is: {self.correct_answer} / {self.question_number}\n")   


     

