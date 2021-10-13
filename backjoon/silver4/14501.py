n = int(input())
ti = []
pi = []
m = []

for i in range(n):
    t, p = input().split()
    ti.append(int(t))
    pi.append(int(p))
    m.append(int(p))
m.append(0)

for i in range(n-1, -1, -1):
    if ti[i] + i > n:
        m[i] = m[i+1]
    else:
        m[i] = max(m[i+1], pi[i]+m[i+ti[i]])

print(m[0])