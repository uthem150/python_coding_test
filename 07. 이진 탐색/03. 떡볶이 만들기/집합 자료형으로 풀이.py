# 해시(Hash)를 이용하는 Set 자료구조를 사용하면 탐색 시간이 평균 O(1)

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if i in array:
    print('yes', end=' ')
  else:
    print('no', end=' ')
