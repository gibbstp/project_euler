"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

#Using sieve of Eratosthenes

def primes():
    i, ps, sieve = 1, [], [True] * (n+1)
    while i < 10001:
