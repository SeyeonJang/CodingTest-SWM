# 정렬
# 실전 - 두 배열의 원소 교체
# 문제 풀이 시간 9'24" of 20'

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(k):
  a.sort()
  b.sort()
  if a[0] > b[n - 1]: break

  a[0], b[n - 1] = b[n - 1], a[0]

print(sum(a))

# 이코테 풀이
# 내 풀이랑 비슷한데 얘는 reverse=True 써서 정렬 반복 없이 비교할 수 있게 만듦

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))
