import random, math
from tools.heuristic import h_x


def cool_down(temperature):
    """
    temperature gets lower along with time, finally stay static
    """
    new_temperature = temperature * 0.985
    return new_temperature


def simulated_annealing(case):
    temperature, columns = 150, len(case)
    current_hx, is_solved = h_x(case), False

    while temperature > 0.05:
        if current_hx == 0:
            break
        # randomly generate a successor
        column = random.randint(0, columns - 1)
        step = random.randint(1, columns - 1)
        successor = case[::]
        successor[column] = (successor[column] + step) % columns

        successor_h_x = h_x(successor)
        delt_e = successor_h_x - current_hx
        if delt_e < 0:  # successor is better
            case = successor
            current_hx = successor_h_x
        else:
            p = math.exp((-1)*delt_e/temperature)
            if random.random() <= p:
                case = successor
                current_hx = successor_h_x

        temperature = cool_down(temperature)

    is_solved = (current_hx == 0)
    return is_solved
