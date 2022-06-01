import json
import random
from sys import argv

if len(argv) == 2:
    values = json.loads(open(argv[1]).read())
else:
    values = json.loads(open(input("name of file: ")).read())

while True:
    category = random.choice(list(values.keys()))
    question, answer = random.choice(list(values[category].items()))
    print(category + ": " + question)
    player_answer = input()
    if player_answer == "q":
        quit()
    elif player_answer == answer:
        print("spravne")
    elif player_answer == "":
        print(answer)
    else:
        print("spatne: ", answer)
