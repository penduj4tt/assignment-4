class Vehicle:
    def __del__(self):
        print("Vehicle object destroyed")
        print(10/0)
v = Vehicle()
del v

# output
# Vehicle object destroyed
# Exception ignored in: <function Vehicle.__del__ at 0x000001DC0523AC10>
# Traceback (most recent call last):
#   File "C:/Users/SUKHMAN DEEP SINGH/Documents/training python/assign4/9.py", line 4, in __del__
#     print(10/0)
# ZeroDivisionError: division by zero

