
'''
https://yoongrammer.tistory.com/86
위상 정렬 Topological sort

비순환 방향 그래프(DAG: Directed Acylic Graph)
사이클이 없는 방향 그래프
이벤트 간의 우선순위를 나태내기 위해 주로 사용
정점을 선형으로 정렬, 싸이클이 없음, 모든 간선(u,v)에 대해  u가 v보다 먼저 오는 순서
DAG가 아닌 경우 그래프에 대한 위상 정렬 불가능
=> 선수과목 수강 문제가 DAG, 위상정렬의 가장 대표적인 예
위상 정렬 진행 시 모든 간선은 오른쪽을 가리키게됨

정점에 들어오는 간선 수를 저장하기 위해 iin_degree[N] 배열 사용
i번째 요소는 정점 i로 들어오는 가장자리 수 저장

1. 모든 정점의 in_degree 설정
2. in_degree가 0인 정점은 방문한 것으로 표시, queue에 정점 추가
3. queue가 빌 때가지 순회하며 작업 수행
- queue의 앞 요소를 dequeue()로 가져와서 T[]에 append
- dequeue()한 정점에 인접한 정점 중 방문하지 않은 정점의 in_dgree 하나 감소
- in_degree 감소 후 값이 0이면 해당 정점은 queue에 enqueue()하고 방문한 것으로 표시

step1
각 노드의 간선 수 in_degree에 저장

step2
in_degree가 0인 정점 확인(가장 끝에 위치하는 정점)
해당 정점을 queue에 삽입, 방문 표시

step3
queue에서 dequeue해서 나온 node를 T[]에 append
그리고 해당 node의 인접 node 중 방문하지 않은 node의 n_degree 값 1 감소
만약 in_degree 값이 0이라면 queue에 enqueue, 방문 표시

step1 ~ step3 반복 queue가 비면 stop
T[]를 return
'''










