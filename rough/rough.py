import sys
from datetime import datetime
import time
import html
import json
import requests
import matplotlib.pyplot as plt
import random

def get_questions():
    subject = input("Choose Subject:\n1. Computer Science\n2. Mathematics\n3. Science\n4. History\n5. Geography\n6. General Knowledge\n8. Politics
\n")
    amount = input("How many questions? ")
    response = requests.get(f"https://opentdb.com/api.php?amount={amount}")
    data = response.json()
    questions = data['results']
    score = 0
    for q in questions:
        print(html.unescape(q["question"]))

        if q["type"] == 'multiple':
            options = []
            options.extend([html.unescape(x) for x in q["incorrect_answers"]])
            options.append(html.unescape(q['correct_answer']))
            random.shuffle(options)
            for i, op in enumerate(options, start = 1):
                print(f'{i}. {op}')
            correct_option = options.index(q['correct_answer']) + 1
            i = 0
            while i <= 3:
                try:
                    user_ans = int(input('Answer: '))
                    selected_option = options[user_ans - 1]
                    if user_ans == correct_option:
                        print("Correct answer!")
                        score += 1
                        break
                    else:
                        if i == 3:
                            print(f"Correct answer: {q["correct_answer"]}")
                        else:
                            print("Oops.. Try again!")
                except ValueError:
                    print("Please enter valid option number.")
                except IndexError:
                    print("Please enter a valid option number.")

                i += 1

        if q["type"] == "boolean":
                try:
                    user_anstf = input("Answer(True/False): ").strip().capitalize()
                    if user_anstf in ["True", "false"]:
                        if user_anstf == (q["correct_answer"]):
                            print("Correct answer!")
                            score += 1
                            break
                        else:
                            print("Uh-ohh.. That was wrong!")
                            print(f'Correct answer: {q["correct_answer"]}')
                    else:
                        raise ValueError
                except ValueError:
                    print("This is a True/False question.")
                    print("Please enter only True or False.")
    print(f"Score: {score}/{amount}")

get_questions()
