"""
    Arrays: Left Rotation
    Challenge https://www.hackerrank.com/challenges/ctci-array-left-rotation
    A left rotation operation on an array of size n shifts each of the array's 
    elements 1 unit to the left. For example, if 2 left rotations are 
    performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].
    Given an array of n integers and a number, d, perform d left rotations on 
    the array. Then print the updated array as a single line of space-separated 
    integers

    @fnscoder
"""

n, d = [int(i) for i in input().split()]
v = input().split()
print(' '.join(v[d:] + v[:d]))