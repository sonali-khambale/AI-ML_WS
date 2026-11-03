# 1. Even or Odd Function
def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(10))
print(is_even(7))

# 2. Largest of Two Numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(10, 20))


# 3. Print Numbers (1 to n)
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)


# 4. Sum of Numbers (1 to n)
def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

print(sum_n(5))


# 5. Multiplication Table
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

table(5)


# 6. Count Even Numbers in a List
def count_even(numbers):
    count = 0

    for i in numbers:
        if i % 2 == 0:
            count += 1

    return count

print(count_even([1, 2, 3, 4, 6]))


# 7. FizzBuzz (1 to 100)
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()


# 8. Palindrome Checker
def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

print(palindrome("madam"))
print(palindrome("hello"))


# 9. Count Vowels
def count_vowels(s):
    count = 0

    for ch in s:
        if ch.lower() in "aeiou":
            count += 1

    return count

print(count_vowels("Hello World"))


# 10. Second Largest Number (Without sort())
def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')

    for n in numbers:
        if n > largest:
            second = largest
            largest = n
        elif largest > n > second:
            second = n

    if second == float('-inf'):
        return None

    return second

print(second_largest([10, 20, 5, 30, 25]))


# 11. Guessing Game
import random

def guessing_game():
    number = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == number:
            print("Correct! You won.")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

guessing_game()


# 12. Grade Calculator
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

print(grade(95))
print(grade(85))
print(grade(75))
print(grade(65))
print(grade(40))