n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 오름차순 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0
count = 0

for _ in range(m):
  if count < k:  # counter가 k번이 되기 전까지는
    result += first
    count += 1
  else:  # counter가 k번이 되면
    result += second
    count = 0  # counter 초기화

print(result)
