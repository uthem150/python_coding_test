# 세로길이 N, 가로길이 M
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들 방문
# 일반적으로 수학 좌표계에서는 (x, y)가 **가로(x축), 세로(y축)**를 의미하지만, 
# 프로그래밍에서 2차원 리스트(배열)를 다룰 때는 관례적으로 첫 번째 인덱스를 행, 두 번째 인덱스를 열로 사용
def dfs(x, y):
    # 좌표가 범위 벗어나면 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    # 현재 노드를 방문하지 않음
    # graph의 x번째 행, y번째 열의 원소
    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문처리

        # 상하좌우 모두 재귀적으로 DFS 함수 호출
        dfs(x+1, y) 
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False


result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)
