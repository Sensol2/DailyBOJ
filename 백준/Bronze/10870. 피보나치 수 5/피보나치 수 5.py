def pibo(n):
    if(n>1):
        return pibo(n-1)+pibo(n-2)
    elif(n==1):
        return 1
    else:
        return 0
    
N=int(input())
print(pibo(N))