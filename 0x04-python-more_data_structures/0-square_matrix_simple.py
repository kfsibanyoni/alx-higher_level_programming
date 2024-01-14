#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    
    new_mat = []
    for row in matrix:
        trans = []
        for x in row:
            x = x * x
            trans.append(x)
        new_mat.append(trans)
    return (new_mat)
