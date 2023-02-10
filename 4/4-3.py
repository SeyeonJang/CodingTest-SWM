# 구현
# 실전 4-3. 왕실의 나이트
# 문제 풀이 시간 14' 06"

n = input()

row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
col = ['1', '2', '3', '4', '5', '6', '7', '8']

sum = 8
for i in row:
  if n[0] == i:
    if i == 'a' or i == 'h': sum -= 3
    elif i == 'b' or i == 'g': sum -= 2
for j in col:
  if n[1] == j:
    if j == '1' or j == '8': sum -= 3
    elif j == '2' or j == '7': sum -= 2

print(sum)

# 이코테 풀이

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(
  ord('a')) + 1  #ord는 아스키코드 변환 함수, ord('a') = 97

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2),
         (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
  #이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = column + step[1]
  # 해당 위치로 이동이 가능하다면 카운트 증가
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

print(result)
