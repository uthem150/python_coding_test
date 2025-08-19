from collections import deque

n, m = map(int, input().split())

world = []

for _ in range(n):
  world.append(list(map(int, input())))

# 이동할 네 방향 정의 (상, 하, 좌, 우)
# 2차원 배열 코드에서는, x,y 반대임
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
  # 방문할 노드를 저장할 큐(queue)를 생성합니다.
  queue = deque()
  # 시작 노드 (x, y)를 튜플 형태로 큐에 추가합니다.
  queue.append((x, y))

  # 큐가 빌 때까지 반복
  while queue:
    # 가장 먼저 들어온 노드를 꺼내 현재 위치로 설정합니다.
    x, y = queue.popleft()

    # 현재 위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 미로 공간 벗어난 경우 무시
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      # 벽인 경우 무시
      if world[nx][ny] == 0:
        continue

      # [핵심 로직] 다음 위치가 길(값이 1)이고, 처음 방문하는 경우
      # BFS의 특성상, 어떤 노드에 도착했을 때 그 경로는 항상 최단 거리입니다.
      # 따라서 처음 방문할 때의 거리만 기록하면 됩니다.
      if world[nx][ny] == 1:
        # 이전 위치의 최단 거리에 1을 더해 현재 위치의 최단 거리를 기록합니다.
        # 이 방식은 별도의 거리 측정 배열 없이, 맵 자체에 거리를 기록하는 방법
        world[nx][ny] = world[x][y] + 1
        # 다음 탐색을 위해 현재 위치를 큐에 추가합니다.
        queue.append((nx, ny))

  # 가장 오른쪽 아래까지의 최단 거리 반환
  return world[n - 1][m - 1]


# BFS 수행 결과 출력
print(bfs(0, 0))
