'''
2차원 리스트 생성과 접근
'''
# a=[0]*3
# print(a)
a=[[0]*3 for _ in range(3)] #반복문이 3번 돌면서 [0]*3이 수행됨
print(a)
# a | 0 1 2
# ---------
# 0 | 0 0 0 
# 1 | 0 0 0
# 2 | 0 0 0
a[0][1] = 1
print(a)
a[1][1] = 2
print(a)

for x in a:
    print(x)

for x in a:
    for y in x:
        print(y, end =' ')
    print()