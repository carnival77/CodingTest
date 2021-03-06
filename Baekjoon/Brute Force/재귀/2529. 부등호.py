k = int(input())
arr = list(input().split())
used=[False]*10
ans=[]

def check(num,k):
    for i in range(k):
        if arr[i] == '<':
            if (int(num[i]) < int(num[i+1]))==False:
                return False
        if arr[i] == '>':
            if (int(num[i]) > int(num[i+1]))==False:
                return False
    return True

def recur(index,num,k):
    if index == k+1:
        if check(num,k):
            ans.append(num)
            return

    for i in range(10):
        if used[i]: continue
        used[i] = True
        recur(index+1,num+str(i),k)
        used[i] = False

recur(0,'',k)
ans.sort()
print(ans[-1])
print(ans[0])