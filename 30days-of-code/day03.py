"""
    Day 3: Intro to Conditional Statements
    Challenge https://www.hackerrank.com/challenges/30-conditional-statements
    Given an integer, n, perform the following conditional actions:
    If n is odd, print Weird
    If n is even and in the inclusive range of 2 to 5, print Not Weird
    If n is even and in the inclusive range of 6 to 20, print Weird
    If n is even and greater than 20, print Not Weird
    Complete the stub code provided in your editor to print whether or not n is weird.
    @fnscoder
"""

n = int(input().strip())

if n % 2 != 0 or (n > 5 and n < 21):
    print('Weird')
else:
    print('Not Weird')