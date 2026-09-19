a = float(input())
b = float(input())
c = float(input())
AC = c - a
BC = c - b
if AC < 0:
 AC = -AC
if BC < 0:
 BC = -BC
print(AC * BC)