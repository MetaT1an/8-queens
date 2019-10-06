import random
from tools.heuristic import h_x


def first_choice(case):
    """
    randomly generate one successor
    take it if it is better else ignore it
    """
    current_hx, iter_times = h_x(case), 3
    is_solved, columns = False, len(case)

    while iter_times > 0:   # try 3 iterations, totally 600 times to randomly find a better successor
        if current_hx == 0:
            break

        choose_times = 200
        # randomly generate one successor, we use random column and random step
        # to define a random successor
        while choose_times > 0:
            column = random.randint(0, columns-1)
            step = random.randint(1, columns-1)
            successor = case[::]
            successor[column] = (successor[column] + step) % columns

            successor_h_x = h_x(successor)
            if successor_h_x < current_hx:      # find a better successor
                case = successor
                current_hx = successor_h_x
                iter_times = 3  # restore counter
                break
            choose_times -= 1
        iter_times -= 1

    is_solved = (current_hx == 0)

    return is_solved
