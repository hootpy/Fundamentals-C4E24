from random import randint

print("Welcome to hangman!")
print("This is the name of a city!")

#chon ngau nhien mot tu khoa
databs = ["hanoi","saigon","london","newyork","madrid","tokyo","sydney"]
pos_key = randint(0,len(databs)-1)
key_word= databs[pos_key]

#hinh hang man va tu khoa bi an ben duoi
hangman = ["  |","  0","  |"," /"]
character = list(key_word)
underline = []
for undercha in range(len(character)):
    underline.append("_")

#so lan sai toi da la 5 va so lan dung toi da la do dai str
false_times = 0
true_times = 0



while false_times < 5 and true_times < len(character):
    print("---")

    #dua vao so lan sai se in ra hang man nhu nao
    for i in range(false_times):
        print(hangman[i])
    print()
    for j in underline:
        print(j,end=" ")
    print()

    #phan tich ket qua nguoi dung nhap
    answ = input("Your guess?: ")

    #neu dung thi thay doi ki tu cua dong underline
    if answ in character:
        for m in range(len(character)):
            if character[m-1] == answ:
                underline[m-1] = answ
                true_times += 1
    
    #neu sai thi tang so lan false time
    else:
        false_times += 1
        print("Be careful!")
    print("**********************************")

#khi vong lap bi break
    #neu dung
if true_times == len(character):
    print("Bingo!")
else:
    #neu sai
    hangman[3] = " / \ "
    print("---")
    for i in hangman:
        print(i)
    print()
    print("You lose!")

