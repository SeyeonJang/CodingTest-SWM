# 정렬
# 실전 - 위에서 아래로
# 문제 풀이 시간 10분 미만 of 15분

n = int(input())
array = [0] * n

for i in range(n):
  array[i] = int(input())
array.sort(reverse=True)

for i in range(n - 1):
  print(array[i], end=' ')
print(array[n - 1])

# 이코테 풀이
n = int(input())

array = []
for i in range(n):
  array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
  print(i, end=' ')
