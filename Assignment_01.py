
# Q1. Check if a number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


  
# Q2. Check whether a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")



# Q3. Find the greater of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater")
elif b > a:
    print("Second number is greater")
else:
    print("Both numbers are equal")



# Q4. Find the greatest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest number:", a)
elif b >= a and b >= c:
    print("Greatest number:", b)
else:
    print("Greatest number:", c)



# Q5. Check if a person is eligible to vote.

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")



# Q6. Check whether a year is a leap year.

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")



# Q7. Check if a character is a vowel or consonant.

ch = input("Enter a character: ").lower()

if ch in "aeiou" and len(ch) == 1:
    print("Vowel")
elif ch.isalpha() and len(ch) == 1:
    print("Consonant")
else:
    print("Please enter a single alphabet")



# Q8. Check whether a number is divisible by 5 and 11.

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")



# Q9. Check if a number is a multiple of both 3 and 7.

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("Multiple of both 3 and 7")
else:
    print("Not a multiple of both 3 and 7")



# Q10. Assign grades based on marks.

marks = int(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")



# Q11. Check if a character is uppercase or lowercase.

ch = input("Enter a character: ")

if len(ch) == 1 and ch.isupper():
    print("Uppercase character")
elif len(ch) == 1 and ch.islower():
    print("Lowercase character")
else:
    print("Not an uppercase or lowercase alphabet")



# Q12. Check whether an alphabet is a vowel using if-elif.

ch = input("Enter an alphabet: ").lower()

if ch == 'a':
    print("Vowel")
elif ch == 'e':
    print("Vowel")
elif ch == 'i':
    print("Vowel")
elif ch == 'o':
    print("Vowel")
elif ch == 'u':
    print("Vowel")
elif len(ch) == 1 and ch.isalpha():
    print("Consonant")
else:
    print("Invalid input")



# Q13. Check if three sides can form a triangle.

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")


# Q14. Determine whether a triangle is Equilateral, Isosceles, or Scalene.

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid sides")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Triangle cannot be formed")
elif a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")



# Q15. Find the largest among four numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("Largest:", a)
elif b >= a and b >= c and b >= d:
    print("Largest:", b)
elif c >= a and c >= b and c >= d:
    print("Largest:", c)
else:
    print("Largest:", d)




# Q16. Check whether a number is a three-digit number.

num = int(input("Enter a number: "))

if 100 <= abs(num) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")



# Q17. Calculate an electricity bill using slab rates.

units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 5
    print("Electricity bill: Rs.", bill)
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
    print("Electricity bill: Rs.", bill)
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
    print("Electricity bill: Rs.", bill)



# Q18. Calculate income tax based on sample income slabs.

income = float(input("Enter annual income: "))

if income < 0:
    print("Invalid income")
elif income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = 12500 + (income - 500000) * 0.20
else:
    tax = 112500 + (income - 1000000) * 0.30

if income >= 0:
    print("Income tax: Rs.", tax)


  
# Q19. Check if a student passes in every subject.

s1 = int(input("Enter marks in subject 1: "))
s2 = int(input("Enter marks in subject 2: "))
s3 = int(input("Enter marks in subject 3: "))

if s1 >= 35 and s2 >= 35 and s3 >= 35:
    print("Student passed")
else:
    print("Student failed")  



# Q20. Check whether a number is within the range 10 to 50.

num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
    print("Number is within the range")
else:
    print("Number is outside the range")




# Q21. Create a simple calculator.

a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


    
# Q22. Check whether a year is a century leap year.

year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Century leap year")
elif year % 100 == 0:
    print("Century year but not a leap year")
else:
    print("Not a century year")




# Q23. Determine season using match-case.

month = int(input("Enter month number (1-12): "))

match month:
    case 3 | 4 | 5:
        print("Summer")
    case 6 | 7 | 8 | 9:
        print("Monsoon")
    case 10 | 11:
        print("Post-monsoon / Autumn")
    case 12 | 1 | 2:
        print("Winter")
    case _:
        print("Invalid month")



    
# Q24. Find the number of days in a month.

month = int(input("Enter month number (1-12): "))
year = int(input("Enter year: "))

if month < 1 or month > 12 or year < 1:
    print("Invalid month or year")
elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("29 days")
    else:
        print("28 days")
elif month in (4, 6, 9, 11):
    print("30 days")
else:
    print("31 days")



  
# Q25. Check password length and digit condition.

password = input("Enter a password: ")

if len(password) >= 8 and any(ch.isdigit() for ch in password):
    print("Password meets the conditions")
else:
    print("Password must have at least 8 characters and one digit")


  
# Q26. Determine ticket price based on age.

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 12:
    print("Ticket price: Rs. 100")
elif age < 60:
    print("Ticket price: Rs. 200")
else:
    print("Ticket price: Rs. 150")



# Q27. Calculate discount based on purchase amount.

amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid amount")
elif amount >= 5000:
    discount = amount * 0.20
    print("Discount: Rs.", discount)
    print("Final amount: Rs.", amount - discount)
elif amount >= 2000:
    discount = amount * 0.10
    print("Discount: Rs.", discount)
    print("Final amount: Rs.", amount - discount)
else:
    print("No discount")
    print("Final amount: Rs.", amount)



# Q28. Check driving license eligibility.

age = int(input("Enter your age: "))
eyesight = input("Have you passed the eyesight test? (yes/no): ").lower()

if age >= 18 and eyesight == "yes":
    print("Eligible to apply")
else:
    print("Not eligible based on these conditions")



# Q29. Create a simple login system.

new_username = "admin"
new_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == new_username and password == new_password:
    print("Login successful")
else:
    print("Invalid username or password")



# Q30. Menu-driven calculator using match-case.

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a + b)

    case 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a - b)

    case 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a * b)

    case 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")

    case 5:
        print("Exiting program")

    case _:
        print("Invalid choice")