n, m = map(int, input().split())

# 결과를 저장할 변수. 첫 비교를 위해 0으로 초기화.
# (카드 숫자는 1 이상이므로 0으로 해도 안전합니다)
result = 0

for _ in range(n):
  data = list(map(int, input().split()))
  # 현재 행의 최솟값을 찾음
  min_value = min(data)
  # 기존의 최댓값(result)과 현재 행의 최솟값(min_value)을 비교하여 더 큰 값을 선택
  result = max(result, min_value)

print(result)

# 변경점: row_min_list를 사용하는 대신, result 변수를 루프가 돌 때마다 갱신합니다.
# 장점: N개의 데이터를 저장할 추가 메모리가 필요 없어지므로 공간 복잡도가 **O(1)**으로 개선됩니다. 
# N이 매우 커지는 상황(예: 100만)이라면 이 방식이 훨씬 효율적입니다.
