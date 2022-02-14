'''
리스트와 내장함수(1)
'''
import random as r
a = []
# print(a)
b = list()
# print(b)

c=[1,2,3,4,5]
# print(c)
# print(c[0])

b=list(range(1,11))
# print(b)

a = c+b
# print(a)

print(c)
c.append(6)
print(c)

c.insert(3, 7)
print(c)

c.pop() #맨뒤에 값을 제거함
print(c)
c.pop(3) #3번 인덱스 값이 제거됨
print(c)

c.remove(4) #4라는 값을 찾아서 제거함
print(c)

print(c.index(5)) #c에서 5라는 값의 인덱스값을 리턴함

c=list(range(1,11))
print(c)
print(sum(c)) #리스트의 모든 값을 합침
print(max(c)) #리스트의 모든 값 중 가장 큰 값을 리턴함
print(min(c)) #리스트의 모든 값 중 가장 작은 값을 리턴함
print(min(7,5)) #인자값 중 최소값을 찾아줌

print(c)
r.shuffle(c) #랜덤으로 섞음
print(c)
c.sort() #오름차순 정렬
print(c)
c.sort(reverse=True) #내림차순 정렬
print(c)
c.clear() #리스트에 값을 모두 지움
print(c)
