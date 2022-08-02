import random
numbers = ["A","K","Q","J",2,3,4,5,6,7,8,9,10]

deck = [["Hearts"],["Diamonds"],["Clubs"],["Spades"]]
for i in range(4):
    for j in range(13):
        deck[i].append(numbers[j])
input("Press enter to pick a card.")       
shape = random.randint(0,3)
number = random.randint(1,14)
print(deck[shape][number],deck[shape][0])