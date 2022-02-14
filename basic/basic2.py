'''
변수입력과 연산자
'''
# a = input("숫자를 입력하세요 : ")
# print(a)


# a, b = input("숫자를 입력하세요 : ").split()
# print(type(a))
# print(a + b) # 23 : 문자형이라서 두 숫자가 연결되서 보여짐
# a = int(a)
# b = int(b)
# print(a, b)
# print(type(a))
# print(type(b))
# print(a+b)

a, b = map(int, input("숫자를 입력하세요 : ").split()) # 두개의 숫자를 받아서 int로 변경해서 맵핑해줌
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #몫
print(a%b) #나머지
print(a**b) #거듭제곱

a = 4.3
b = 5
c = a + b
print(type(c))
