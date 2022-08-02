from random import randint
x = randint(1,10)
guess = int(input("Guess the number: "))

while guess != x:
    if guess < x:
        guess = int(input("Try something biger: "))
    if guess > x:
        guess = int(input("Try something smaller: "))
print("Correct!")
