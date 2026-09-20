X = int(input())
N = int(input())
power = X
S = 0.0
for i in range(1, N + 1):
 if i > 1: power *= X
 term = power / i
 if i % 2 == 1: S += term
 else: S -= term
print(S)