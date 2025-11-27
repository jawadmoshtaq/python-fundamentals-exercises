# DAY 1 - TASK 1

name = "Jawad"
age = 32
is_student = True

print(name)
print(age)
print(is_student)

# DAY 1 - TASK 2

country = "Italy"
population = 59000000
is_eu_member = True

sentence = f"{country} has a population of {population} people. EU member: {is_eu_member}"
print(sentence)

# DAY 1 - TASK 3

a = 10
b = 4

sum_result = a + b
difference = a - b
product = a * b
quotient = a / b

print(sum_result)
print(difference)
print(product)
print(quotient)

# DAY 2 - TASK 4

first_name = "Mohammad Jawad"
last_name = "Moshtaq"

full_name = first_name + " " + last_name
print(full_name)


# DAY 2 - TASK 5

product_price = 3.5
product_quantity = 4

total_cost = product_price * product_quantity
print(total_cost)


# DAY 2 - TASK 6

radius = 5
pi = 3.14

area = pi * (radius ** 2)
print(area)

# DAY 2 - TASK 7

birth_year = 1992
current_year = 2025

age_calculated = current_year - birth_year
print(age_calculated)


# DAY 2 - TASK 8

celsius = 25
fahrenheit = celsius * 9/5 + 32
print(fahrenheit)

# DAY 2 - TASK 9

kilometers = 3.5
meters = kilometers * 1000
print(meters)


# DAY 2 - TASK 10

monthly_salary = 900
yearly_salary = monthly_salary * 12
print(yearly_salary)


# DAY 3 - TASK 11

def square(number):
    return number * number

print(square(5))


# DAY 3 - TASK 12

def print_name_age(name, age):
    print(f"My name is {name} and I am {age} years old.")

print_name_age("Mohammad Jawad", 33)


# DAY 3 - TASK 13

def multiply(x, y):
    return x * y

print(multiply(3, 7))


# DAY 3 - TASK 14

def is_even(number):
    return number % 2 == 0

print(is_even(10))
print(is_even(7))


# DAY 3 - TASK 15

def largest_of_three(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

print(largest_of_three(3, 10, 7))


# DAY 3 - TASK 16

text = " Python programming is awesome! "

stripped = text.strip()
length = len(stripped)
uppercased = stripped.upper()
replaced = stripped.replace("awesome", "powerful")

print(stripped)
print(length)
print(uppercased)
print(replaced)


# DAY 3 - TASK 17

email = "jawadmoshtaq@gmail.com"

at_index = email.find("@")
username = email[:at_index]
domain = email[at_index + 1:]

print(username)
print(domain)
print(f"User '{username}' is using the domain '{domain}'.")


# DAY 4 - TASK 18

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)


# DAY 4 - TASK 19

counter = 0

counter = counter + 1
counter = counter + 1
counter = counter + 1

counter = counter - 1
counter = counter - 1

print(counter)


# DAY 4 - TASK 20

def greet_user(name):
    return f"Hello, {name}! Welcome to the program."

def calculate_bmi(weight, height):
    return weight / (height ** 2)

user_name = "Jawad"
greeting = greet_user(user_name)
print(greeting)

weight = 70
height = 1.87

bmi = calculate_bmi(weight, height)
bmi_text = f"Your BMI is {bmi:.2f}"
print(bmi_text)

upper_text = bmi_text.upper()
print(upper_text)

