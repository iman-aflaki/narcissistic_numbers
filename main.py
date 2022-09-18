def is_narcissistic_num(n):
    import math
    return sum([int(i)**len(str(n)) for i in str(n)])

for i in range(1,1000):
    if i == is_narcissistic_num(i):
        print(i,end=', ')
