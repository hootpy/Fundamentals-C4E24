while True:
    pw = input("Enter your password")
    if len(pw) > 8: 
        if (not pw.isupper()) and (not pw.islower()) and (not pw.isdigit()):
            break

print("Thank you")