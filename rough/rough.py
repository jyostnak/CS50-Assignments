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
        user_ans = input('Answer: ')
        if q["type"] == "boolean":
            while True:
                user_ans.strip().lower()
                if user_ans in ["true", "false"]:
                    break

                print("This is a True/False question.")
                print("Please enter only True or False.")


get_questions()
