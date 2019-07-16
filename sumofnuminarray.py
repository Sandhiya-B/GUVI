first,second = input().split( )
first=int(first)
second=int(second)
n=list(input().split())
n=[int(x) for x in n]
sum = 0
for i in range(0,second):
    sum = sum+n[i]
print(sum)
