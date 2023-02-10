# 구현
# 실전 4-4. 게임 개발
# 문제 풀이 시간 59' 20" (시간 19'20" 넘김, 콘솔창에 출력 안 나와서 실패함)

n, m = map(int, input().split())
a, b, direct = map(int, input().split())
# 리스트로 입력받는 거 책 보고 함
gameMap = []
for i in range(n):
  gameMap.append(list(map(int, input().split())))

direction = [0, 1, 2, 3]  #북동남서 wdsa
move = [(0, -1), (1, 0), (0, 1), (-1, 0)]
my = [(a, b)]
myWay = []

cnt = 0
bp = 0
while True:
  if a < 0 or b < 0 or a >= n or b >= m: break  #화면 넘어가면 break
  if bp > 0: break
  for d in direction:
    if d == direct:
      direct += 1
      if direct > 3: direct = 0  #방향 설정하기

  # 캐릭터 옮기기
  my[0] += move[direct]
  if a < 0 or b < 0 or a >= n or b >= m: break  #맵 넘어가면 break >> '맵의 외곽은 항상 바다로 되어있다' >> 필요없음
  for i in myWay:
    if i == my[0]:  #만약 가본 칸이라면
      my[0] -= move[direct] * 2
    else:  #안 가본 칸 중에
      myWay.append((a, b))
      if gameMap[a][b] != 1:  #육지라면 cnt++
        cnt += 1
      else:  #바다라면
        my[0] -= move[direct] * 2
        cnt += 1
        #또 뒤로 갔는데도 바다라면
        if gameMap[a][b] == 1:
          bp += 1
    break

print(cnt)



# 이코테 답

# N,M 공백으로 구분하여 입력받기
n,m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)] # 이거 중요 ************************
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 #현재 좌표 방문 처리

# 전체 맵 정보 입력받기
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction =3

# 시뮬레이션 시작
count = 1 #1로 시작하는거.....
turn_time = 0
while True:
  #왼쪽으로 회전
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
  if d[nx][ny] == 0 and array[nx][ny]==0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_time += 1
  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있다면 이동하기
    if array[nx][ny]==0:
      x = nx
      y = ny
    # 뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time = 0

# 정답 출력
print(count)