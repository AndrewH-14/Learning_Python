# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#
# It should tell them the interpretation of their BMI based on the BMI value.
#
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height ** 2))

if 18.5 > bmi:
    print("Your BMI is " + str(bmi) + ", you are underweight.")
else:
    if 25 > bmi:
        print("Your BMI is " + str(bmi) + ", you have a normal weight.")
    else:
        if 30 > bmi:
            print("Your BMI is " + str(bmi) + ", you are slightly overweight.")
        else:
            if 35 > bmi:
                print("Your BMI is " + str(bmi) + ", you are obese.")
            else:
                print("Your BMI is " + str(bmi) + ", you are clinically obese.")
