# Create variables 
# Display the data type of a variable 
# Change from one data type to the other
# Take inputs from a user 
# Display outputs to a user 


#Variables
Name = ""
Age = 0
Legal = False
BMI = 35.67
Hobbies = ["Drawing", "Painting", "Grafitti"]
Favorites = {}
Pairs = ()

#Data types
print (f"The variable Name is of data type {type(Name)}")
print (f"The variable Age is of data type {type(Age)}")
print (f"The variable Legal is of data type {type(Legal)}")
print (f"The variable BMI is of data type {type(BMI)}")
print (f"The variable Hobbies is of datat type {type(Hobbies)}")
print (f"The variable Favorites is of data type {type(Favorites)}")
print (f"The varible Pairs is of data type {type(Pairs)}")

#Change data types
Age1 = str(Age)
print(f"Age is now a {type(Age1)}")
Age2 = float(Age)
print (f"Age is now a type {type(Age2)}")
Legal1 = str(Legal)
print(f"Legal is now a {type(Legal1)}")

#Allow user input
FName = input(f"What is your first name? ")
LName = input(f"What is your last name? ")
AGe = int(input(f"How old are you? ")) 
List = []
n = int(input(f"How many items will be in the list? "))
for i in range(n):
    a = input("Complete the list")
    List.append(a)

b = input("Any thing to go into the tuple")
c = input("Another thing to go into the tuple")   
Tup = (b,c)


#Outputing 
print (f"My name is {FName} {LName} and i am {AGe} years old. For my list, I have {List} and I have {Tup} for my tuple")

