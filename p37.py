import math

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False

    return True

def is_truncatable(n):
    s = str(n)
    while len(s) > 0:
        if not is_prime(int(s)):
            return False
        s = s[:-1]

    s = str(n)
    while len(s) > 0:
        if not is_prime(int(s)):
            return False
        s = s[1:]

    return True

num_left = 11
sum_of_primes = 0
i = 10
while num_left > 0:
    if is_truncatable(i):
        sum_of_primes += i
        num_left -= 1

    i += 1

print(i)
print(sum_of_primes)


