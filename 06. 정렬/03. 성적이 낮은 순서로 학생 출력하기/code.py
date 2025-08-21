n = int(input())

array = []

for _ in range(n):
  name, score = input().split()
  array.append((name, int(score)))

array = sorted(array, key=lambda student: student[1])

for i in range(n):
  print(array[i][0], end=" ")

# for student in array:
#   print(student[0], end=" ")
