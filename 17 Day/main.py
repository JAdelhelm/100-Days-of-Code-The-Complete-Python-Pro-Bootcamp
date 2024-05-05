
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


if __name__ == '__main__':
    # Liste von Quesiton - Objekten
    question_bank = [
        Question(question_data[val]["text"],question_data[val]["answer"]) 
        for val in range(len(question_data))
        ]
    quiz = QuizBrain(question_bank)
    while True:
        quiz.next_question()
    

    # print(len(question_bank)) 12


