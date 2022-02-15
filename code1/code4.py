import sys
sys.stdin = open('code1/input.txt', 'rt')
n = int(input())
a_list = list(map(int, input().split()))
avg = round(sum(a_list)/n)
min = float('inf')
for i, x in enumerate(a_list):
    tmp = abs(x-avg)
    if min > tmp:
        min = tmp
        score = x
        no = i+1
    elif tmp == min:
        if x > score:
            score = x
            no = i+1
print(avg, no)
