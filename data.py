from questions import question_list
from answers import answer_list
import random

question_data = []

for i in range(160):
    question_data.append({"text" : question_list[i+1] , "answer":answer_list[i]})
random.shuffle(question_data)