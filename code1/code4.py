import sys
sys.stdin = open('code1/input.txt', 'rt')
n = int(input())
a_list = list(map(int, input().split()))
#round()는 round_half_even 방식을 택함
# avg = round(sum(a_list)/n)
avg = int(sum(a_list)/n + 0.5)

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
