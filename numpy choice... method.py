
'''
p=[0.1, 0.3, 0.6, 0.0]
3 → 10% chance

5 → 30% chance

7 → 60% chance

9 → 0% (মানে কখনোই বাছাই হবে না)

'''
from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3,3))

print(x)