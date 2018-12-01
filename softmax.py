import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):

    expL = np.exp(L)
    print(expL)
    sumExpL = sum(expL)
    result = []

    for i in expL:
         result.append(i/sumExpL)

    return result


