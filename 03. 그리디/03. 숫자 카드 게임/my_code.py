n, m = list(map(int, input().split()))
row_min_list = list()

for _ in range(n):
  tmp_list = list(map(int, input().split()))
  row_min_list.append(min(tmp_list))

result = max(row_min_list)

print(result)
