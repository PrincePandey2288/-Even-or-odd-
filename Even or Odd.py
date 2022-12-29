d=str(input())
l=list(map(int,d.split(',')))
m=1
for i in l:
    m*=i
print(m)
if m%2==0:
    print("even")
else:
    print("odd")