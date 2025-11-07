import random


def generate_question(level):
    if level <= 10:
        if level == 1: 
            a = random.randint(1, 10)
            
        question = f"{a}"
    else :
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split(", ")
        if level == 11:
            a = "12 / 4 + 7"
        elif level == 15:
            question = "Terdapat pola ABCDABCDABCD \n Apa huruf ke-2018?"
            
        
        