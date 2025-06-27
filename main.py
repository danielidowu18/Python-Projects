# Testing Print Function
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
input("print('what to print')")
print(len(input('what is your name?')))

# Band Name Generator
print("Welcome to the Band Name Generator!")
city = input("What city are you from?\n")
petName = input("What is the of your pet?\n")
print("Your band name can be " + city + " " + petName)

# Number digits addition
num = input("Please type a two digit number!")
print(int(num[0]) + int(num[1]))


# BMI Calculator
height = float(input("What is your height in m? "))
weight = float(input("What is your weight in kg? "))
h = float(height) * float(height)
b_m_i = int(weight) / h
print(int(b_m_i))

# Testing f strings
print(f"My height is {h}")

# Remaining days, weeks and years Calculator
age = input("what is your current age? ")
days = 365 * (90 - int(age))
weeks = 52 * (90 - int(age))
months = 12 * (90 - int(age))
print(f"You have {days} days, {weeks} weeks and {months} months left.")


# Tip Bill Calculator
print("Welcome to the tip calculator.")
totalBill = input("What was the total bill? $")
percentTip = input("What percentage tip would you like to give? 10, 12 or 15? ")
numOfppl = input("How many people to split the bill? ")
tipBill = int(totalBill) * (int(percentTip) / 100)
increasedBill = int(totalBill) + tipBill
individualPays = round(increasedBill / int(numOfppl), 2)
print(f"Each person should pay: ${individualPays}")


# Even Number Checker
number = int(input("Which number do you want to check? "))

if number % 2 == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")     


# BMI Calculator that tells you if you're underweight or overweight
height = float(input("What is your height in m? "))
weight = float(input("What is your weight in kg? "))
heightSq = height * height
body_m_i = weight / heightSq
rbody_m_i = round(body_m_i, 1)
print(f"Your BMI is {rbody_m_i}")
if rbody_m_i < 18.5:
    print("You are underweight.")
elif rbody_m_i < 25:
    print("You have a normal weight.")
elif rbody_m_i < 30:
    print("You are overweight.")
elif rbody_m_i <  35:
    print("You are Obese.")
else:
    print("You are clinically obese.")


# Leap Year checker
year = int(input("Which year do you want to check? "))
div4 = year % 4
div100 = year % 100
div400 = year % 400
if div4 == 0:
    if div100 == 0:
        if div400 == 0:
            print("Leap year!")
        else:
            print("Not leap year!")
    else:
        print("Leap year!")
else: 
    print("Not leap year!")   


# Python Pizza Deliveries
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
    elif extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${bill}.")
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 5
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.") 
        else:
            print(f"Your final bill is: ${bill}.")
    elif extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${bill}.")
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 5
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.") 
        else:
            print(f"Your final bill is: ${bill}.")    
    elif extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${bill}.")        
        

# Ticket Generator
age = int(input("What is your age?\n"))        
if age >= 45 and age <= 50: 
    print("You have a free ticket!.")  
else:
    print("You have to pay for your ticket.")         


# Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n") 
lowerName1 = name1.lower()
lowerName2 = name2.lower()
numOft = int(lowerName1.count("t")) + int(lowerName2.count("t"))
numOfr = int(lowerName1.count("r")) + int(lowerName2.count("r"))
numOfu = int(lowerName1.count("u")) + int(lowerName2.count("u"))
numOfe = int(lowerName1.count("e")) + int(lowerName2.count("e"))
numOfl = int(lowerName1.count("l")) + int(lowerName2.count("l"))
numOfo = int(lowerName1.count("o")) + int(lowerName2.count("o"))
numOfv = int(lowerName1.count("v")) + int(lowerName2.count("v"))
fdigit = str(numOft + numOfr + numOfu + numOfe)
sdigit = str(numOfl + numOfo + numOfv + numOfe)
loveScore = fdigit + sdigit
loveScoreNum = int(loveScore)
if loveScoreNum < 10 or loveScoreNum > 90:
    print(f"Your score is {loveScoreNum}, you go together like coke and mentos.")
elif loveScoreNum >= 40 and loveScoreNum <= 50:
    print(f"Your score is {loveScoreNum}, you are alright together.")
