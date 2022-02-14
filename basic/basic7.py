'''
문자열과 내장함수
'''
msg = "It is Time"
print(msg.upper()) #모든 문자를 대문자화 시킴
print(msg.lower()) #모든 문자를 소문자화 시킴
print(msg)

tmp = msg.upper()
print(tmp)
print(tmp.find('T')) #처음 발견되는 T의 인덱스번호를 리턴함
print(tmp.count('T')) #전체에서 T의 개수를 리턴함
print(msg)
print(msg[:2]) #처음부터 인덱스2번 전까지 출력
print(msg[3:5])
print(len(msg)) #문자열의 총 길이(공백포함)

for i in range(len(msg)):
    print(msg[i], end='')
print()

for x in msg:
    print(x, end='')
print()

for x in msg:
    if x.isupper(): #isupper()는 대문자인지 확인하는 함수
        print(x, end=" ")
print()

for x in msg:
    if x.islower(): #islower()는 소문자인지 확인하는 함수
        print(x, end="")
print()

for x in msg:
    if x.isalpha(): #isalpha()는 알파벳인지 확인하는 함수
        print(x, end="")
print()

tmp='AZ'
for x in tmp:
    print(ord(x)) #ord()는 아스키번호를 출력해줌, A=65, Z=90

tmp='az'
for x in tmp:
    print(ord(x))

tmp=65
print(chr(tmp)) #아스키번호에 대응되는 문자를 출력해줌
