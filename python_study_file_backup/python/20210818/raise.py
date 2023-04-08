def rsp(mine, yours):
    allowed = ['가위', '바위', '보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise IndexError
#기존에 있는 Error name 사용해야함

try:
    rsp('잉','부')
except ValueError:
    print('jieun')
except IndexError:
    print('hwang')


school = {'1반':[172, 185, 158, 177, 165, 169],
          '2반':[165, 177, 167, 180, 191]}

try :
    for class_number, students in school.items():
        for student in students:
            if student > 190:
                print(class_number,'에 키가', student,'인 학생이 있습니다')
                raise StopIteration
except StopIteration:
    print('동작 끝')
