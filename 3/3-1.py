# 그리디
# 예제 3-1 거스름돈
# 문제 풀이 9분
'''
num = int(input("숫자:"))
if num > 500:
  count = num // 500 + (num % 500) // 100 + ((num % 500) % 100) // 50 + (((num % 500) % 100) % 50) // 10
elif num >= 100 and num < 500:
  count = num // 100 + (num % 100) // 50 + ((num % 100) % 50) // 10
elif num >= 50 and num < 100:
  count = num // 50 + (num % 50) // 10
else:
  count = num // 10
print(count) '''

# 이코테 답

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
  n %= coin
  count += n  #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기

print(count)
