# Data Types
# 1. Find the data type of every value in a mixed list
def find_types(lst):
    for i in lst:
        print(i, ":", type(i))

my_list = [10, 3.14, "Hello", True, 5+2j]

find_types(my_list)


# 2. Convert a nested list into a tuple of tuples
def convert_tuple(lst):
    result = tuple(tuple(i) for i in lst)
    return result

my_list = [[1, 2], [3, 4], [5, 6]]

print(convert_tuple(my_list))


# 3. Remove duplicate values while preserving original order
def remove_duplicates(lst):
    result = []

    for i in lst:
        if i not in result:
            result.append(i)

    return result

my_list = [1, 2, 3, 2, 4, 1, 5]

print(remove_duplicates(my_list))


# 2.Operators
# 4. Check whether a number is a power of 2
def power_of_two(n):
    if n > 0 and (n & (n - 1)) == 0:
        return "Power of 2"
    else:
        return "Not a power of 2"

print(power_of_two(16))
print(power_of_two(10))



# 5. Swap two numbers using bitwise XOR
a = 10
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print("a =", a)
print("b =", b)


# 6. Check divisibility by both 4 and 6
def check_number(n):
    if n % 4 == 0 and n % 6 == 0:
        return "Divisible by both"
    else:
        return "Not divisible by both"

print(check_number(24))

# 7. Calculate electricity bill using different unit rates
def electricity_bill(units):
    if units <= 100:
        bill = units * 2

    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3

    else:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5

    return bill

units = 250
print("Electricity Bill:", electricity_bill(units))


# 3. Conditional Statements
# 8. Check whether three sides can form a triangle
def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "Valid Triangle"
    else:
        return "Invalid Triangle"

print(check_triangle(3, 4, 5))


# 9. Determine the type of triangle
def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid Triangle"

    elif a == b == c:
        return "Equilateral"

    elif a == b or b == c or a == c:
        return "Isosceles"

    else:
        return "Scalene"

print(triangle_type(5, 5, 5))
print(triangle_type(5, 5, 3))
print(triangle_type(3, 4, 5))


# 10. Create a simple ATM menu
balance = 5000

def atm():
    global balance

    while True:
        print("\n1. Withdraw")
        print("2. Deposit")
        print("3. Balance")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = int(input("Enter amount: "))

            if amount > 0 and amount <= balance:
                balance -= amount
                print("Withdrawal successful")
            else:
                print("Invalid amount or insufficient balance")

        elif choice == 2:
            amount = int(input("Enter amount: "))

            if amount > 0:
                balance += amount
                print("Deposit successful")
            else:
                print("Invalid amount")

        elif choice == 3:
            print("Balance:", balance)

        elif choice == 4:
            print("Thank you!")
            break

        else:
            print("Invalid choice")

atm()

# 11. Calculate income tax based on tax slabs
    # Example tax slabs:
    # - Up to ₹2,50,000: 0%
    # - ₹2,50,001 to ₹5,00,000: 5%
    # - ₹5,00,001 to ₹10,00,000: 20%
    # - Above ₹10,00,000: 30%
def calculate_tax(income):
    if income <= 250000:
        tax = 0

    elif income <= 500000:
        tax = (income - 250000) * 0.05

    elif income <= 1000000:
        tax = (250000 * 0.05) + (income - 500000) * 0.20

    else:
        tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

    return tax

print("Tax:", calculate_tax(800000))


# 12. Menu-driven calculator using if-elif
def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Result:", a + b)

    elif choice == 2:
        print("Result:", a - b)

    elif choice == 3:
        print("Result:", a * b)

    elif choice == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid choice")

calculator()


# 4. Loops
# 13. Print all prime numbers between 1 and n
def prime_numbers(n):
    for num in range(2, n + 1):
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print(num, end=" ")

prime_numbers(20)


# 14. Find factorial using a loop
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

print(factorial(5))


# 15. Print Fibonacci series up to n terms
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)


# 16. Check whether a number is an Armstrong number
def armstrong(n):
    temp = n
    digits = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == n:
        return "Armstrong Number"
    else:
        return "Not Armstrong Number"

print(armstrong(153))


