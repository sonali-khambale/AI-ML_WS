# 1. Check whether a number is Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")



# 2. Find the Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


# 3. Check whether a Number is Prime
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")


# 4. Print Fibonacci Series up to N Terms
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b



# 5. Find Factorial of a Number Using a Loop
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial is:", fact)


# 6. Reverse a String Without Using [::-1]
text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string:", reverse)


# 7. Check whether a String is a Palindrome
text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")


# 8. Count Vowels and Consonants in a String
text = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in text.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)



# 9. Find the Sum of All Elements in a List
numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total += num

print("Sum of elements:", total)


# 10. Find Largest and Smallest Element Without max() or min()
numbers = [10, 25, 5, 40, 15]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


# 11. Remove Duplicate Elements from a List
numbers = [10, 20, 10, 30, 20, 40]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List without duplicates:", unique)


# 12. Count Frequency of Each Element Using Dictionary
numbers = [1, 2, 2, 3, 1, 2, 4]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency:", frequency)


# 13. Find the Second-Largest Number in a List
numbers = [10, 20, 40, 30, 50]

largest = numbers[0]
second = None

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num != largest:
        if second is None or num > second:
            second = num

print("Second largest:", second)


# 14. Sort a List Without Using sort() or sorted()
numbers = [5, 2, 8, 1, 9]

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)


# 15. Function to Return Only Even Numbers from a List
def even_numbers(numbers):
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)

    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print("Even numbers:", even_numbers(numbers))



# 16. Find Frequency of Each Character in a String

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character frequency:", frequency)


# 17. Check Whether Two Strings are Anagrams

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Anagrams")
else:
    print("Not Anagrams")


# 18. Find All Duplicate Values in a List
numbers = [10, 20, 30, 10, 40, 20, 50]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate values:", duplicates)


# 19. Find the Longest Word in a Sentence
sentence = input("Enter a sentence: ")

words = sentence.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)



# 20. Student Marks Program
    # Grade criteria: A = 90% and above, 
    # B = 75–89%, C = 60–74%, 
    # D = 40–59%, F = below 40%. 
    # Passing requires at least 35 marks in every subject.
marks = []

for i in range(5):
    mark = int(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

total = sum(marks)

percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if all(mark >= 35 for mark in marks):
    print("Result: PASS")
else:
    print("Result: FAIL")
