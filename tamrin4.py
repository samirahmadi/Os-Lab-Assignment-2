weight=float(input("Enter weight kg:"))
fheight=float(input("Enter height cm:"))
height=(fheight/100)**2
BMI=weight/height
print(BMI)
if BMI<18.5:
 print(" u are Underweight")
elif 18.5<=BMI<=24.9:
 print(" u are Normal")
elif 25<=BMI<=29.9:
 print(" u are Overweight")
elif 30<=BMI<=34.9:
 print(" u are Obese")
elif 35<=BMI:
 print(" u are Extremely Obese")