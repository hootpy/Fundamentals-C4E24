from random import randint
items = ["hexagon","friend","hanoi","technology","english","global","excel","computer"]
j = randint(0,len(items)-1)
word = items[j]
characters = list(word)
word1 = []
while len(characters)>0:
        i = randint(0,len(characters)-1)
        n_ran = characters[i]
        word1.append(n_ran)
        characters.remove(n_ran)
while True:
    print(*word1)
    n = input("Your answer is: ")
    if n == word:
        print("Bingo!")
        break
    else:
        print("Try again!")