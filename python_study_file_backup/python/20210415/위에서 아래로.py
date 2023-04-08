
# 수열을 내림차순으로 정렬하는 프로그램
#n = int( input() )
#
#graph = []
#for i in range(n) :
#    graph.append( int(input()) )
#
# sorted( array, reverse = True ) : 내림차순
#graph_sort1 = sorted( graph, reverse = True )
#
# none or reverse = False : 오름차순 
#graph_sort2 = sorted( graph )
#
#print('내림차순 : ', graph_sort1, '\n오름차순 : ', graph_sort2, '\n')



#성적이 낮은 순서로 학생 출력
#n 명의 학생 정보는 이름과 성적으로 구분됨
n = int( input() )
#name, grade = input().split()

student = []

for i in range(n) :
    input_data = input().split()
    student.append( (input_data[0] , int(input_data[1]) ) )    

#def def_key (data) :
#    return data[1]
#result = sorted(student, key=def_key)
# 람다함수(익명함수) lambda 인자 : 표현식
#result = sorted(student, key=lambda data : data[1])
result = sorted( student, key = (lambda data : data[1]) )

for i in result :
    print(i[0], end=' ')
print('\n')


#lambda 예시
def hap(x, y) :
    return x+y

print(hap(10,20))

print((lambda x, y : x+y)(10,20))
#lambda a, b : a%b