else:
    print(f"Your score is {loveScoreNum}.")                 
    
    
# Treasure Island Game 
print("Welcom to the Treasure Island.")
print("Your mission is to find the treasure.")
crossRoad = (input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")).lower()
if crossRoad == "left":
    water = (input("You come across a body of water. Do you want to 'wait' for a boat or 'swim' across\n")).lower()
    if water == "swim":
        door = (input("You get to a house that has three doors. Which of the doors do you want to enter? 'red', 'yellow' or 'blue'\n")).lower()
        if door == "red":
            print("Game Over, You entered a room burning with fire.")
        elif door == "yellow":
            print("Congratulations!!!, You entered a room filled with Gold.")
        elif door == "blue":
            print("Game Over, You entered a room full of American ninjas")    
        else:
            print("Game Over, There's no door with that colour")
    elif water == "wait":
        print("Game Over. You entered a boat full of Pirates.")
    else:
        print("Game Over, Nothing like that.")        
elif crossRoad == "right":
    print("Game Over, You fell into a hole of Spiders.")
else:
        print("Game Over, Nothing like that.")        
        
        
# Heads or Tails Game 
import random

test_seed = int(input("Create a seed number.\n"))
random.seed(test_seed)

num = random.randint(0, 1)
if num == 0:
    print("Heads!")
else:
    print("Tails!")            
    
    
# Select a random person to pay the bill
import random

# if you want a seed number.
# seedNum = int(input("Create a seed number.\n"))
# random.seed(seedNum)
namesAsCSV = input("Give me the names of everyone, seperated by a comma.\n")
names = namesAsCSV.split(", ")
# billPayer = random.choice(names) OR
numOfNames = len(names)
indexOfBillPayer = random.randint(0, numOfNames - 1)
billPayer = names[indexOfBillPayer]
print(f"{billPayer} is going to pay the bill.")    


# Rock, Paper, Scissors Game
import random

scissors = '''
    _____)_____
    ___________)
    ___________)
'''
rock = '''
    ________
    (_______)
    (_______)
'''
paper = '''
    ___)____
    ________)__
    ___________)
    __________)
    ______)
'''
choices = [rock, paper, scissors]
userChoiceNum = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computerChoiceNum = random.randint(0, 2)
userChoice = choices[userChoiceNum]
computerChoice = choices[computerChoiceNum]
print(userChoice)
print(f"Computer chose:\n {computerChoice}")
if userChoice == rock and computerChoice == paper:
    print("You lose")
elif userChoice == rock and computerChoice == scissors:
    print("You win")
elif userChoice == paper and computerChoice == rock:
    print("You win")
elif userChoice == paper and computerChoice == scissors:
    print("You lose")
elif userChoice == scissors and computerChoice == rock:
    print("You lose")
elif userChoice == scissors and computerChoice == paper:
    print("You win")
elif userChoice == computerChoice:
    print("You drew")
                             

# Addition of numbers from 1-100(with a step of 2 each time)
total = 0
for n in range(0, 101, 2):
    total += n
print(total)           


# FizzBuzz Game
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")     
    elif n % 3 != 0 or n % 5 != 0:
        print(n)                          
        
        


# Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

for alpha in letters:
    alpha = random.choices(letters, k = nr_letters)
for num in numbers:
    num = random.choices(numbers, k = nr_numbers)
for sym in symbols:
    sym = random.choices(symbols, k = nr_symbols)       
passw = alpha + num + sym
random.shuffle(passw)
password = ''.join(passw)
print(f"Your password is: {password}")

# Defining Functions
def greet():
    print("Good Morning")
    print("What's your name")
    print("Nice to meet you")
greet()


# Number of Cans of Paint Calculator
import math
def paint_calc(height, width, cover):
    numOfCans = (height * width) / cover
    approxCans = math.ceil(numOfCans)
    print(f"You'll need {approxCans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Prime Number checker
def prime_checker(number):
    # This prime number checker is only valid for numbers 1 - 100
    # if number == 2 or number == 3 or number == 5 or number == 7:
    #     print("It's a prime number.")
    # elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
    #     print("It's not a prime number.")
    # else:
    #     print("It's a prime number.")
    # OR
    isPrime = True
    for num in range(2, number):
        if number % num == 0:
            isPrime = False
    if isPrime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")                   
    
n = int(input("Check this number: "))
prime_checker(number=n) 


# Grade Generator(Testing kowledge of dictionaries)
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}
for student in student_scores:
    student_grades[student] = student_scores[student]
    if student_grades[student] >= 91:
        print(f"{student} is Oustanding")
    elif student_grades[student] >= 81 and student_grades[student] <= 90:
        print(f"{student} is Excellent")
    elif student_grades[student] >= 71 and student_grades[student] <= 80:
        print(f"{student} is Acceptable")
    elif student_grades[student] <= 70:
        print(f"{student} Failed")
print(student_grades)
# OR
# for student in student_scores:
#     grade = student_scores[student]
#     if grade >= 91:
#         print(f"{student} is Oustanding")
#     elif grade >= 81 and grade <= 90:
#         print(f"{student} is Excellent")
#     elif grade >= 71 and grade <= 80:
#         print(f"{student} is Acceptable")
#     elif grade <= 70:
#         print(f"{student} Failed")




# Travel log app to test knowledge in nesting of documents and list
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
] 

