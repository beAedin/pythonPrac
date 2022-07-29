from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
score=0


# Create quesions (using Class)
for i in question_data:
    new_q = i["text"]
    new_answer = i["answer"]
    data = Question(new_q, new_answer)
    question_bank.append(data)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")