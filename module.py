import numpy as np

# создание фигур
def rotate_rect(r):
    return np.ones((r[1],r[0]))

def rect(r):
    return np.ones(r)

def L_poli(l):
    l_h,l_w = l
    return np.pad(np.zeros((l_h-1,l_w-1)),[(0,1),(1,0)],constant_values =1)

def L_poli_rotate90(l):
    l_h,l_w = l
    return np.pad(np.zeros((l_w-1,l_h-1)),[(1,0),(1,0)],constant_values =1)

def L_poli_rotate180(l):
    l_h,l_w = l
    return np.pad(np.zeros((l_h-1,l_w-1)),[(1,0),(0,1)],constant_values =1)

def L_poli_rotate270(l):
    l_h,l_w = l
    return np.pad(np.zeros((l_w-1,l_h-1)),[(0,1),(0,1)],constant_values =1)

# решающий алгоритм
def solve(base_row,matr,k,solutions=[]):
    polino = matr[k]
    for row in polino:
        sum_row = base_row+ row
        if sum_row.max()<2:
            solutions.append(row)
            if len(matr) == k+1:
                return solutions
            
            flag = solve(sum_row,matr,k+1)
            if flag: 
                return solutions
            solutions.pop()
    return False

# вывод решения
def prtin_solution(solutions,T):
    out = np.zeros(T[0]*T[1])
    for i,row in enumerate(solutions):
        out+=row *(i+1)
    return out.reshape((T[1],T[0]))