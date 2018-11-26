height=int(input("Your height (cm): "))
weight=int(input("Your weight (kg): "))

bmi= weight/((height/100)**2)
print("Your BMI is:", bmi)

if bmi<16:
    print("You are severely underweight!")
elif 16 <= bmi and bmi < 18.5:
    print("You ar underweight!")
elif 18.5 <= bmi and bmi < 25:
    print("You are normal!")
elif 25 <= bmi and bmi < 30:
    print("You are overweight!")
else:
    print("You are obese!")