def h_x(case):
    """
    we regard the collision numbers as h(x) value
    case: tuple
        a state of 8-queens problem
    return: bool
        whether the problem is solved using given case
    """
    value, columns = 0, len(case)

    for col_a in range(columns):
        for col_b in range(col_a+1, columns):
            collision_row = case[col_a] == case[col_b]  # collision in the same row
            collision_cross = (col_b - col_a) == abs(case[col_a] - case[col_b])   # collision in the cross

            if collision_row or collision_cross:
                value += 1
    return value