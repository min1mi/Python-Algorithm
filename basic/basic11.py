'''
함수 만들기
'''
# def add(a, b):
#     c = a + b
#     print(c)

# add(3,2)
# add(5,6)

# def add(a, b):
#     c=a+b
#     return c

# x = add(1,3)
# print(x)

# def add(a, b):
#     c=a+b
#     d=a-b
#     return c, d #튜플로 리턴됨

# print(add(3,2))


#소수만 찾는 프로그램
def isPrime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

a = [12,13,7,9,19]

for y in a:
    if isPrime(y):
        print(y, end=' ')


