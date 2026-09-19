A = float(input())
N = int(input())
P = 1.0
S = 1.0
for i in range(1, N + 1):
 P *= A
 S += P
print(S)