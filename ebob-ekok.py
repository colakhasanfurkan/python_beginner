a=int(input("Enter a number: "))
list=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 
      37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
      79, 83, 89, 97]
if a in list:
    print("{} is a prime number.".format(a))