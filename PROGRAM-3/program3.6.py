n=int(input("enter the value of n:"))
list=[]
for i in range(n):
    num=int(input("enter a num:"))
    list.append(num)
    print("even numbers are")
    print("[",end="")
    for num in list:
        if num%2==0:
            print(num,end=",")
            print("]")
            
