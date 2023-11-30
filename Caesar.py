import sys
import math
b = []
c = int(sys.argv[2])
for char in sys.argv[1]:
    b.append(ord(char))
understand = lambda a: print(chr(a-c), end="")
(list(map(understand, b)))
print("")
