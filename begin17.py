a = float(input())
b = float(input())
c = float(input())
AC = c - a
if AC < 0:
 AC = -AC
BC = c - b
if BC < 0:
 BC = -BC
print(AC, BC, AC + BC)