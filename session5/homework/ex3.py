#Implement quiz program

question = [
    "If x = 8, then what is the value of 4(x+3)"
]


choice = [
    {
        "1":35,
        "2":36,
        "3":40,
        "4":44
    }
]

answer = [
    "4"
]


print('Hello to quiz')
print('Answer the following question:')

print(question[0])
for k,v in choice[0].items():
    print(k,v,sep=":")

ans = input("Your answer is: ")

if ans == answer[0]:
    print("Correct!")
else:
    print("Incorrect!")
