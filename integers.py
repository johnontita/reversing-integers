"""
Write a program that takes an integer as input and returns an integer with
reversed digit ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19.

"""
numbers=(input('enter the integer numbers   '))
number_reversed=int(numbers[::-1])
print(number_reversed)
