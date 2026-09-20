X = int(input())
N = int(input())
fact = 1.0
power = X
S = X
for i in range(1, N + 1):
 fact *= (2 * i) * (2 * i + 1)
 power *= X * X
 term = power / fact
 if i % 2 == 1: S -= term
 else: S += term
print(S)