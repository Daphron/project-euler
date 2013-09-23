#TODO: make under 1 min.
#SOLVED
import math


MAX_P = 1000

best_p = 120
best_num_sides = 3
for p in range(2, MAX_P+1):
    num_sides = 0
    if p % 30 == 0:
        print(p)
    for a in range(1, MAX_P/2 + 2):
        for b in range(1, MAX_P/2 + 2):
            c = p - a - b
            if a > b and b > c and c**2 + b**2 == a**2 and a + b + c == p and c > 0:
                # print("sides {} {} {}".format(a,b,c))
                # print("P={}".format(p))
                num_sides += 1

    if num_sides > best_num_sides:
        # print("Change to p={}".format(p))
        # import pdb; pdb.set_trace()
        best_num_sides = num_sides
        best_p = p

print("Done")
print(best_p)




