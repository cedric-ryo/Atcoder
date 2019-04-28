a,b = map(int,input().split())
#print(a+b) if a == b else print(b+b-1)
if a == b:
    print(a+b)
elif a > b:
    print(a+a-1)
else:
    print(b+b-1)
