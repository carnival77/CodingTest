n = int(input())

m = int(input())

broken=[False] * 10

broken_numbers = list(map(int,input().split()))

for i in broken_numbers:
    broken[i] = True

ans=abs(n-100)

def nums_possible(c):
    if c==0:
        if broken[c]==True:
            return 0
        else:
            return 1
    cnt=0
    while c>0:
        if broken[int(c%10)] == True:
            return 0
        else:
            c//=10
            cnt+=1
    return cnt

for i in range(1000001):
    c=i
    pmpress=0
    nums_cnt = nums_possible(c)
    if nums_cnt > 0:
        pmpress = abs(n-c)
        if ans > (nums_cnt + pmpress):
            ans = nums_cnt + pmpress

print(ans)

# n = int(input())
# m = int(input())
# broken = [False] * 10
# if m > 0:
#     a = list(map(int,input().split()))
# else:
#     a = []
# for x in a:
#     broken[x] = True
# def possible(c):
#     if c == 0:
#         if broken[0]:
#             return 0
#         else:
#             return 1
#     l = 0
#     while c > 0:
#         if broken[c%10]:
#             return 0
#         l += 1
#         c //= 10
#     return l
# ans = abs(n-100)
# for i in range(0, 1000000+1):
#     c = i
#     l = possible(c)
#     if l > 0:
#         press = abs(c-n)
#         if ans > l + press:
#             ans = l + press
# print(ans)