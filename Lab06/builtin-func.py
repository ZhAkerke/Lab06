# Exercise 1
def mult_num(n):
    x = 1
    for i in n:
        x *= i
    return x

n = [2, 3, 4, 5]
x = mult_num(n)
print(x)

# Exercise 2
def string_test(s):
    d = {"upper": 0, "lower": 0}
    
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    print("Upper case: ", d["upper"])
    print("Lower case: ", d["lower"])

string_test("Hello, World!")

# Exercise 3
def palin(string):
    return string == ''.join(reversed(string))

string = "hahahah"
if palin(string):
    print("It is a palindrome.")
else:
    print("Sorry, try another one")

# Exercise 4
from time import sleep
import math

def sqrt(n, ms):
    sleep(ms / 1000)
    x = math.sqrt(n)
    return x

n = 25100
ms = 2123
x = sqrt(n, ms)
print(f"Square root of {n} after {ms} milliseconds is {x}")

# Exercise 5
def true_elem(mytuple):
    return all(mytuple)

mytuple = (True, True, True)
if true_elem(mytuple):
    print("True")
else:
    print("Try again.")