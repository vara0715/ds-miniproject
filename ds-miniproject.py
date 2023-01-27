from random import choice
import random

name = input("Enter your name : ")

class Question:
     def __init__(self,prompt,answer):
            self.prompt = prompt
            self.answer = answer         
            
            
question_prompts = open("question.txt", "r") 
content = question_prompts.read()


questions = [
    Question(content[1:124],"a"),
    Question(content[124:274],"b"),
    Question(content[274:579],"c"),
    Question(content[579:719],"a"),
    Question(content[719:811],"a"),
    Question(content[811:983],"b"),
    Question(content[983:1051],"a"),
    Question(content[1051:1231],"c"),
    Question(content[1231:1375],"c"),
    Question(content[1375:1541],"b"), 
]                          
random.shuffle(questions)
             

def run_quiz(questions):
    score=0
    for question in questions:
        answer= input(question.prompt)
        if answer == question.answer:
             score += 1
    print(f"Hey!",name, "you got" ,score, "out of", len(questions))
run_quiz(questions) 
