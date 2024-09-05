#string concatenation program
'''print("Hello\nWorld!")
print("Hello"+" World!")
'''
# Data types program

# name = input("Enter name: ")
# age = input("Enter age: ")
# isEligible = input("Eligible for voting?: ")
# print(name,"who is", age, "years of age", "is eligible for voting:", isEligible)

# name=input("Enter name: ")
# print("Happy birthday",name)

# a=input("Enter juice 1: ")
# b=input("Enter juice 2: ")
# a,b=b,a
# print(a,b)

# name=input("Enter name: ")
# name_length=len(name)
# # print("Hi",name+"! your name has",str(name_length),"characters!")
# print(f"Hi {name}! Your name has {name_length} characters!")

# Program 1
# a=input("Enter string: ")
# print(a[-1])
# print(a.upper())
# print(a.count("n"))
# print(a.capitalize())
# print(a.replace(a,"thinknyxtechnologies"))
# print(a.find("in"))
# print(a.startswith("t"))
# print(" thinknyx".lstrip())

# Formatting
# ip="IP addresses are {}{} and {}{}"
# x="192.168."
# print(ip.format(x,"1",x,"2"))
# for i in range(0,2):
#     for j in range(1,11):
#         print(f"192.168.{i}.{j}")

# Join
# a="thinknyx"
# print("-".join(a))

# Arithmetic 
#calculate BMI:
# weight=float(input("Enter weight in kg: "))
# height=float(input("Enter height in m: "))
# BMI=weight/(height**2)
# print(round(BMI,1))
# if(BMI<=18.5):
#     print("Underweight")
# elif(BMI<=25):
#     print("Normal weight")
# elif(BMI<=30):
#     print("Slightly Overweight")
# elif(BMI<=35):
#     print("Obese")
# else:
#     print("Clinically obese")
# print("Underweight") if(BMI<=18.5) else print("Normal weight") if(BMI<=25) else print("Slightly Overweight") if(BMI<=30) else print("Obese") if(BMI<=35) else print("Clinically obese")

# Tip calculator
# principal=float(input("Enter Principal amount: "))
# num=int(input("Enter the number of people: "))
# interest=int(input("Enter interest rate(12%,14%,16%): "))
# if(interest!=12 and interest!=14 and interest!=16):
#     print("Enter correct interest rate")
# else:
#     amt=(principal/num)*(1+interest/100)
#     print(round(amt,2))

# Roller coaster program
# height=float(input("Enter height in cm: "))
# if(height>120):
#     print("Can ride")
#     age=int(input("Enter age: "))
#     if(age<12):
#         print("Pay Rs.50")
#     elif(age>18):
#         print("Pay Rs.150")
#     else:
#         print("Pay Rs.100")
# else:
#     print("Can't ride")

#Find odd or even
# num=int(input("Enter number: "))
# if(num%2):
#     print("Odd")
# else:
#     print("Even")

# Prime number
# import math
# def prime(num):
#     i=2
#     if((not num%2) and num>2):
#         return 1
#     while(i<=math.sqrt(n)):
#         if(not(num%i)):
#             return 1
#         i+=1
#     return 0

# n=int(input("Enter number: "))
# flag=prime(n)
# if(flag):
#     print("Not prime")
# else:
#     print("Prime")

# Sum of odd numbers
# num=int(input("Enter number: "))
# i=1
# sum=0
# for i in range(i,num+1):
#     if(i%2):
#         sum+=i
# print(sum)

#bizzbuzz game
# for i in range(1,101):
#     if(not i%15):
#         print("BizzBuzz")
#     elif(not i%3):
#         print("Bizz")
#     elif(not i%5):
#         print("Buzz")
#     else:
#         print(i)

# Pizza billing
# sum=0
# flag=1
# while(flag):
#     size1=input("Enter size of pizza (small,medium or large): ")
#     if(size1=="small"):
#         sum+=15
#     elif(size1=="medium"):
#         sum+=20
#     elif(size1=="large"):
#         sum+=25
#     else:
#         print("Invalid input")
#     q=int(input("Would you like cheese or pepporoni?(2 for cheese, 1 for pepporoni or 0): "))
#     while(q):
#         if(size1=="small" and q==1):
#             sum+=2
#         elif((size1=="medium" or size1=="large") and q==1):
#             sum+=3
#         if(q==2):
#             sum+=1
#         q=int(input("Would you like cheese or extra pepporoni?(2 for cheese, 1 for extra pepporoni or 0): "))
#     flag=int(input("Do you want another pizza?(1 for yes, 0 for no): "))
# print("Your total bill is:",sum)

# Functions and modules
# simple calculator
# from module_test import *
# print("Welcome to the Simple Calculator!")
# sum=0
# temp=1
# while(temp):
#     print("What do you want to do?\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
#     temp=int(input("Enter your option: "))
#     if(temp==5):
#         break
#     if(temp<1 or temp>5):
#         print("Invalid input")
#         continue
#     a,b=input("Enter the numbers: ").split()
#     a,b=[int(a),int(b)]
#     sum=calc(a,b,temp)
#     print("Your answer is:",sum)

#Leap year
# year=int(input("Enter the year: "))
# if(not year%4):
#     if(not year%100):
#         if(not year%400):
#             print("Leap Year")
#         else:
#             print("Not Leap Year")
#     else:
#         print("Leap Year")
# else:
#     print("Not Leap Year")

# from math import *
# a=int(input("Enter number: "))
# print(factorial(a))
# print(pi)

# from random import *
# print(choice(["heads","tails"]))

# from module_test import *
# userscore,computerscore=0,0
# while True:
#     flag=int(input("-------------------------------\nDo you want to play?(0 or 1): "))
#     if(not flag):
#         break
#     user=get_user_choice()
#     if(user not in ["rock","paper","scissors"]):
#         print("Invalid input")
#         continue
#     comp=ran()
#     result=compare(user,comp)
#     a,b=calculatescore(result)
#     userscore+=a
#     computerscore+=b
#     print("Computer choice:",comp)
#     print("----------------------------------------------------------------\n******",result,f"******  Score -> User:{userscore}, Computer:{computerscore}\n----------------------------------------------------------------\n")
l=[1,2,3,4]
print(type(l))