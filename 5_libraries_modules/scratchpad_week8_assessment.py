import random
import datetime

print(dir(random))

t = datetime.date.today()
n = datetime.date(t.year + 1, 1, 1)

d = n - t

print(type(d), d)