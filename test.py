graph = [
    {8,5,2},
    {5,2,0},
    {1,7,6,2},
    {0,1},
    {4},
    {0,5},
    {8,9,2},
    {2,5,4},
    {5,4}
]
import itertools
import math
n = 31
def is_prime(n):
    for i in range(2,round(math.sqrt(n))):
        if not n % i:
            return False
    return True
is_palan = lambda x: str(x) == str(x)[::-1]
for i in itertools.count(n):
    if all((is_palan(i), is_prime(i))):
        print(i)
        break