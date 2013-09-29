#TODO: make run in < 1 min
import math

def is_abundant(num):
    sumnum = 1
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            # print('inside')
            # print(i)
            sumnum += i
            if num // i != i:
                sumnum += num // i

    if sumnum > num:
        # print('abundant')
        return True

    return False

def can_be_written(num, abundants):
    for i in abundants:
        if num-i in abundants:
            return True

    return False

abundants = []
sumnum = 0
for i in range(1,28124):
    if i % 1000 == 0:
        print(i)

    if is_abundant(i):
        abundants.append(i)
        # print(abundants)
    if not can_be_written(i, abundants):
        sumnum += i

print(sumnum)


    
