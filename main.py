import json
import random

values = json.loads(open("letopocty.json").read())
while True:
    question, answer = random.choice(list(values[random.choice(["svet", "cr"])].items()))
    print(question)
    player_answer = input()
    if player_answer == answer:
        print("spravne")
    elif player_answer == "":
        print(answer)
    else:
        print("spatne: ", answer)
