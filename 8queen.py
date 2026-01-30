import math

def conflict(a):
    for i in range(1,len(a)):
        for j in range(i):
            if a[i]==a[j] or math.fabs(a[i]-a[j])==math.fabs(i-j):
                return True
    return False

location=[0]*8
index=1
while index<8:
    while location[index]<8:
        if conflict(location[:index+1]):
            location[index]+=1
        else:
            index+=1
            break
    if index==8:
        break
    if location[index]==8:
        location[index]=0
        index-=1
        location[index]+=1
for i in location:
    print(i+1,end=' ')
