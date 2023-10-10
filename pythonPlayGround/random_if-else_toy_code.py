# If n is odd, print weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even adn greater than 20, print Not Weird

import math
import os
import random
import re
import sys

# The randint() function generates a random number between 1 and 100.
# It than assigns that number to n each time the code is ran.

n = random.randint(1, 100)
print(n)
if (n % 2 != 0):
    print('Weird')
elif (n % 2 == 0) and (2 <= n < 5):
    print('Not Weird')
elif (n % 2 == 0) and (6 <= n <= 20):
    print('Weird')
elif (n % 2 == 0) and (n > 20):
    print('Not Weird')
