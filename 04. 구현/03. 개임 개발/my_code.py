# 세로 크기 n, 가로 크기 m
n, m = map(int, input().split())

# 처음 좌표 , 방향 d
distance_from_noth, distance_from_south, d = map(int, input().split())
world = []

for _ in range(n):
  world.append(list(map(int, input().split())))

visited_block = 1
world[distance_from_noth][distance_from_south] = 2


# 사용자 방향은 북,동,남,서
def rotate():
  global d
  # 북쪽 -> 서쪽
  if (d == 0):
    d += 3
  # 서쪽 -> 남쪽
  elif (d == 3):
    d -= 1
  # 남쪽 -> 동쪽
  elif (d == 2):
    d -= 1
  # 동쪽 -> 북쪽
  else:
    d -= 1


#            북, 동, 남, 서 한칸씩 이동
east_move = [0, 1, 0, -1]
south_move = [-1, 0, 1, 0]

direction_counter = 0

# 일단 rotate하고, 전진 or stop
while True:
  # 1. 일단 회전
  rotate()
  # 회전 수 증가
  direction_counter += 1

  # 2. 만약 해당 방향으로 0이 있으면 전진
  if (world[distance_from_noth + south_move[d]][distance_from_south +
                                                east_move[d]] == 0):
    distance_from_noth += south_move[d]
    distance_from_south += east_move[d]
    # 갔다고 체크
    world[distance_from_noth][distance_from_south] = 2
    visited_block += 1
    direction_counter = 0
    continue

  # 4방향 모두 갈 곳 없음
  if (direction_counter == 4):
    # 후진
    if (world[distance_from_noth - south_move[d]][distance_from_south -
                                                  east_move[d]] == 2):
      distance_from_noth -= south_move[d]
      distance_from_south -= east_move[d]
      direction_counter = 0
      continue

    if (world[distance_from_noth - south_move[d]][distance_from_south -
                                                  east_move[d]] == 1):
      break

print(visited_block)
