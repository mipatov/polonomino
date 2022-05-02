import numpy as np
from module import *

T = (3, 5)
R = [((2, 2), 1)]
# R = [((2,2),1),((3,1),1)]
L = [((3, 2), 1), ((2, 2), 2)]

rect_list = []

for shape, n in R:
    rs = rect(shape)
    rrs = rotate_rect(shape)

    rows = [[rs, rrs]] * n
    rect_list.extend(rows)

L_poly_list = []
for shape, n in L:
    ls = L_poly(shape)
    ls90 = L_poly_rotate90(shape)
    ls180 = L_poly_rotate180(shape)
    ls270 = L_poly_rotate270(shape)

    rows = [[ls, ls90, ls180, ls270]] * n
    L_poly_list.extend(rows)

poly_list = [*rect_list, *L_poly_list]


t_w, t_h = T

poly_matr_list = []
for poly_id, support_poly in enumerate(poly_list):
    matr = np.zeros([0, t_h*t_w])
    for p_id, p in enumerate(support_poly):
        p_h, p_w = p.shape

        for i in range(t_h-p_h+1):
            for j in range(t_w-p_w+1):
                new_row = np.pad(
                    p, [(i, t_h-p_h-i), (j, t_w-p_w-j)]).reshape(-1)
                matr = np.vstack([matr, new_row])

    poly_matr_list.append(matr)

solutions = []
base = np.zeros([1, t_h*t_w])
result = solve(base, poly_matr_list, 0,solutions)

if result:
    print("Найдено решение: ")
    print(prtin_solution(solutions, T))
else:
    print("Решение не найдено!")
