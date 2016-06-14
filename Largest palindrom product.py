"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

#str(n) == str(n)[::-1]

def largest_palindrome():
    a = 999
    palindrome = []
    while a > 0:
        for i in range(999, 99, -1):
            result = a * i
            if str(result) == str(result)[::-1]:
                palindrome.append(result)
        a -= 1
    print(max(palindrome))
largest_palindrome()