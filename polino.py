import numpy as np
from module import *

T = (3,5)
R = [((2,2),1)]
# R = [((2,2),1),((3,1),1)]
L = [((3,2),1),((2,2),2)]

rect_list = []

for shape,n in R:
    rs = rect(shape)
    rrs = rotate_rect(shape)
    
    rows = [[rs,rrs]] * n
    rect_list.extend(rows)

L_poli_list = []
for shape,n in L:
    ls = L_poli(shape)
    ls90 = L_poli_rotate90(shape)
    ls180 = L_poli_rotate180(shape)
    ls270 = L_poli_rotate270(shape)
    
    rows = [[ls,ls90,ls180,ls270]] * n
    L_poli_list.extend(rows)

poli_list = [*rect_list,*L_poli_list]


t_w,t_h = T 

p_matr_list = []
for poli_id,support_poli in enumerate(poli_list):
    mat = np.zeros([0,t_h*t_w])
    for p_id,p in enumerate(support_poli): 
        p_h,p_w = p.shape

        for i in range(t_h-p_h+1):
            for j in range(t_w-p_w+1):
                mat = np.pad(mat,[(0,1),(0,0)])
                table = np.pad(p, [(i, t_h-p_h-i), (j, t_w-p_w-j)]) # фигура на столе
                nonzero_idx = table.reshape(-1).nonzero()
                mat[-1][nonzero_idx]=1

    p_matr_list.append(mat)

base = np.zeros([1,t_h*t_w])
solution = solve(base,p_matr_list,0)

if solution:
    print("Найдено решение: ")
    print(prtin_solution(solution,T))
else:
    print("Решение не найдено!")