n = int(input())

list = []

for _ in range(n):
  list.append(int(input()))

list.sort(reverse=True)

for i in range(n):
  print(list[i], end=" ")


# .sort()는 리스트 자체를 그 자리에서 수정하고, 
# sorted()는 새로운 정렬된 리스트를 반환하는 것이 가장 큰 차이점

# 구분	|  .sort()	|  sorted()
# 작동 방식	|  원본 리스트를 직접 변경 (In-place)	|  원본은 그대로 두고, 새로운 리스트를 생성하여 반환
# 반환 값	|  None (리스트를 직접 수정하므로 반환 값이 없음)	|  정렬된 새로운 리스트
# 사용 대상	|  리스트 자료형에서만 사용 가능 (메서드)	|  모든 반복 가능한(iterable) 객체에 사용 가능 (내장 함수)
# 사용법	  |  my_list.sort()	|  new_list = sorted(my_iterable)

# .sort는 list에서만 사용 가능한 메소드이므로, sorted( iterable, reverse=True)를 사용하는게 좀더 맞을 것 같음
