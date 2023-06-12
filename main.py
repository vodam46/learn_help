#!/usr/bin/env python3
import json
import random
from sys import argv
import itertools

if len(argv) == 2:
    values = json.loads(open(argv[1]).read())
else:
    values = json.loads(open(input("name of file: ")).read())

values = list(itertools.chain.from_iterable([[[
            category+": "+question, answer
            ] for question, answer in list(values[category].items())
    ] for category in list(values.keys())]))


while True:
    correct = 0
    wrong = 0
    asked = 0
    for question, answer in random.sample(values, len(values)):
        check_answer = answer.replace(" ", "")
        print(question)
        player_answer = input().replace(" ", "")
        if player_answer == "q":
            print(f"✅ {correct} ❌ {wrong} ❓ {asked}")
            quit()
        elif player_answer == check_answer:
            correct += 1
            print("✅ " + answer)
        elif player_answer == "":
            asked += 1
            print(answer)
        else:
            wrong += 1
            print("❌ ", answer)
    print(f"✅ {correct} ❌ {wrong} ❓ {asked}")
