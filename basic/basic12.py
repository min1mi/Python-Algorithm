'''
람다 함수 => 익명함수, 람다 표현식이라고 불림
'''
#함수 정의
def plus_one(x):
    return x+1

# print(plus_one(1))

a=[1,2,3]
print(list(map(plus_one, a))) #map(함수명, 자료), 자료를 함수로 실행시킴

#람다 함수 정의
# plus_two = lambda x: x+2
# print(plus_two(1))

#내장함수에 인자로 쓸 때 편리함, sort 함수 사용할 때 주로 사용함
print(list(map(lambda x: x+1, a))) #map(함수명, 자료), 자료를 함수로 실행시킴


