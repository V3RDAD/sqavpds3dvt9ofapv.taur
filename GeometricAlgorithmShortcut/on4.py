import random
import decimal
while True:
   x = decimal.Decimal(-random.randrange(1,10))*decimal.Decimal(-random.randrange(1,10))
   y = x / x
   z = y / x
   w = x / y / z
   print(w)
