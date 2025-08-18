# 입력 받기
input_data = input()

# 파이썬에서는 문자열(string)도 리스트처럼 인덱스(index)로 바로 접근할 수 있음
# ord() 함수는 하나의 문자를 유니코드 정수로 변환

# 행: 문자를 숫자로 변환 후 -1 (e.g. '1' -> 1 -> 0)
row = int(input_data[1]) - 1
# 열: ord() 함수 이용 (e.g. 'a' -> 0)
column = ord(input_data[0]) - ord('a')

# 나이트의 8가지 이동 방향 벡터 (steps)
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

result = 0
for step in steps:
  # 이동 후의 위치 계산
  next_row = row + step[0]
  next_column = column + step[1]
  
  # 해당 위치가 체스판 내에 있는지 확인
  if 0 <= next_row <= 7 and 0 <= next_column <= 7:
    result += 1

print(result)
