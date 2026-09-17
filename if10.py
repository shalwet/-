A = float(input())
B = float(input())
if A != B:
    S = A + B
    A = S
    B = S
else:
    A = 0
    B = 0
print(A, B)