# 17. Reverse a number and check palindrome
def reverse_number(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    print("Reverse:", reverse)

    if original == reverse:
        print("Palindrome Number")
    else:
        print("Not Palindrome")

reverse_number(121)


# 18. Find GCD of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return abs(a)

print(gcd(12, 18))


# 5. Functions
# 19. Check whether a string is a palindrome
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

print(is_palindrome("madam"))
print(is_palindrome("hello"))


# 20. Count vowels and consonants in a string
def count_vowels_consonants(s):
    vowels = 0
    consonants = 0

    for ch in s.lower():
        if ch in "aeiou":
            vowels += 1

        elif ch.isalpha():
            consonants += 1

    return vowels, consonants

v, c = count_vowels_consonants("Hello World")

print("Vowels:", v)
print("Consonants:", c)


# 21. Calculate simple and compound interest
def interest(p, r, t):
    si = (p * r * t) / 100

    ci = p * (1 + r / 100) ** t - p

    return si, ci

simple, compound = interest(10000, 5, 2)

print("Simple Interest:", simple)
print("Compound Interest:", compound)


# 22. Return all factors of a number
def factors(n):
    result = []

    for i in range(1, abs(n) + 1):
        if n % i == 0:
            result.append(i)

    return result

print(factors(12))


# 23. Find the second-largest number in a list
def second_largest(lst):
    first = float('-inf')
    second = float('-inf')

    for n in lst:
        if n > first:
            second = first
            first = n

        elif first > n > second:
            second = n

    if second == float('-inf'):
        return None

    return second

print(second_largest([10, 20, 30, 40, 50]))


# 6. Lists
# 24. Merge two lists without duplicates
def merge_lists(a, b):
    result = []

    for i in a + b:
        if i not in result:
            result.append(i)

    return result

list1 = [1, 2, 3]
list2 = [3, 4, 5]

print(merge_lists(list1, list2))


# 25. Find second-largest and second-smallest elements
def find_values(lst):
    unique = []

    for n in lst:
        if n not in unique:
            unique.append(n)

    if len(unique) < 2:
        return None, None

    smallest = float('inf')
    second_smallest = float('inf')

    largest = float('-inf')
    second_largest = float('-inf')

    for n in unique:
        if n < smallest:
            second_smallest = smallest
            smallest = n
        elif n < second_smallest:
            second_smallest = n

        if n > largest:
            second_largest = largest
            largest = n
        elif n > second_largest:
            second_largest = n

    return second_largest, second_smallest

lst = [10, 20, 30, 40, 50]

a, b = find_values(lst)

print("Second Largest:", a)
print("Second Smallest:", b)


# 28. Find common elements between two lists
def common_elements(a, b):
    result = []

    for i in a:
        if i in b and i not in result:
            result.append(i)

    return result

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print(common_elements(list1, list2))


# 7. Tuples & Sets
# 29. Count frequency of each element in a tuple
def frequency(t):
    result = {}

    for i in t:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    return result

t = (1, 2, 2, 3, 3, 3, 4)

print(frequency(t))


# 30. Find union, intersection and difference of two sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)


# 31. Check whether one set is a subset of another
def check_subset(a, b):
    if a.issubset(b):
        return "Subset"
    else:
        return "Not a subset"

set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(check_subset(set1, set2))


# 8. Dictionaries
# 32. Count frequency of words in a sentence
def word_frequency(sentence):
    words = sentence.lower().split()
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result

print(word_frequency("python is easy python is powerful"))


# 33. Create a dictionary from two lists
def create_dict(keys, values):
    result = {}

    for i in range(len(keys)):
        result[keys[i]] = values[i]

    return result

keys = ["name", "age", "city"]
values = ["Rahul", 21, "Pune"]

print(create_dict(keys, values))


# 34. Sort a dictionary by its values
def sort_dictionary(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

data = {
    "Apple": 50,
    "Banana": 20,
    "Mango": 40
}

print(sort_dictionary(data))



# 9. File Handling
# 35. Count lines, words and characters in a text file
# First, create a file named data.txt and write some text inside it.
def count_file():
    with open("data.txt", "r") as file:
        data = file.read()

    lines = data.splitlines()
    words = data.split()
    characters = len(data)

    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", characters)

count_file()


# 36. Copy only even-numbered lines into another file
def copy_even_lines():
    with open("data.txt", "r") as file:
        lines = file.readlines()

    with open("output.txt", "w") as file:
        for i in range(len(lines)):
            if (i + 1) % 2 == 0:
                file.write(lines[i])

    print("Even lines copied successfully")

copy_even_lines()




# 10. Exception Handling
# 37. Handle invalid integer input using try-except
def get_integer():
    try:
        n = int(input("Enter a number: "))
        print("Number:", n)

    except ValueError:
        print("Invalid input! Please enter an integer.")

get_integer()


# 38. Handle file-not-found errors
def read_file():
    try:
        with open("data.txt", "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("File not found!")

read_file()


# 11. Modules
# 39. Random password generator using random and string modules
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

print(generate_password(10))


# 40. Calculate days between two dates using datetime
from datetime import datetime

def calculate_days(date1, date2):
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")

    difference = abs((d2 - d1).days)

    return difference

print(calculate_days("2025-01-01", "2025-01-10"))



