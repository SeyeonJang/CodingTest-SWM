# 그리디
# 실전 3-2. 큰 수의 법칙
# 문제 풀이 32' 29" (제한 풀이 시간 2분 29초 over)

n, m, k = input().split()  #input.split() 인터넷 봄
n = int(n)
m = int(m)
k = int(k)

arr = list(map(int, input().split()))  #list, map 인터넷봄
arr.sort(reverse=True)  #sort 인터넷 봄
#print(arr) #확인용

sum = 0
for i in range(m):
  if (i + 1) % (k + 1) == 0:
    sum += arr[1]
  else:
    sum += arr[0]
  #print("합" + str(sum)) #확인용

print(sum)

# 이코테 풀이

n, m, k = map(int, input().split())  #이렇게 하면 내가 int 다 처리해준 것처럼 안 해도 됨
data = list(map(int, input().split()))  #n개의 수 공백으로 구분하여 받기

data.sort()
first = data[n - 1]  #첫 번째로 큰 수
second = data[n - 2]  #두 번째로 큰 수

result = 0

while True:
  for i in range(k):  #가장 큰 수 k번 더하기
    if m == 0:  #m이 0이라면 반복문 탈출
      break
    result += first
    m -= 1  #더할 때마다 m 1씩 빼기
  if m == 0:  #m이 0이라면 반복문 탈출
    break
  result += second  #두 번째로 큰 수 한 번 더하기
  m -= 1  #더할 때마다 1씩 빼기
print(result)  #최종 답안 출력
