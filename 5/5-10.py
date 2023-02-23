# DFS/BFS
# 실전. 음료수 얼려 먹기
# 문제 풀이 시간 17' 45" (못 풀어서 포기...)


def dfs(graph, v, visited):
  for i in range(n):
    for j in range(m):
      v = graph[i][j]
      if v is not visited[True] and v == 0:
        dfs(graph, v, visited)


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
  data = list(map(int, input().split("")))
  graph[i].append(data)

print(graph)  #graph 테스트용

visited = [[False] * m] * n

dfs(graph, 0, visited)

# 이코테 풀이 =================

n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))  #split 없으면 붙어있는 거 그냥 받을 수 있나봄 기억하기


# DFS로 특정한 노드 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
  # 주어진 범위 벗어나는 경우 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  # 현재 노드 아직 방문하지 않았다면
  if graph[x][y] == 0:
    graph[x][y] = 1  # 노드 방문처리
    # 상,하,좌,우 위치 재귀적 호출
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False


# 모든 노드(위치)에 대해 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    #현재 위치에서 DFS 수행
    if dfs(i, j) == True:
      result += 1

print(result)
