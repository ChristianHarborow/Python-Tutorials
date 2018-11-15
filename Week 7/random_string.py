import random


def random_string():
    ANSWERS = ['Yes', 'No', 'Maybe', 'Ni!']
    return random.choice(ANSWERS)

print(random_string())
