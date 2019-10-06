import random
from methods.steepest import steepest


def random_restart(case):
    """
    we define the max number of attempts 5000
    case: list
        a state of 8-queens problem
    return: bool
        whether the problem is solved using given case
    """
    max_attempts, is_solved = 20, False
    columns = len(case)
    new_case = case[::]

    while max_attempts > 0:
        result = steepest(new_case)
        if not result:  # not succeed to solve
            for column in range(columns):
                new_case[column] = random.randint(0, columns-1)  # random start
            max_attempts -= 1
        else:
            is_solved = True
            break

    return is_solved
