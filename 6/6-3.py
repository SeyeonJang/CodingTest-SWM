# 정렬
# 퀵 정렬 예제 6-5.py(책)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
  if len(array) <= 1:
    return array

  pivot = array[0]  #피벗은 첫 번째 원소
  tail = array[1:]  #피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot]  #분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot]  #분할된 오른쪽 부분

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))