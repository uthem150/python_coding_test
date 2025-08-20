n, m = map(int, input().split())

graph = []

for _ in range(n):
  graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
  if not (0 <= x < n and 0 <= y < m):
    return False

  elif (graph[x][y] == 0):
    graph[x][y] = 1

    dfs(x + dx[0], y + dy[0])
    dfs(x + dx[1], y + dy[1])
    dfs(x + dx[2], y + dy[2])
    dfs(x + dx[3], y + dy[3])

    return True

  else:
    return False


count = 0

for i in range(n):
  for j in range(m):
    if (dfs(i, j)):
      count += 1

print(count)
