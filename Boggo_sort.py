a = """ Just Boggo Sort 'algorithm'.
    Created by chief141.github.io
    Repo link : https://github.com/chief141/boggo-sort-python
    Do whatever you want to do with this, I dont give a F, just remember
    I dont take any reponsibility(s) of this piece of code.
"""

from random import randrange
from time import perf_counter

def check_sorted(lis):
    for i, j in enumerate(lis):
        if i < len(lis) - 1:
            if lis[i] > lis[i + 1]:
                return False
    else:
        return True

def randomize_list(lis):
    i = 0
    while i < len(lis):
        rand_a = randrange(len(lis))
        rand_b = randrange(len(lis))
        if rand_b != rand_a:
            lis[rand_a], lis[rand_b] = lis[rand_b], lis[rand_a]
            i += 1
    return lis


def main():
    l = []
    n = int(input("Enter number of items in list : ")) #Your LIst
    for k in range(n):
        try: l.append(int(input("Enter a number : ")))
        except: pass

    if check_sorted(l):
        print("It's already sorted!!")
        return l

    else:
        started = perf_counter()
        number = 1
        while True:
            new_l = randomize_list(l)
            print(f"{number}th : {new_l}")
            number += 1
            if check_sorted(new_l):
                print(f"Time Taken : {perf_counter() - started}sec")
                print('Sorted : ')
                return new_l
                break;


if __name__ == '__main__':
    print(main())