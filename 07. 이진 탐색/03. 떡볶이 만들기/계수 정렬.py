n = int(input())
array = [0] * 1000001

# 가게에 있는 부품 번호 받아서 입력 -> 있으면 1로 표시
for i in input().split():
  array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

# 확인 요청한 부품 번호를 하나씩 확인
for i in x:
  # 해당 부품이 존재하는지 확인
  if array[i] == 1:
    print('yes', end=' ')
  else:
    print('no', end=' ')
