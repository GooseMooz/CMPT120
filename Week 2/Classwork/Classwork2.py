ans = True
p = [True, False]
q = [True, False]
r = [True, False]
for i in range(2):
    for k in range(2):
        for j in range(2):
            ans = p[i] and (q[k] or r[j])
            print(ans)

