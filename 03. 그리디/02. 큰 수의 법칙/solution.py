# N(배열 크기), M(총 덧셈 횟수), K(연속 가능 횟수)를 입력받습니다.
n, m, k = map(int, input().split())

# N개의 숫자로 이루어진 배열을 입력받습니다.
data = list(map(int, input().split()))

# 입력받은 배열을 오름차순으로 정렬합니다.
data.sort()

first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 반복문을 사용하면, M크기가 커지면 시간초과 판정
# -> 반복되는 수열의 패턴을 찾아 수학적으로 계산

# 가장 큰 수(first)가 K번, 두 번째로 큰 수(second)가 1번 나오는 
# (k+1) 크기의 수열이 반복되는 횟수를 계산
# 예를 들어 M=8, K=3이면 (6,6,6,5)라는 크기 4짜리 수열이 8 // 4 = 2번 반복
count_of_sequence = m // (k + 1)

# 위 수열이 반복된 후, 남은 덧셈 횟수를 계산
# M=8, K=3이면 8 % 4 = 0, 즉 남는 숫자가 없음
# M=10, K=3이면 10 % 4 = 2, 즉 2번을 더 더해야 함
remainder = m % (k + 1)

# 가장 큰 수가 총 몇 번 더해지는지 계산
# (수열 반복 횟수 * 수열 내 가장 큰 수의 등장 횟수(k)) + 남은 횟수
count_of_first = (count_of_sequence * k) + remainder

# 두 번째로 큰 수가 총 몇 번 더해지는지 계산
# M에서 가장 큰 수가 더해진 횟수를 뺌
count_of_second = m - count_of_first

# 최종 결과를 계산
# (가장 큰 수 * 더해진 횟수) + (두 번째로 큰 수 * 더해진 횟수)
result = (first * count_of_first) + (second * count_of_second)

# 최종 결과를 출력
print(result)
