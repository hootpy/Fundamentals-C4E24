bingo = 66

while True:
    m = input("Guess my number (0-100): ")
    if m.isdigit():
        n = int(m)
        if 0 <= n and n < 50:
            print("Too small!")
        elif 50 <= n and n < 66:
            print("A little bit small!")
        elif n > 66 and n < 80:
            print("A little bit large!")
        elif 80 <= n and n <= 100:
            print("Too large!")
        elif n > 100:
            print("Please enter a valid number!")
        else:
            print("Bingo!")
            break
    else:
        print("Please enter a valid number!")