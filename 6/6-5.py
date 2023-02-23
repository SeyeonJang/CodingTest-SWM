# 정렬
# 계수 정렬 예제 6-6.py(책)

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)  #모든 값 포함하는 리스트 선언, 0으로 초기화, 크기는 max값+1

for i in range(len(array)):
  count[array[i]] += 1  #각 데이터에 해당하는 인덱스 값 증가

for i in range(len(count)):  #0~9 돌기
  for j in range(count[i]):  #자리에 있는 수 만큼
    print(i, end=' ')
