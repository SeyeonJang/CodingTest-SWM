# 그리디
# 실전 3-2. 큰 수의 법칙
# 문제 풀이 32' 29" (제한 풀이 시간 2분 29초 over)

n, m, k = input().split()  #input.split() 인터넷 봄
n = int(n)
m = int(m)
k = int(k)

arr = list(map(int, input().split()))  #list, map 인터넷봄
arr.sort(reverse=True) #sort 인터넷 봄
print(arr)

sum = 0
for i in range(m):
  if (i+1) % (k+1) == 0:
    sum += arr[1]
  else:
    sum += arr[0]
  print("합"+str(sum))

print(sum)