'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

def is_prime(n):
    """"pre-condition: n is a nonnegative integer
    post-condition: return True if n is prime and False otherwise."""
    if n < 2:
         return False;
    if n % 2 == 0:
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def largest_prime(number):
    prime = []
    n = 3
    while n*n < number:
        if is_prime(n) and number % n == 0:
            prime.append(n)
        n += 1
    print(max(prime))

largest_prime(600851475143)