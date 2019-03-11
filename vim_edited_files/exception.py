""" this is a docstring now i thing
"""
import math
anumber = int(input("Pleas enter an integer "))
try:
    print(math.sqrt(anumber))
except:
    print("Bad Value for Square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(anumber)))
try:
    pass
except:
    pass

