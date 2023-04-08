
#a = "10303"
#b = "32220000"
a = "2555"
b = "1255"
#a = "100"
#b = "2345"
l = list()
#l = ""

for aa in a:
    for bi, bb in enumerate(b):
        #print(aa, bb)
        if aa == bb:
            l.append(aa)
            #l += aa
            b = b[:bi]+b[bi+1:]
            print(aa, bb, bi)
            print(b)
            break
if not l:
    print('?')

print(l)
l.sort(reverse=True)
print(l)
for ll in l:
    print(ll, end="")
#ls = "".join(l)
#print(ls)
#print(b)



