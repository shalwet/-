x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
a = x2 - x1
if a < 0:
 a = -a
b = y2 - y1
if b < 0:
 b = -b
print(2 * (a + b), a * b)