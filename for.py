import pygame
list=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 
      37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
      79, 83, 89, 97]


#for x in range(b):
#    list[x]=list[x]+1
#   print(list[x])
a=int(input("Ener a number: "))

for i in range(2,a):
    if (a%i)==0:
        print("{} is not a prime number.".format(a))
        break
    else:
        print("{} is a prime number.".format(a))
        break