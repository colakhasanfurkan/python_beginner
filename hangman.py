import random
list = ["speed","alive","school","table","project","travel","construction","architect","alligator"]
word = random.choice(list)
print(word)
lives = 3
point = 0
x= len(word)
mask= "____________________"

while True:
    print(mask[0:x])
    guess = input("Enter a letter to guess the word: ")
    c = 0
    
    for i in range(x):
        if word[i] == guess:
            mask = mask[:i] + guess + mask[i+1:]
            c +=1
    
    if guess in word:
        point += c
        
        print("Right letter, guess another.")
    if point == x:
        print(f"You win, word is {word}.")
        break
    elif guess not in word:
        print("Wrong guess, try again.")
        lives -= 1
    if lives == 0:
        break
input()