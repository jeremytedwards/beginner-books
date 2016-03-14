# -*- coding: utf-8 -*-
import random


def ask_if_you_like(where="green eggs and ham?"):
    question = "do you like " + where
    response = input(question)
    return response


def main():
    eggs_are_liked = False
    times_asked = 0
    to_be_asked = {
        "q1": "them here or there?",
        "q2": "them in a house with a mouse?",
        "q3": "them in a box with a fox?",
        "q4": "them on a train",
        "q5": "them in the dark?",
        "q6": "them on a boat?",
    }
    while eggs_are_liked is not True:
        times_asked += 1
        asking = random.choice(to_be_asked.values())
        eggs_are_liked = ask_if_you_like(asking)
    return


if __name__ == "__main__":
    sys.exit(main())
