#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    uniq = []
    for i in my_list:
        if i in uniq:
            continue
        else:
            uniq.append(i)

    for element in uniq:
            result += element
    return (result)
