""" prompt user for number of questions for a quiz, and return a list of question_ids per preferred rules """

import sys

def prompt_user():
    """ prompt user for number of questions """

    try:
        number_questions = int(raw_input("How many questions would you like in your quiz? (enter number) >> "))
    except ValueError:
        print "Sorry, please try again."

    return number_questions

def generate_questions(num):

    with open("nri-backend-takehome/usage.csv") as file:
        usage = file.read().split(',')

    with open("nri-backend-takehome/questions.csv") as file:
        questions = file.read().split(',')

    question_ids = []

    while len(questions_ids) < num:
        

    return question_ids

if __name __ = "__main__":

    number_questions = prompt_user()
    generate_questions(number_questions)


# The expected output is to display a list of question_ids.
# Use each strand as close as possible to an equal number of times. (e.g. There are two strands, so if the user asks for a 3 question quiz, it's okay to choose one strand twice and the other once.)
# Use each standard as close as possible to an equal number of times.
# Without the usage file, prefer questions that have not yet been assigned.
# Duplicating questions in the quiz is OKAY, if the quiz requires more questions than are available with even distribution!