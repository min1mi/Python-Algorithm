'''
변수명 정하기
1) 영문과 숫자, _로 이루어짐
2) 대소문자를 구분
3) 문자나, _로 시작함
4) 특수문자 사용하면 안됨(&, % 등)
5) 키워드를 사용하면 안됨(if, for 등)
'''

a = 1
A = 2
print(a, A)


a, b, c = 3, 2, 1
print(a, b, c)

#값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

#변수 타입
a = 1234512345123412312312313123123123
print(a)
a = 12.123123123145678912345678 #실수는 8바이트가 넘어가면 데이터가 손실된다
print(a)
print(type(a))
a = 'student'
print(a)
print(type(a))

#출력방식
print("number")
a, b, c, = 1, 2, 3
print(a, b, c)
print("number : ", a, b, c)
print(a, b, c, sep=', ') #sep = 변수 사이의 공간을 어떤 형식으로 보여줄지에 대해 정의
print(a, b, c, sep='\n')
print(a, end=' ') #end = 기본적으로 print 함수는 개행이 되는데 개행을 하지 않고 싶을 경우 사용함
print(b, end=' ')
print(c)