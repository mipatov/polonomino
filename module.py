import numpy as np

# создание фигур


def rotate_rect(r):
    return np.ones((r[1], r[0]))


def rect(r):
    return np.ones(r)


def L_poly(l):
    l_h, l_w = l
    return np.pad(np.zeros((l_h-1, l_w-1)), [(0, 1), (1, 0)], constant_values=1)


def L_poly_rotate90(l):
    l_h, l_w = l
    return np.pad(np.zeros((l_w-1, l_h-1)), [(1, 0), (1, 0)], constant_values=1)


def L_poly_rotate180(l):
    l_h, l_w = l
    return np.pad(np.zeros((l_h-1, l_w-1)), [(1, 0), (0, 1)], constant_values=1)


def L_poly_rotate270(l):
    l_h, l_w = l
    return np.pad(np.zeros((l_w-1, l_h-1)), [(0, 1), (0, 1)], constant_values=1)

# решающий алгоритм


def solve(base_row, poly_matr_list, k, solutions=[]):

    poly = poly_matr_list[k]
    for row in poly:
        sum_row = base_row + row
        if sum_row.max() <= 1:
            solutions.append(row)
            if len(poly_matr_list) == k+1:
                return True

            flag = solve(sum_row, poly_matr_list, k+1, solutions)
            if flag:
                return True
            solutions.pop()
    return False

# вывод решения


def prtin_solution(solutions, T):
    out = np.zeros(T[0]*T[1])
    for i, row in enumerate(solutions):
        out += row * (i+1)
    return out.reshape((T[1], T[0]))
