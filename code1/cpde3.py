import sys
sys.stdin=open('code1/input.txt', 'rt')

n, k = map(int, input().split(' '))
a_list = list(map(int, input().split(' ')))
result = set() # 중복제거

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            result.add(a_list[i]+a_list[j]+a_list[m])

result = list(result)
result.sort(reverse=True)
 
print(result[k-1])