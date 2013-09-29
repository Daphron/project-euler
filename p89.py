
numbers = { "I" : 1, "V" : 5 , "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

def roman_to_normal(roman):
    normal = 0
    max_digit = "I"
    for d in roman[::-1]:
        if numbers[d] >= numbers[max_digit]:
            normal += numbers[d]
            max_digit = d
        else:
            normal -= numbers[d]

    return normal

def min_rep(num):
    digits = 0
    values = [1000, 500, 100, 50, 10, 5, 1]
    for v in values:
        if num > 0:
            digits += num // v
            num -= num // v

f_name = "roman.txt"
fin = open(f_name)

num_saved = 0
for line in fin:
    num_saved += len(line) - min_rep(roman_to_normal(line))

print(num_saved)
        

