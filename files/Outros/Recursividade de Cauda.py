def fatorial(N, PARCIAL = 1):
    if (N <= 1): return PARCIAL
    else: return fatorial(N - 1, PARCIAL * N)

n = int(input())
print(fatorial(n))
input()
