'''
반복문(for, while)
'''
# a = range(10) #range 함수는 순차적으로 정수 리스트를 만든다.
# print(list(a))
# a = range(1, 11)
# print(list(a))

# for i in range(10):
#     print(i)

# for i in range(10, 0, -2):
#     print(i)

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# i = 10
# while i >= 1:
#     print(i)
#     i = i - 1

#반복문 멈추기
# i = 1
# while True:
#     print(i)
#     if i == 10:
#         break
#     i += 1

# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#         print("짝수")
#     print(i)

for i in range(1, 11):
    print(i)
    if i == 5:
        break
else: #for문이 정상적으로 종료될 경우 else가 실행됨
    print(11)
