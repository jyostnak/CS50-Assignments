import sys
from datetime import datetime
import time
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
        print(q["question"])

        if q["type"] == 'multiple':
            options = []
            options.extend(q['incorrect_answers'])
            options.extend(q['correct_answer'])
            for op in options:
                print(f'{options.index(op)}. {op}')
        user_ans = input('Answer: ')

