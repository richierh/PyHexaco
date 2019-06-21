import random

nilai = random.randint(1700, 1900)
acak = random.randint(10000,99999)
print (nilai)
lisennombor =  str(nilai * 4) + str(acak)
n = int(lisennombor)

# n = 3434556782

lastdigit = int(repr(n)[0:4])

print (int(lastdigit/4))


print (lisennombor)