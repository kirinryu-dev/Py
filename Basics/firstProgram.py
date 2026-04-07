# This is the first simple program in python 
# ======= Basics ======= 
# 1. Variables and Data Types 
# Data types 
# string = text 
name = "Alice" ;
greating = "Hello world" ;

# integer = numbers 
age = 31
temperature = 37 # (healthy human temp)

# float = number with " . "
height = 2.5 
pi = 314149 

# boolean = true / false 
is_student = True 
has_driving_licence = False 

# none (is an abscence of value)
data = None

# type checking 
# print(type(name)) ;
# print(type(height)) ;
# print(type(is_student)) ;

# Variables and operations 
x = 3 
y = 10 
c = 100
d = 999

a = x ;
b = y ;

# print(a + b) ;
# print(b - a) ;
# print(c * d) ;
# print(d // a) ;
# print(a % b) ;

# input and output 
# this small exercice ask the user for his name and age 
# user_message = "What is your name ? : "
# user_message_1 = "How old are you ? : "
# name = input(user_message) ;
# age = int(input(user_message_1)) ;

# output formating 
# 1
# print(f"Hello {name} , you are {age} years old") ;
# 2
# print("Hello {name} , you are {age} yeras old".format(name,age)) ;

# 2. statements
# control structures if...else
age = 61

# if age>= 18:
#     print(f"You are {age} years old") ;
# elif age>= 13:
#     print("You are still young") ;
# else:
#     print("You are a child") ;

# list and tuple 
# List are mutable and can be changed 

fruits = ["apple", "banana", "avocado", "potato", "mango"] ;
numbers = [1, 2, 3, 4, 5] ;
mixed = ["hello", 2, 6, "avocado"] ;

# accessing element starts with 0 index :
# print(fruits[2]) ;
# print(numbers[0]) ;
# print(mixed[2:3]) ;

fruits.append("orange") ;
fruits.append("banana") ;
numbers.remove(2) ;
fruits.insert(1, "mojomo") ;
pop = fruits.pop() ;
# print(fruits) ;
# print(numbers) ;
fruitsLength = len(fruits) ;
# print(fruitsLength) ;

# tuple can not be changed immutable 
coordinate = (10,2) 
rgb = (255,255,0) 
# tuples are said to be faster and prevent changes incidents 
# you can inpack them 
# x,y = coordinate 
# y,x = coordinate 
# print(y) ;
# print(x) ;


# dictionary key-value pair 
# creating dictionary 
person = {
    "name": "alice" ,
    "age": 31 ,
    "city": "Lome"

}
# print(person["name"]) ;
name = person["name"] ;
age = person["age"] ;
city = person["city"] ;

# print(name) ;
# print(age) ;
# print(city) ;
# print("======== Final Output ==========") ;
# print(f"The user is called {name} and her/his age is {age}. They live in {city}") ;
# modifying / adding to dictionary 
person["age"] = 61 
job = person["job"] = "Engineer"
print("=== Final Output ===") ;
print(f"The user is called {name} and she/he is {age} and lives in {city}.") ;
print(f"Her job is {job} .") ;
# interacting with dict
print(person.keys()) ;
print(person.values()) ;
print(person.items()) ;
for key, value in person.items():
    print(f"{key}: {value}") ;

# 3. Functions and Modules
# 4. Object-Oriented Programming (Classes and Objects)
# 5. Exception Handling (try, except)
# 6. File Handling (open, read, write)
# 7. Libraries and Frameworks (e.g., NumPy, Pandas, Flask
