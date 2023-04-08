
g = [[2,3,4],[11,22,33],[34,45,56]]
s = g.pop()
for i in range(2):
    g.append(s+[i])
print(g)

s = [1,2,3,4,5]
s2 = [0 for _ in range(len(s))]

for i,v in enumerate(s):
    s2[i] = v

print(s, s2)
s[2] = 333

print(s, s2)

s2[4] = 123

print(s, s2)

