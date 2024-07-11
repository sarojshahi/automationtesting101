#Agenda
#IF ELSE STATEMENT
#NESTED ELSE IF STATEMENT
#FUNCTION
#OOPS
#CONSTRUCTOR
#IMPORT MODULE

#IF ELSE STATEMENT
# num = -12
# if(num>0):
#     print("The Number is Positive")
# elif(num<0):
#     print("The Number is Negative")
# else:
#     print("The Number is zero")
#
# age = int(input("Enter your age: "))
# if(age>18):
#     print("You are an adult")
# elif(age<18 and age>12):
#     print("You are a teenager")
# else:
#     print("You are an infant")

#NESTED IF ELSE
# score = int(input("Enter a number number: "))
# if(score>=32 and score<=100):
#     if(score>=32 and score<50):
#         print("You are just pass")
#     elif(score>=50 and score<80):
#         print("You are an average student23")
#     else:
#         print("You are a bright student")
# elif(score<32 and score>=0):
#     print("You have failed")
# else:
#     print("Input Invalid")

#FUNCTION
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.

# def sum(num1, num2):
#     return num1 + num2
# print(sum(1,2))

# def multi(num1, num2):
#     return print( num1 * num2 )
#
# multi(3,4)
#
# def div (num1, num2):
#     return print(num1/num2)
# div(12,3)

# def add(num1, num2=10): #formal Arguement
# 	print(num1+num2)
# add(3,4) #actual arguement
# add(6)
# add(5,6)

# def print_name(name):
#     return print(name)
#
# print_name("Saroj")
# print_name("Proush")
# print_name("Youtube")
# print_name("Code with Harry")

# def func():
#     x=5
#     print("The value of x is ", x)
# func()
# print("The value of y is 10")

#Class
# class Students:
#     name = "Saroj Shahi"
#     course = "QA"
#     age = 10
#     def state(self):
#         print(f"{self.name} is a of age {self.age}")
# student = Students()
# student.name = "Proush"
# student.course = "Design"
# student.age = 12
# 
# print(student.name, student.age)
# student.state()



class Library:
    book = "Harry Potter"
    writter =  "JK Rolling"
    price = 1000
    def info(self):
        print(f"{book} is written by {writter} and sold at {price}")

books = Library()
books.book = "The perks of being a wallflower"
books.witter = "Stefan Chbosky"
books.price = 500

books.info()