###Data types
print(len("Hello"))

print("Hello"[0])
print("123"+"345")
print(123+345)
print(123_345_678)


num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + "character.")
a = float(123)
print(type(a))

print(70+float("100.5"))
print(str(70) + str(100))
print(6+9)
two_digit_number= input("Type a two digit number")
print(type(two_digit_number))
print("hello"[0])
two_digit_number= input("Type a two digit number")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
print(first_digit)
print(second_digit)
result=int(first_digit) +int (second_digit)
print(result)
print(3*(3+3)/3-3)
##How to calculate BMI

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi= int (weight)/ float(height)**2
print(bmi)
bmi_as_int= int(bmi)
print(bmi_as_int)
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
weight_as_int = int(weight)
height_as_float= float(height)
bmi=weight_as_int/(height_as_float)**2
bmi_as_integer=int(bmi)
print(bmi_as_integer)


print(int (8/3))
print(round(8/3,2))
print(type(4//2))
result /=2
print(result)
score=0
score+=1
print(score)
score=0
height=1.8
isWinning = True
print("your score is"+str(score))
print(f"your score is{score}, your height is {height} ,you are winning is {isWinning}")

age=input("What is your current age?")
age_as_int=int(age)
years_remaining=90-age_as_int
days_remaining=years_remaining*365
weeks_remaining=years_remaining*52
months_remaining=years_remaining*12
print(months_remaining)
print(years_remaining)
print(weeks_remaining)
print(f"you have {days_remaining} days,{weeks_remaining} weeks,and {months_remaining} months left.")
print("Welcome to the tip calculator!")
bill= float(input("What was the total bill? $"))
print(type(bill))
tip=int(input("How much tip would you like to give 10, 12 ,or 15?"))
people=int(input("How many people to split the bill?"))
bill_with_tip=bill*(1+tip/100)
print(bill_with_tip)
tip_as_percent=tip/100
total_tip_amount= bill* tip_as_percent
total_bill = bill+total_tip_amount
bill_per_person= total_bill /people
final_amount=round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")
print("Each person should pay $ " + str(final_amount))
print("Welcome to the tip calculator")
bill=float(input("What was the total bill ? $ "))
print(type(bill))

print("Hello"+"Angela")
print(2*3)
bill=7%2
print(bill)
Height=int(input("Height in centimeters ?"))
bill=("if height > 120 :")
print(bill)
bmi = 28
if bmi < 18.5:
   print(f"Your bmi is {bmi} , you are underweight.")
elif bmi < 25:
  print(f"Your bmf is {bmi} ,you have a normal weight .")
elif bmi < 30:
  print(f"Your bmf is {bmi} ,you are overweight .")
elif bmi < 35:
   print(f"Your bmf is {bmi} ,you are obese .")
else:
  print(f"Your bmi is {bmi}, you are clinically obese.")
height=float(input("What is your height in m :"))
weight=float(input("What is your weight in kg :"))
print(bmi)
if bmi < 18.5:
    print(f"Your bmi is{bmi},you are underweight.")
elif bmi < 25:
       print(f"Your bmi is{bmi},you are normal.")
year=int(input ("Write a year ?"))
print(type(year))
leap_year= year /4
print(leap_year)
goal=year/100
print(goal)
till=year/400
print(till)

year=int(input("Write a year"))
if year%4==0:
    print("The year(year), is a leap year")
elif year%100!=0:
    print("The year (year),is not a leap year")

