import random

"""
[0, 1, 2, 3, 4, 6, 8, 5]
we define an instance of 8-queens problem as a 8-length tuple
each element in the tuple represents the position of each queen in different columns
"""
cases_number = 400


def gen_cases():
    """
    f: file
        to store all randomly generated cases/instances of 8-queens problem
    cases: str
        put each case together into a string, separated by \n
    """
    f = open("../cases.txt", "w")
    cases = ""

    for i in range(cases_number):
        for column in range(7):
            cases += str(random.randint(0, 7)) + " "
        cases += str(random.randint(0, 7)) + "\n"

    f.write(cases)
    f.close()


if __name__ == '__main__':
    gen_cases()     # to generate all the cases
