# 구현
# 실전 4-4. 게임 개발
# 문제 풀이 시간 

n, m = map(int, input().split())
a, b, direct = map(int, input().split())
# 리스트로 입력받는 거 책 보고 함
gameMap = []
for i in range(n):
  gameMap.append(list(map(int, input().split())))

direction = [0,1,2,3] #북동남서 wdsa
move = [(0,-1), (1,0), (0,1), (-1,0)]
my = [(a,b)]
myWay = []

cnt = 0
bp = 0
while True:
  if a<0 or b<0 or a>=n or b>=m: break #화면 넘어가면 break
  if bp>0: break
  for d in direction:
      if d==direct:
        direct += 1
        if direct>3: direct=0 #방향 설정하기

  # 캐릭터 옮기기        
  my[0] += move[direct]
  if a<0 or b<0 or a>=n or b>=m: break #화면 넘어가면 break
  for i in myWay:
    if i==my[0]: #만약 가본 칸이라면
      my[0] -= move[direct] * 2
    else: #안 가본 칸 중에
      myWay.append((a,b))
      if gameMap[a][b] != 1: #육지라면 cnt++
        cnt += 1
      else: #바다라면
        my[0] -= move[direct] * 2
        cnt += 1
        #또 뒤로 갔는데도 바다라면
        if gameMap[a][b] == 1:
          bp += 1
    break

print(cnt)