from cgitb import small


print("\nEnter numbers for find to biggest or smallest number.")
print("For stop entering number type 0.\n")
list=[]
i=0
a=1
while a!=0:
    a=int(input("Enter number {} : ".format(i+1)))
    if a!=0:
        list.append(a)
        i+=1

n=len(list)

b=list[0]
for k in range(n-1):
     for j in range(n-k-1):
         if list[j]>list[j+1]:
             temp=list[j]
             list[j]=list[j+1]
             list[j+1]=temp

print(list[n-1])

print("Choose option:")
print("1. Find biggest number.")
print("2. Find smallest number.")
x=int(input())
if x==1:
    print(list[n-1])
elif x==2:
    print(list[0])
             
