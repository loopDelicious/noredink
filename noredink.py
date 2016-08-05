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

        # create nested dictionaries

        # question_dict = {
        #                   strand_name = {
        #                                   standard_name: [question_ids]
        #                                   },
        #                   },

        # question_dict = {
        #                   Nouns = {
        #                               Common:     [1,2],
        #                               Abstract:   [3],
        #                               Proper:     [4,5,6]
        #                              },
        #                   Verbs = {
        #                               Action:     [7,8],
        #                               Transitive: [9,10,11],
        #                               Reflexive:  [12]
        #                            }
        #                   }

        question_dict = {}

        for line in questions:

            strand_name = question[1]
            standard_name = question[3]
            question_id = question[4]


            if strand_name not in question_dict:
                question_dict =

            if strand_name in question_dict:


                if standard_name in question_dict[strand_name]:
                    question_dict[strand_name][standard_name].append(question_id)
                else:
                    question_dict[strand_name][standard_name] = [question_id]


            else:
                question_dict[strand_name][standard_name] = [question_id]

    results = []

    while len(results) < num:

        # loop over dictionary to pull from strand and standards equally
        for strand_name in question_dict:
            for standard_name in question_dict[strand_name]:
                for question in question_dict[strand_name][standard_name]:
                    results.append(question_id)

    return results


if __name __ = "__main__":

    number_questions = prompt_user()
    generate_questions(number_questions)


# The expected output is to display a list of question_ids.
# Use each strand as close as possible to an equal number of times. (e.g. There are two strands, so if the user asks for a 3 question quiz, it's okay to choose one strand twice and the other once.)
# Use each standard as close as possible to an equal number of times.
# Without the usage file, prefer questions that have not yet been assigned.
# Duplicating questions in the quiz is OKAY, if the quiz requires more questions than are available with even distribution!