def add_new_country(countryParam, visitsParam, citiesParam):
    new_country_param = {
        "country": countryParam,
        "visits": visitsParam,
        "cities": citiesParam,
    }
    travel_log.append(new_country_param)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log) 


          
# Secret Aucttion App
logo = '''
                     ___________
                     \         /
                      )_______(
                      |"""""""|_.-._,.---------.,_.-._
                      |       | | |               | | ''-.
                      |       |_| |_             _| |_..-'
                      |_______| '-' `'---------'` '-'
                      )"""""""(                    
                     /_________\ 
                     `'-------'`
                   .-------------.
                   /_______________\ 
'''
print(logo)
print("Welcome to the secret auction program.")
totalBidders = {}
userAnswer = "yes"
while userAnswer == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders = {
        name: bid,
    }
    totalBidders[name] = bidders[name]
    # OR bidders.update({name: bid})
    userAnswer = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if userAnswer == "no":
        nameOfBidder = max(totalBidders, key = totalBidders.get)
        highestBid = totalBidders[nameOfBidder]
        print(f"The winner is {nameOfBidder} bidding ${highestBid}.")
        
        

# Getting Days in a Month from a Year
def is_leap(year):
    div4 = year % 4
    div100 = year % 100
    div400 = year % 400
    if div4 == 0:
        if div100 == 0:
            if div400 == 0:
                return True
            else:
                return False
        else:
            return True
    else: 
        return False   
    
def days_in_month(yearParam, monthParam):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31, 31]
    if is_leap(yearParam) == False:
        return month_days[monthParam - 1]
    elif is_leap(yearParam) == True:
        if monthParam == 2:
            month_days[1] = 29
        return month_days[monthParam - 1]
      
year = int(input("What year?: "))
month = int(input("Which month?: "))
days = days_in_month(year, month)
print(days)
                  

# List Comprehension   
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]

print(squared_numbers)

result = [num for num in numbers if num % 2 == 0]

print(result)                  

# Dictionary Comprehension
sentence = "What is Airspeed Velocty of an Unladen Swallow?"
word_list = sentence.split(" ")
result = {word: len(word) for word in word_list}

print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)



# unlimted args
def add(*args):
    value = 0
    for n in args:
        value += n
    print(value)    

add(4, 5, 6, 2, 10, 11)


# Error Handling
fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:    
        print(fruit + " Pie")
    
    
make_pie(4)


face_book_posts = [
    {"Likes": 21, "Comments": 2},
    {"Likes": 13, "Comments": 2, "Shares": 1},
    {"Likes": 33, "Comments": 8, "Shares": 3},
    {"Comments": 4, "Shares": 2},
    {"Comments": 1, "Shares": 1},
    {"Likes": 19, "Comments": 3}
]

total_likes = 0

for post in face_book_posts:
    try:
        total_likes += post["Likes"]
    except KeyError:
        post["Likes"] = 0    
        total_likes += post["Likes"]
        
print(total_likes)

