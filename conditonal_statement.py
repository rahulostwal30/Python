"""
Conditional statement ==> it is a statement that execute a specific block of code 
                          based on condition is True or False

                          if
                          elif
                          else
 """
# a = 50
# if(a<200):
#     print("condition shi hai")
# else:
#     print("condition galat hai")




" --------------------------------------  PRACTICE QUESTION  -----------------------------------"
" Question 1. check weather as integer is even or odd "
# n = 4
# if n%2==0:
#     print(f"number is even ")
# else:
#     print("number is odd ")


"Question 2. Check number is a negative, positive and zero "
# n = 10
# n = -5
# n = 0
# if n>0:
#     print(f"number is a positive")
# elif n==0:
#     print("number is a zero ")
# else:
#     print("number is a negative")



"Question 3. largest of two numbers "
# x = 8
# y = 8
# if x>y:
#     print("x is a largest")
# elif y>x:
#     print("y is a largest")
# else:
#     print("both are equal ")



" Question 4. Largest of three number "
# a = 5 ; b = 8 ; c = 2
# if c<a>b:
#     print(f"{a} is largest number")
# elif a<b>c:
#     print(f"{b} is a largest number")
# elif a<c>b:
#     print(f"{c} is a largest number")
# else:
#     print("both are equal number")



"Question 5. check weather is year is a Leap year"
# year = 2024

# if(year%400==0 or (year%100!=0 and year%4==0)):
#     print("leap year")
# else:
#     print("not a leap year")


"Question 6. voting eligibility "
# age = 19
# if age>=18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")


"Question 7. Calculating the grede "
# marks = 45
# if 90<=marks<=100:
#     print("Grade A")
# elif marks>=75:
#     print("Grade B")
# elif marks>=60:
#     print("Grade C")
# else:
#     print("Fail")


"Question 8. Number is divisible by both 3 and 5"
# n = 15
# if (n%3 and n%5)==0:
#     print("Divisible by both 3 and 5")
# else:
#     print("Not divisible by both")


"Question 9. calculater "
# print("""
# Addition = +
# Substraction = -
# Multiplication = *
# Divide = /
# """)
# mode = input("enter mode :  ")
# a = 10
# b = 5
# if(mode=='+'):
#     print("Addition : ",a+b)
# elif mode=='-':
#     print("Substraction : ",a-b)
# elif mode=='*':
#     print("Multiplication : ",a*b)
# elif mode=='/':
#     print("divide : ",a/b)
# else:
#     print("invalid operator")


"Question 10. identify if character is alphabet digit and special symble "
# cha = 'a'
# if 'a'<=cha<='z' or 'A'<=cha<='Z':
#     print("character is alphabet")
# elif 1<=cha<=9:
#     print("character is digit")
# else:
#     print("specital symble")



"Question 11. check temperature "
# temp = 31
# if temp>30:
#     print("Temperature is hot")
# else:
#     print("temperature is cold")


"Question 12. pass and Fail"
# marks = 45
# if marks>=40:
#     print("you passed")
# else:
#     print("you Failed")



"Question 13. check number equality"
# a = 8
# b = 10
# if a==b:
#     print(" both are equal")
# else:
#     print("both are not equal ")


"Question 14. check number is a multiple by 7"
# n = 22
# if n%7==0:
#     print("number is divisible by 7")
# else:
#     print("not divisible by 7")



"Question 15. check number by sign and parity"
# num = 6
# if num>0:
#     if num%2==0:
#         print("Positive even")
#     else:
#         print("positive odd")
# elif num<0:
#     if num%2==0:
#         print("negative even")
#     else:
#         print("negative odd")
# else:
#     print("Zero")



"Question 16. Allow calculation only if principal is positive"
# principal = 100
# if principal>0:
#     print("This number is eligible for calculation")
# else:
#     print("This number is not eligible for calculation ")



"Question 17. Classify age group"
# age = 15
# if age>=60:
#     print("He is senior")
# elif age>=20:
#     print("He is Adult")
# elif age>=13:
#     print("He is Teen")
# else:
#     print("He is child")



"Question 18. Password length check"
# pw = 'rahul12'
# if len(pw)>=8:
#     print("your password is valid")
# else:
#     print("your password is invalid")



"Question 19. classify day as weekend or weekday"
# day = 'Monday'
# if 'saturday'==day=='sunday':
#     print("This is a weekend")
# else:
#     print("This is a weekday")



" Question 20. compute BMI and classify health category"
# weight = 85
# height = 1.6
# bmi = weight/(height**2)

