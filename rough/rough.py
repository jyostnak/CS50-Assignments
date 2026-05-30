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
    data = response.json
    questions = data['results']
    print(questions[0]["question"])
get_questions()
