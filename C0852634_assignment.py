# Part1 Write a function called ceaser_cypher that takes a string and an integer as parameters, and returns a new string that contains the letters from the original string rotated by the given amount.

def ceaser_cypher(string, shift):
    new_string = ""
    for i in string:
        if i.isalpha():
            if i.isupper():
                new_string += chr((ord(i) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_string += chr((ord(i) - ord('a') + shift) % 26 + ord('a'))
        else:
            new_string += i
    return new_string

encoded=ceaser_cypher("Python", 7)
print(encoded)

# Part-2) Binary Search Algorithm Implementation!
# write a function

"""
Write a function in Python that takes a list of integers, and a specific integer and uses binary search to find if the desired integer is present in the list. 
If the integer is present, the function will return True, otherwise, it will return False
"""
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return True
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return False

searched_item = binary_search([1,2,3,4,5,6,7,8,9,10], 7)
print(searched_item)

# Part-3) Formula Implementation!
"""
Write a function called estimate_pi that uses this formula to compute and return an estimate of π. 
It should use a while loop to compute terms of the summation until the last term is smaller than 
1e-15, which is Python notation for 10^(-15) .
"""
import math


def estimate_pi():
    k = 0.0
    last_term = 1.0
    sigma = 0
    while last_term > 1e-15:
        last_term = ((math.factorial(4.0 * k)) * (1103.0 + 26390.0 * (k))) \
        / ((math.factorial(k) ** 4.0) * (396.0 ** (4.0 * k)))
        k += 1.0
        sigma += last_term
    result = ((2 * math.sqrt(2)) / 9801) * sigma
    return 1 / result

print(estimate_pi())
print(math.pi)

