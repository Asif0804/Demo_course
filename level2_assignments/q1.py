a = list(map(int, input().split()))
b = list(map(int, input().split()))
c =[]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
          c.append(a[i])

d = list(set(c))
print("Common Elements: ", d)