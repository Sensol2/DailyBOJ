import math

while True:
    N = list(input())
    if N == ['0']:
        break

    if len(N) % 2 == 0: # 짝수면 중간에 아무 수 하나 끼워넣기
        N.insert(len(N)//2, '0')
    
    median = math.ceil(len(N) / 2) - 1
    if N[0:median] == list(reversed(N[median+1:])):
        print("yes")
    else:
        print("no")