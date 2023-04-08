
students = ['태', '진', '정', '하', '성']

#번호까지 넣어서 딕셔너리형으로

# enumerate로 number 정의
for number, name in enumerate(students):
    print("{}번의 이름은 {}입니다.".format(number+1, name))

# "{}번".format(number+1) : name :콜론으로 구분하는 딕셔너리 
# for number, name in enumerate(students) 정의부분
students_dict = { "{}번".format(number+1) : name for number, name in enumerate(students) }
print(students_dict)

scores = [85, 92, 78, 90, 100]
for x, y in zip(students, scores):
    print(x, y)

score_dict = { "{}점".format(score) : "학생 {}".format(name) for score, name in zip(scores, students)}
print(score_dict)

