# 그리디
# 실전 3-4. 1이 될 때까지
# 문제 풀이 5' 54" 근데 틀림 (n<k 경우 생각 안함)

result = 0
n, k = map(int, input().split())

while True:
  if n == 1:
    break
  if n % k == 0:
    n //= k
    result += 1
    continue
  n -= 1
  result += 1

print(result)

# 이코테 풀이1

n, k = map(int, input().split())
result = 0

#n이 k 이상이라면 k로 계속 나누기
while n >= k:
  #n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
  while n % k != 0:
    n -= 1
    result += 1
  #k로 나누기
  n //= k
  result += 1

#마지막으로 남은 수에 대해 1씩 빼기
while n > 1:
  n -= 1
  result += 1

print(result)

# 이코테 풀이2

n, k = map(int, input().split())
result = 0

while True:
  # (n==k로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
  target = (n // k) * k
  result += (n - target)  #나누어 떨어지는 수가 될 때까지 차이나는 만큼 한 번에 빼기 wow...
  n = target
  # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break
  # k로 나누기
  result += 1
  n //= k

# 마지막으로 남은 수 1씩 빼기
result += (n - 1)
print(result)
