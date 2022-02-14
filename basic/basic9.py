'''
리스트와 내장함수(2)
'''
a = [23,12,36,53,19]
print(a[:3]) #0~2번까지 출력함
print(a[1:4]) #1~3까지 출력함
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
print()

for x in a:
    if x%2 == 1: #홀수만 출력
        print(x, end=' ')
print()

for x in enumerate(a): #튜플로 리턴함 (0, 23), (1, 12) ...
    print(x)
    print(x[1])

b=(1,2,3,4,5)
print(b)
print(b[2])
# b[0]=7 #error, 튜플은 리스트와 똑같지만, 리스트와는 다르게 값을 변경할 수 없음

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

if all(50>x for x in a): #all함수는 리스트가 가진 값이 조건문을 모두 참이여야 참
    print('True')
else:
    print('False')

if any(13>x for x in a): #any함수는 리스트가 가진 값이 조건문 중 하나라도 참이라면 모두 참
    print('True')
else:
    print('False')