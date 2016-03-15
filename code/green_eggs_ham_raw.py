# -*- coding: utf-8 -*-
import sys

times_asked = 0

def ask_if_you_like_green_eggs_and_ham(where="green eggs and ham?"):
    my_question = "do you like " + where
    response = input(my_question)
    return response


def main():
    eggs_are_liked = ask_if_you_like_green_eggs_and_ham()
    times_asked = 1
    questions = {
        "q1": "them here or there?",
        "q2": "them in a house with a mouse?",
        "q3": "them in a box with a fox?",
        "q4": "them on a train?",
        "q5": "them in the dark?",
        "q6": "them on a boat?",
    }
    for i in questions:
        if eggs_are_liked is not True:
            times_asked += 1
            my_question_is = questions[i]
            eggs_are_liked = ask_if_you_like_green_eggs_and_ham(my_question_is)
        else:
            break
    print("Times asked: ", times_asked)


if __name__ == "__main__":
    sys.exit(main())
