n = int(input())

array = []

for _ in range(n):
  name, score = input().split()
  array.append([name, int(score)])

array = sorted(array, key=lambda student: student[1])
# -> sorted함수가 array의 요소 람다함수에게 하나씩 전달 -> 그 전달된 매개변수는 student이라는 인자에 담김

# def get_score(student):
#   return student[1]

# sorted 함수의 key 인자로 get_score를 전달
# 주의: 함수를 호출하는 것이 아니라, 함수 이름 자체를 전달해야 합니다 -> get_score() (X)
# sorted_students = sorted(array, key=get_score)

# lamda 인자, 표현식
# def add(x,y):
#    return x + y

# lamda x,y : x + y

for student in array:
  print(student[0], end=' ')
