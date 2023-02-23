# 정렬
# 실전 - 성적이 낮은 순서로 학생 출력하기
# 문제 풀이 시간 5분(알고리즘 only, 구현은 튜플 몰라서 못 했음) of 20분

# n = int(input())

# dict = {}
# for i in range(n):
#   name, score = dict(map(input().split()))
#   score = int(score)
# dict.sort()

# for i in range(n):
#   print(dict[i].value, end=' ')

# 위 코드는 튜플 몰라서 틀렸음.
# 이코테 풀이

n = int(input())

array = []
for i in range(n):
  input_data = input().split()  #자동으로 리스트로 저장되나봐
  array.append(
    (input_data[0], int(input_data[1])))  #이거 괄호 하나 더 쳐준 이유가 튜플로 들어가서임 ㄷ

array = sorted(array, key=lambda student: student[1])

for student in array:
  print(student[0], end=' ')
