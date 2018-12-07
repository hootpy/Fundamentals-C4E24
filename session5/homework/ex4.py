
question = [
    "If x = 8, then what is the value of 4(x+3)",
    "If x = 8, then what is the value of 4(x+3)",
    "If x = 8, then what is the value of 4(x+3)",
    "If x = 8, then what is the value of 4(x+3)",
    "If x = 8, then what is the value of 4(x+3)"
]


choice = [
    {
        "1":35,
        "2":36,
        "3":40,
        "4":44
    },
    {
        "1":35,
        "2":36,
        "3":40,
        "4":44
    },
    {
        "1":35,
        "2":36,
        "3":40,
        "4":44
    },
    {
        "1":35,
        "2":36,
        "3":40,
        "4":44
    },
    {
        "1":35,
        "2":36,
        "3":40,
        "4":44
    }
]

answer = [
    "4",
    "4",
    "4",
    "4",
    "4"
]
######################################################

print('Hello to quiz')
print('Answer the following question:')
correct_ans = 0
for i in range(len(question)):
    print(question[i])
    for k,v in choice[i].items():
        print(k,v,sep=": ")

    ans = input("Your answer is: ")

    if ans == answer[i]:
        print("Correct!")
        correct_ans += 1
    else:
        print("Incorrect!")
    print("**************************************************")

print(f"You answer correctly {correct_ans} out of {len(question)} questions!")