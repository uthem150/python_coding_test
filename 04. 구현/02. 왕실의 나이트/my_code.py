location_string = input()

# location_list[0] location_list[1]로 각각 얻기 위함
location_list = list(location_string)

column_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row_list = ['1', '2', '3', '4', '5', '6', '7', '8']

column_pos = 0
row_pos = 0

while True:
  if (column_list[column_pos] == location_list[0]):
    break
  column_pos = column_pos + 1

while True:
  if (row_list[row_pos] == location_list[1]):
    break
  row_pos = row_pos + 1

# 이동 가능한 8가지
dx = [2, 2, 1, -1, -2, -2, 1, -1]
dy = [1, -1, -2, -2, 1, -1, 2, 2]

# position이 하나라도 지정된 범위를 벗어나면, 그건 카운트하지 x
# 계산 후 행 열 모두 범위 0~7 사이어야 함.
result = 0

for i in range(8):
  if (column_pos + dx[i] < 0 or column_pos + dx[i] > 7):
    continue
  elif (row_pos + dy[i] < 0 or row_pos + dy[i] > 7):
    continue
  else:
    result += 1

print(result)
