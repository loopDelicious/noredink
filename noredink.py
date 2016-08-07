""" prompt user for number of questions for a quiz, and return a list of question_ids per preferred rules """

# import random

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
        questions = file.read().split('\n')
        question_list = []
        for question in questions:
            line = question.split(',')
            question_list.append(line)

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

    # construct the nested dicts
    question_dict = {}

    for line in question_list[1:]:

        strand_name = line[1]
        standard_name = line[3]
        question_id = line[4]

        if strand_name in question_dict:
            if standard_name in question_dict[strand_name]:
                question_dict[strand_name][standard_name].append(question_id)
            else:
                question_dict[strand_name][standard_name] = [question_id]
        else:
            question_dict[strand_name] = dict([(standard_name,[question_id])])

    # loop through nested dictionaries to pull from strands and standards equally
    results = []

    # prefer questions that have not yet been answered
    # not_used = set()    # set for unique values and constant lookup time
    # for line in usage:
    #     if line[3] is None:
    #         not_used.add(line[1])
    # if num >= 1:
    #     results.append(random.choice(not_used))
    #   still need to account for the strand / standard this question draws from

    for strand_name in question_dict:
        for standard_name in question_dict[strand_name]:
            for question in question_dict[strand_name][standard_name]:
                results.append(question)
                if len(results) >= num:
                    return results


if __name__ == '__main__':

    number_questions = prompt_user()
    print generate_questions(number_questions)


# The expected output is to display a list of question_ids.
# Use each strand as close as possible to an equal number of times. (e.g. There are two strands, so if the user asks for a 3 question quiz, it's okay to choose one strand twice and the other once.)
# Use each standard as close as possible to an equal number of times.
# Without the usage file, prefer questions that have not yet been assigned.
# Duplicating questions in the quiz is OKAY, if the quiz requires more questions than are available with even distribution!