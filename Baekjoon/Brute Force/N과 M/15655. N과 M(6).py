import sys
n,m = map(int,input().split())

used = [False] * n
result = [0]*m

arr = list(map(int,input().split()))
arr.sort()
index=0

def recursive(index,start,n,m):
    if index==m:
        sys.stdout.write(' '.join(map(str,result))+'\n')
        return

    for i in range(start,n):
        if used[i]:
            continue
        else:
            used[i] = True
            result[index] = arr[i]
            recursive(index+1,i+1,n,m)
            used[i] = False

recursive(0,0,n,m)