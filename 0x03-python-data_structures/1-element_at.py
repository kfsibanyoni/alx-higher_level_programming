#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx > len:
        print("None")
    else:
        print('{:d}'.format(idx))
