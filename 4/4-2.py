# 구현
# 예제 4-2 시각 14' 03"
# 문제 풀이

n = int(input())
#t_list = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]
# 3이 들어간 분 * 모든 초 = 15*60
# 3이 안 들어간 분 * 3이 들어간 초 = 45*15

sum = 0
if n == 3 or n == 13 or n == 23:
  for i in range(n + 1):
    sum += 60 * 60
else:
  for i in range(n + 1):
    if i == 3 or i == 13 or i == 23: sum += 60 * 60
    else: sum += (15 * 60 + 45 * 15)

print(sum)

# 이코테 풀이

# H 입력받기
h = int(input())

count = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k):
        count += 1
print(count)
