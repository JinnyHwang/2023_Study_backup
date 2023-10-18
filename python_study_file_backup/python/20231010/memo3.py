
print(2^4^5)
print(4^5^2)
print(5^1^3)


def cal_XOR(l):
    re = 0
    for ll in l:
        re = re^ll
    return re

print(cal_XOR([5,1,3]))