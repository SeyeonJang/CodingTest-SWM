# 그리디
# 실전 3-3. 숫자 카드 게임
# 문제 풀이 20' 40"

n, m = map(int, input().split())
arr = [[0 for col in range(n)] for row in range(m)]  # 배열 선언법 구글링함
print("done")

for i in range(n):
  arr[i] = list(map(int, input().split()))
  arr[i].sort()
  print(arr[i][0], arr[i][1], arr[i][2])

arr.sort(reverse=True)
print(arr[0][0])

# 이코테 풀이 (배열을 안 쓰고 min, max 이용함... 와)

n, m = map(int, input().split())

result = 0
for i in range(n):  #한 줄씩 입력받기
  data = list(map(int, input().split()))
  min_value = min(data)  #현재 줄에서 가장 작은 수 찾기
  result = max(result, min_value)  #가장 작은 수 중 가장 큰 수 찾기

print(result)

# 이코테 풀이2 (2중 반복문)

n, m = map(int, input().split())

result = 0
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 가장 작은 수 찾기
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)
  # 가장 작은 수 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)
