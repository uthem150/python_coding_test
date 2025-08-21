import sys

n = int(input())
market_list = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
customer_list = list(map(int, sys.stdin.readline().rstrip().split()))

# nlogn
sorted_market_list = sorted(market_list)


# 이진 탐색 1번시 logn
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if (target == array[mid]):
      return "yes"

    elif (target <= array[mid]):
      end = mid - 1

    else:
      start = mid + 1

  return "no"


# m개의 요소에 대해 binary search (m*logn)
for i in range(m):
  print(binary_search(sorted_market_list, customer_list[i], 0, n - 1), end=" ")

# 총 (m+n)logn
