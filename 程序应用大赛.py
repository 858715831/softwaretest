def Win(list,name):
    list.sort(key=lambda x:(-x[1],-x[2]),reverse=True)
    index=-1
    for i in range(len(list)):
        if name==list[i][0]:
            index=i
    if index < len(list)*0.6:
        print("YES")
    else:
        print("NO")


n= int(input())
for _ in range(n):
    m,name=input().split(" ")
    m=int(m)
    list=[]
    for _ in range(m):
        name1,num1,score1=input().split(" ")
        list.append((name1,int(num1),int(score1)))

    Win(list,name)
