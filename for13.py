N = int(input())
S = 0.0
for i in range(1, N + 1):
    if i % 2 == 1:
        S += 1 + i / 10
    else:
        S -= 1 + i / 10
print(S)