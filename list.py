n=int(input("Enter the no. of elements:"))
list2 = []
for i in range(0, n):
    x=int(input())
    list2.append(x)
for num in list2:
    if(num<0):
        list2.remove(num)
print(list2)
