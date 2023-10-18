

# 가장 약한 포탑
# 가장 강한 포탑

# 포탑의 정보
# 1. 공격력
# 2. 공격한 시점
# 3. 행
# 4. 열

class PoTop:
    def __init__(self, pw, t, x, y):
        self.pw = pw
        self.t = t
        self.x = x
        self.y = y
    
    # 약한 포탑 순서
    def __lt__(self, other):
        if self.pw != other.pw:
            return self.pw < other.pw
        if self.t != other.t:
            return self.t < other.t
        if self.x+self.y != other.x+other.y:
            return self.x+self.y > other.x+other.y
        return self.y > other.y




