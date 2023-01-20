# 구현
# 예제 4-1 상하좌우
# 문제 풀이 17' 41"

n = int(input(""))
data = list(map(str, input().split()))

x = 1
y = 1
for a in data:
  if a == 'R':
    y += 1
  elif a == 'L':
    y -= 1
  elif a == 'U':
    x -= 1
  else:
    x += 1
  if x < 1:
    x = 1
  elif x > n:
    x = n
  elif y < 1:
    y = 1
  elif y > n:
    y = n
  print("%c %d %d" % (a, x, y))

print("%d %d" % (x, y))

# 이코테 풀이

n = int(input())
x, y = 1, 1  #아 변수 2개면 이렇게 받아야 함
plans = input().split()  # char형이라서 list, map 따로 안 넣음!

#L,R,U,D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획 하나씩 확인
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간 벗어나는 경우 무시
  if nx < 1 or ny > 1 or nx > n or ny > n:  #무시하는 코드 넣어서 한 번에 처리 가능!!!
    continue
  # 이동 수행
  x, y = nx, ny

print(x, y)

# 리스트 초기화하는 코드 몇 줄 더 쓰더라도 이게 깔끔하다 훨씬 ... 내가 쓴 게 더 짧지만 이게 더 깔끔함