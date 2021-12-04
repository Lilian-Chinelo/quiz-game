from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
if not quiz.still_has_questions():
    print("You have completed the quiz!")
    print(f"Your final score is: {quiz.score} / {quiz.question_number}. ")












# class User:
#     def __init__(self, username, user_id):
#         self.username = username
#         self.user_id = user_id
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
#
# user_1 = User("Lilian", 12)
# user_2 = User("Jon", 13)
#
# user_1.follow(user_2)
#
# # print(user_1.following)
# # print(user_1.followers)
#
# print(user_2.followers)
# print(user_2.following)
