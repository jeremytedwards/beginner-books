# -*- coding: utf-8 -*-
import sys


def ask_do_you_like_where(where="green eggs and ham?"):
    do_you_like_them = "do you like " + where
    response = input(do_you_like_them)
    return response


def main():
    eggs_are_liked = ask_do_you_like_where()
    num_times_asked = 1
    to_be_asked_dict = {
        "q1": "them here or there?",
        "q2": "them in a house with a mouse?",
        "q3": "them in a box with a fox?",
        "q4": "them on a train?",
        "q5": "them in the dark?",
        "q6": "them on a boat?",
    }
    for each_question in to_be_asked_dict:
        if eggs_are_liked is not True:
            num_times_asked += 1
            question_where = to_be_asked_dict[each_question]
            eggs_are_liked = ask_do_you_like_where(question_where)
        else:
            break
    print("Times asked: ", num_times_asked)


if __name__ == "__main__":
    sys.exit(main())
