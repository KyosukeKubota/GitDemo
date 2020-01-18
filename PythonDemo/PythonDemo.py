import datetime as dt

p = dt.date.today()
t = dt.datetime.now()

a = 5 + 8
b  = 8 / 3

print(p)
print(t)
print(a)
print(b)

if a % 3 == 0:
    print("a % 3 == 0")
elif a % 3 == 1:
    print("a % 3 == 1")
else:
    print("a % 2 == 2")

for item in [0,1,2,3,4,5]:
    print(item)

for item in range(0,6):
    print(item)