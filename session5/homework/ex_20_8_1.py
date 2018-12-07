userinput = input("Enter your string: ").lower()
rmv_spa = userinput.replace(" ","")
char = list(rmv_spa)
char.sort()
string_count={}
for i in char:
    if i.isalpha():
        if i in string_count:
            string_count[i] +=1
        else:
            string_count[i] = 1

for k,v in string_count.items():
    print(k,v,sep=": ")