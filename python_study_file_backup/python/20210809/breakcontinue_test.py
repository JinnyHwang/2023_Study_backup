numbers = [(1, 2), (10, 0)]

for a, b in numbers:
    if b == 0:
        print("0으로 나눌 수는 없습니다.")
        continue
    # 이 부분이 else문에 들어있지 않도록 수정해야 합니다.
    print("{}을(를) {}로 나누면 {}".format(a, b, a/b))
                                     