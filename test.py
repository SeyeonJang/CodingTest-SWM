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
