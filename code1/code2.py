import sys
sys.stdin=open("code1/input.txt", 'rt')

T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split(' '))
    a_list = list(map(int, input().split(' ')))

    a_list = a_list[s-1:e]
    a_list.sort()

    print("#%d %d" %(t+1, a_list[k-1]))