import random

def bubble_sort():
    ls = random.sample(range(1, 101), 10)
    for i in range(len(ls)):
        for j in range(0, len(ls)-i-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    print(ls)

bubble_sort()
