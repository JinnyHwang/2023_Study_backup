'''
DFS/BFS

그래프 graphs
정점(vertex, node)과 간선(edge, link)
유향(directed)그래프와 무향(undirected)그래프
스택(stack)
큐(queue)


깊이우선탐색 DFS
한 정점에서 인접한 모든 정점을 방문하되
각 인접 정점을 기준으로 깊이 우선 탐색을 끝낸 후
다음 정점으로 진행
-> 스택을 이용하여
어느 정점에서 DFS를 하고있는지 기억하고 돌아감


넒이우선탐색 BFS
한 정점에서 인접한 모든 정점을 방문하되
방문한 각 인접 정점을 기준으로 너비우선탐색 행함
-> 큐를 이용하여
어느 정점에서 BFS를 해야하는지 기억하고 돌아감
'''






t1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
t2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]














