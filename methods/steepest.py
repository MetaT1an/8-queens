from tools.heuristic import h_x


def steepest(case):
    """
    only one queen was moved from the case to get successors
    case: list
        a state of 8-queens problem
    return: bool
        whether the problem is solved using given case
    """
    current_hx, is_solved = h_x(case), False
    columns = len(case)

    while True:
        if current_hx == 0:
            break
        # every iter is to find the best successor
        min_hx = 100
        for column in range(columns):
            for step in range(1, columns):  # step is the distance the queen will move [1, 8)
                successor = case[::]  # copy
                successor[column] = (successor[column] + step) % columns  # move one step

                successor_h_x = h_x(successor)  # calculate the h_x value
                if successor_h_x < min_hx:     # compare the h_x value of each successor
                    next_case = successor
                    min_hx = successor_h_x
        if min_hx < current_hx:
            current_hx = min_hx
            case = next_case
        else:
            break

    is_solved = (current_hx == 0)

    return is_solved    # whether the problem is solved
