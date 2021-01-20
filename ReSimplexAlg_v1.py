# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 21:57:59 2020
Implementing the Revised Simplex Algorithm 
@author: Mert Parcaoglu
"""
import numpy as np


# Problem transformation to appropriate version
def setup_algorithm(type_prob, c, e, A, b):
    """

    :param type_prob: Defines the problem type. 1, if the problem is a maximization problem;
                                                0, if the problem is a minimization problem.
    :param c: Coefficients of Objective function
    :param e: Equation type.    2, '>=' type equations;
                                1, '<=' type equations;
                                0, '==' type equations.
    :param A: The coefficients matrix of variables from constraints.
    :param b: RHS values
    :return:  Objective Func. Value, Basis, NB, feasibility status
    """

    if type_prob == 0:
        c *= -1

    seq_of_vars = {'x_{}'.format(i+1): i for i in range(len(c))}

    # If the problem type is minimization,
    # the problem is converted to maximization by multiplying c by -1.

    for i, e_ in enumerate(e):
        if e_ == 2:
            c = np.append(c, [0, np.float64(-1)])
            A = np.append(A, np.array([[-1 if i == j else 0 for j in range(e.shape[0])]]).T,
                          axis=1)
            seq_of_vars['e_{}'.format(len([0 for i in seq_of_vars.keys() if 'e' in i])+1)] = len(seq_of_vars.keys())
            A = np.append(A, np.array([[1 if i == j else 0 for j in range(e.shape[0])]]).T,
                          axis=1)
            seq_of_vars['a_{}'.format(len([0 for i in seq_of_vars.keys() if 'a' in i])+1)] = len(seq_of_vars.keys())

        elif e_ == 1:
            c = np.append(c, 0)
            A = np.append(A, np.array([[1 if i == j else 0 for j in range(e.shape[0])]]).T,
                          axis=1)
            seq_of_vars['s_{}'.format(len([0 for i in seq_of_vars.keys() if 's' in i])+1)] = len(seq_of_vars.keys())

        else:
            chck = True
            for k in range(A.shape[1]):
                if [0 if j != i else 1 for j in range(A.shape[0])] == A[:, k].tolist():
                    chck = False
            if chck:
                c = np.append(c, np.float64(-1))
                A = np.append(A, np.array([[1 if i == j else 0 for j in range(e.shape[0])]]).T,
                              axis=1)
                seq_of_vars['a_{}'.format(len([0 for i in seq_of_vars.keys() if 'a' in i])+1)] = len(seq_of_vars.keys())

    # Equations are checked for adding slack or artificial variables.
    # Then, artificial variables are labeled by using 'artificials'.

    has_art = False

    # Two - Phase method has been used in this project.
    if len([0 for i in seq_of_vars.keys() if 'a' in i]) > 0:
        art_seq = [v for k, v in seq_of_vars.items() if 'a' in k]
        c_t = np.array([np.float64(-1) if i in art_seq else np.float64(0) for i in range(len(c))])
        has_art = True
        for i in np.argwhere(c_t == -1.0):
            c_t += A[np.where(A[:, i[0]] == 1.0), :].reshape(A.shape[1], )

        c_init = c
        c = c_t
        phase = 1
    else:
        phase = 2

    # TODO: aciklamalara devam et Two-Phase aciklanacak

    Basis, Basis_name, NB, NB_name, c_b, c_n, B, N, x_b, z = initial(A, c, b, seq_of_vars)

    B = B.astype(np.float64)

    while True:
        con = True
        w = step_1(c_b, B)
        print('NB : ', NB)
        entering, con = step_2(w, N, c_n, NB_name)
        if not con:
            break
        eta, leaving, unb = step_3(B, N, entering, x_b, Basis_name)
        if unb:
            break
        B = step_4(B, eta, leaving)
        Basis[leaving], NB[entering] = NB[entering], Basis[leaving]
        Basis_name[leaving], NB_name[entering] = NB_name[entering], Basis_name[leaving]
        x_b = B.dot(b)
        c_b = c[Basis]
        c_n = c[NB]
        z = c_b.dot(B).dot(b)
        N = A[:, NB]

        if phase == 1:
            if len([0 for i in NB_name if 'a' in i]) == len([0 for i in seq_of_vars.keys() if 'a' in i]):
                print('phase-2 start')
                """
                for k, v in seq_of_vars.items():
                    if 'a' in k:
                        NB_name.remove(k)

                NB = [seq_of_vars[k] for k in NB_name]
                print('NB: ',NB)
                N = B.dot(A[:,NB])"""
                c_n = c_init[NB]
                c_b = c_init[Basis]
                c = c_init
                phase = 2


        print('z: ', z)
        print('basis: ', Basis_name)
        print('x_b: ', x_b)
    if not unb:
        feasibility = True
        for i in x_b:
            if i < 0:
                feasibility = False
                break
        if feasibility and has_art:
            for var_ord, var_ in enumerate(Basis_name):
                if 'a' in var_:
                    if x_b[var_ord] > 0:
                        feasibility = False
                        break
                    else:
                        z = c_init[Basis].dot(x_b)
        print('Results => ', 'z: ', z)
        print('Results => ', 'basis: ', Basis_name)
        print('Results => ', 'x_b: ', x_b)
        print('Results => ', 'c_b: ', c_b)
        return Basis_name, NB_name, x_b, (z * (-1.0) if type_prob == 0 else z), feasibility, False
    else:
        return -1, -1, -1, -1, True, True


# Initialization

def initial(A, c, b, name):
    Basis = [i for i in range(A.shape[1])
             if [0 if j != 0 else 1 for j in range(A.shape[0])] == sorted(A[:, i],
                                                                          reverse=True)]

    Basis_name = [list(name.keys())[list(name.values()).index(i)] for i in Basis]

    NB = [i for i in range(A.shape[1]) if i not in Basis]

    NB_name = [list(name.keys())[list(name.values()).index(i)] for i in range(A.shape[1]) if i not in Basis]

    c_b = c[Basis]
    c_n = c[NB]
    B = A[:, Basis]
    N = A[:, NB]
    x_b = B.dot(b)
    z = c_b.dot(x_b)
    print('Basis_name: ', Basis_name,
          '\nBasis: ', Basis,
          '\nNB: ', NB,
          '\nNB_name: ', NB_name,
          '\nc_b: ', c_b,
          '\nc_n', c_n,
          '\nB', B,
          '\nN', N,
          '\nx_b', x_b,
          '\nz', z)
    return Basis, Basis_name, NB, NB_name, c_b, c_n, B, N, x_b, z


# Basis, Basis_name, NB, NB_name, c_b, c_n, B, N, x_b, z = initial(A,c)

def step_1(c_b, B):
    # B is assigned to place of B inverse.
    w = c_b.dot(B)
    return w


def step_2(w, N, c_n, NB_name):
    control = w.dot(N) - c_n
    print('control : ', control,
          '\n w : ', w,
          '\n N : ', N,
          '\n c_n : ', c_n,
          '\n contolr_sum : ', sum(control < 0))
    if np.min(w.dot(N) - c_n) >= 0:
        # Optimal solution is found.
        return -1, False
    entering = np.argmin(w.dot(N) - c_n)
    print('entering variable: ' + NB_name[entering])
    return entering, True


def step_3(B, N, entering, x_b, Basis_name):
    y = B.dot(N[:, [entering]])
    if sum(y <= 0) == len(y):
        print('unbounded')
        return -1,-1, True
    print('y : ', y)
    print('X_b : ', x_b)
    leaving = np.argmin(x_b / np.where(y <= 0., 1e-10, y))
    eta = np.array([1 if i == leaving else -item[0] for i, item in enumerate(y)]) / y[leaving]
    print('leaving variable: ' + Basis_name[leaving])
    return eta, leaving, False


def step_4(B, eta, leaving):
    E = np.delete(np.insert(np.identity(len(B)), leaving, eta, axis=1), leaving + 1, axis=1)
    B = E.dot(B)
    print('E : ', E)
    print('B_new : ',B)
    return B
