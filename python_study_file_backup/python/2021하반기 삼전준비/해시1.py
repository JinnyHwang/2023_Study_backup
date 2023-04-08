
l = ["12","123","1235","567","88"]
#l.sort( key=lambda x : len(x))
l.sort()
print(l)


str1 = "56"
str2 = "8567"
str3 = "5689"
print(str1 in str3[:len(str1)])

def test():
    for a in l:
        if str1 in a:
            print(a)


def solution1(phone_book):
    
    phone_book.sort(key = lambda x : len(x))
    check = {}
    answer = True
    for p in phone_book:
        for c in check:
            print("c : {}, p : {}".format(c, p))
            if c in p[:len(c)]:
                answer = False
                break
        else:
            check[p] = check.get(p, 0)
            print(check[p])
    return answer

l2 = ["12","567","88", "87", "878"]
l3 = ["123", "456", "4568"]
l4 = ["934793", "34", "44", "9347"]
l5 = ["123", "456", "4567", "999"]
l6 = ["11", "22", "33", "44", "123", "345", "1245", "4567", "34566"]
def solution(phone_book):
    
    phone_book.sort()
    answer = True
    
    print(phone_book)
    print(len(phone_book))
    for i, p in enumerate(phone_book):
        if i >= len(phone_book)-1:
            break
        print(i, i+1, p, phone_book[i+1])
        if p in phone_book[i+1]:
            answer = False
            break
        else:
            continue
    return answer

def sol(phone_book):
    
    phone_book.sort()
    print(phone_book)
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            print(p1, p2)
            return False
    return True

def sol2(phone_book):
    
    hash_map = {}
    
    for pn in phone_book:
        hash_map[pn] = 1
    
    for pn in phone_book:
        for h in hash_map:
            if pn in h[:len(pn)]:
                return False
    else:
        return True
    

#print(solution(l6))
print(l6)
print(sol2(l6))


# 제출 code
def solution(phone_book):
    
    phone_book.sort()
    answer = True
    
    for i, p in enumerate(phone_book):
        if i >= len(phone_book)-1:
            break
        if p in phone_book[i+1][:len(p)]:
            answer = False
            break
        else:
            continue
    return answer

def solution(phone_book):
    
    phone_book.sort()
    answer = True
    phone_book_len = len(phone_book)
    
    for i, p in enumerate(phone_book, start=1):
        if i < phone_book_len and p in phone_book[i][:len(p)]:
            answer = False
            break
        else:
            continue
    return answer




