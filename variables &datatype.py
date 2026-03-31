# Question 1(variables): Create a variable with your name and print it.
name="My name is Anika" 
print(name)
 
 #Question 2(variables): Create two variables, one for your age and one for your city. Print both.
 
age= 24 
city="Chattogram" 
print(age)
print(city)

#Question 3(variables): Create two number variables, add them together and print the result.


num1=26
num2=31
add=num1+num2
print(add)

#Question 4(variables): Create a variable and change its value, then print both old and new value.

age=24
print(age) #prints old value:24
age=25
print(age) #prints new value:25

#Question 5(variables): Create 3 variables — your name, age, and country. Print them all in one line.

name="Anika"
age=24
city="Chattogram"
print("My name is", name,"My age is", age,"My City is", city)


#Question 1(data types)Create 3 variables — your name, age, and country. Print them all in one line .

name="Anika" 
age=24
country="Bangladesh"
print(type(name))
print(type(age))
print(type(country))

#question 2 (data types)Create variables of 4 different types (str, int, float, bool) and print their types using type()
name="Anika" 
age=24
price=20.5
name_Anika = True
print(name_Anika)
print(type(name_Anika))

#Question 3: (data types) Create a variable temperature = 36.6 and print its type.

temperature=36.6
print(type(temperature))

#question 4:(data types) Create is_working = False and print it and its type.

is_working = False
print(type(is_working)) 

#question 5:(data types) Convert price = 99 to float using float(price) and print the result.

price=98.9
print(price)

#Question 6:(data types) Convert height = "5.6" to float using float(height) and print its type.

height=5.6
print(type(height))

#Question 7:(data types) Create these variables and print all types:
city = "Dhaka"
population = 2000000
area = 306.38
is_capital = True

#Solution

city="Dhaka" 
population=2000000
area=306.38
is_capital=True
print(type(city))
print(type(population))
print(type(area))
print(type(is_capital))


#Question 8:Write a program to input 2 numbers & print their sum

first=int(input("enter first:"))
second=int(input("enter second:"))
print("sum =", first+second)

#Question 9:WAP to input side of a square & print its area

side=float(input(" enter square side:"))
print("area=",side*side)

#Question 10:WAP to input 2 floating point numbers & print their averagr

a=int(input(" enter first num:"))
b=int(input(" enter second num:"))
print("avg=",(a+b)/2)

#Question 11: WAP to input 2 int numbers,a and b.
#print True if a is greater than or equal to b.If not print False

a=int(input(" enter first num:"))
b=int(input(" enter second num:"))
print(a>=b)