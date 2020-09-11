n=int(input("Enter the no. of elements:"))
list1 = []
for i in range(0, n):
    x=int(input())
    list1.append(x)
for num in list1:
    if(num>0):
        print(num,end=' ')