# if bmi>=30:
#     print("Obese")
# elif bmi>=25:
#     print("Overweight")
# elif bmi>=18.5:
#     print("Normal")
# else:
#     print("Underweight") 


" Question 21. Electricity bill calculator "
# unit = 250
# if unit<=100:
#     bill = unit*5
# elif unit<=200:
#     bill = (100*5)+ ((unit-100)*8)
# else:
#     bill = (100*5)+(100*8)+((unit-200)*10)

# print(f"Total bill amount {bill}")


" Question 22. login system"
# stored_username = 'admin'
# stored_password = 1234
# username = 'admin'
# password = 1234

# if username==stored_username and password==stored_password:
#     print("Login successful")
# else:
#     print("invalid credentials")


" Question 23.  Discount system apply discount based on purchase amount"
# amount = 1500
# if amount>5000:
#     amount = amount - amount*20//100
# elif amount>2000:
#     amount = amount - amount*10//100
# else:
#     print("No discount")

# print("final payable amount : ",amount)


" Question 24. Triangle validator => check if three sides can from a triangle"
# a = 1 ; b = 2 ; c = 3
# if a+b>c and b+c>a and a+c>b:
#     print("valid triangle ")
# else:
#     print("invalid triangle")


" Question 25. Triangle type checker "
# a = 3; b = 4; c = 5
# if a==b==c:
#     print("Equilateral")
# elif a==b or b==c or a==c:
#     print("Isosceles")
# else:
#     print("Scalene")


" Question 26. Time based greeting - print greeting based on hour(0-23)"
# time = 18
# if 5<=time<=11:
#     print("Good morning")
# elif 12<=time<=16:
#     print("Good Afternoon")
# elif 17<=time<=20:
#     print("Good Evening")
# else:
#     print("Good Night")



" Question 27. ATM withdrawal simulation "
# balance = 5000
# withdrow = 250
# if withdrow<=balance and withdrow%100==0:
#     print("Transaction successful ")
#     balance = balance-withdrow
# elif withdrow%100!=0:
#     print("invalid amount ")
# else:
#     print("Error")



" Question 28. Menu based calculater"
# Addition = 1
# substraction = 2
# Multiplication = 3
# Modulo = 4

# x = 4; y = 5; choice = 1

# if(choice in (1,2,3,4)):
#     if choice==1:
#         print(x+y)
#     elif choice==2:
#         print(x-y)
#     elif choice==3:
#         print(x*y)
#     else:
#         print(x%y)
# else:
#     print("invalid symbal")



" Question 29. Bank loan eligibility "
# salary = 50000; credit_score = 750
# if salary>=30000 and credit_score>=700:
#     print("Eligible for loan")
# else:
#     print("is not eligible for loan")



" Question 30. shipping cost calculator "
# weight = 2
# if weight<=2:
#     shipping_charge = 50
# elif weight<=5:
#     shipping_charge = 80
# else:
#     shipping_charge = 120
# print(shipping_charge)


" Question 31.  Income Tax calculator - apply simple tax slabs"
# amount = 15000
# if amount<=250000:
#     print("No tax")
# elif amount<=500000:
#     print("Tax as per slab 5% ")
# elif amount<=1000000:
#     print("Tax as per slab 20%")
# else:
#     print("tax as per slab 30%"

" Question 32. Movie Ticket pricing apply age based discounts"
# age = 15
# if age<12:
#     print("child discount")
# elif age<=60:
#     print("Regular price")
# else:
#     print("senior discount")


"Question 33. Parking calculator fees by parked hours"
# hour = 6
# if hour<=2:
#     fees = hour*20
# else:
#     fees = 40 + (hour-2)*30
# print(f"your parking fees => {fees}")


" Question 44. student scholarship eligibility "
# marks = 92 ; family_income = 200000
# if marks>=85 and family_income<=300000:
#     print("You are eligible for scholarship")
# else:
#     print("you are not eligible for scholarship")


" Question 35. online order validation "
# stock = 5 ; order = 3
# if order<=stock:
#     print("order confirmed") 
# else:
#     print("out of stock")


" Question 36. login attemps limit - lock account after too many failures"
# login = 2
# if login>=3:
#     print("your account is locked")
# else:
#     print("Try again")


" Question 37. delivery charge based on order value"
order_value = 300
if order_value>=500:
    print(f"your bill => {order_value}")
else:
    print(f"your order => {order_value}")
    print("charges => ",40)