import sys
from datetime import datetime
import time
import html
import json
import requests
import matplotlib.pyplot as plt
import random

def get_questions():
    amount = input("How many questions? ")
    response = requests.get(f"https://opentdb.com/api.php?amount={amount}")
    data = response.json()
    questions = data['results']
    for q in questions:
        print(html.unescape(q["question"]))

        if q["type"] == 'multiple':
            options = []
            options.extend([html.unescape(x) for x in q["incorrect_answers"]])
            options.append(html.unescape(q['correct_answer']))
            random.shuffle(options)
            for i, op in enumerate(options, start = 1):
                print(f'{i}. {op}')
            correct_option = options.index('correct_answer') + 1
            i = 0
            while i <= 3:
                try:
                    user_ans = int(input('Answer: '))
                    selected_option = options[user_ans - 1]
                except ValueError:
                    print("Please enter valid option number.")
                except IndexError:
                    print("Please enter a valid option number.")
                if user_ans == correct_option:
                    print("Correct answer!")
                    break
                else:
                    if i == 3:
                        print(f"Correct answer: {q["correct_answer"]}")
                    else:
                        print("Oops.. Try again!")
                i +=1

        if q["type"] == "boolean":
            while True:
                user_anstf = input("Answer(True/False): ").strip().lower()
                if user_anstf in ["true", "false"]:
                    break

                print("This is a True/False question.")
                print("Please enter only True or False.")


get_questions()
