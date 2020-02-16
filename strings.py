str = "This is a demo text"

# Convert to upper case
print(str.upper())

# To check whether the string is numeric or not
print(str.isnumeric())

# Replace
print(str.replace("text", "TEXT"))

# ASCII
print(str.isascii())

# Indexing
print(str[3])

# Slicing
print(str[10:19])

# String formatting
name = input("Enter your name : ")
print("Your name is : {}".format(name))

# String formatting for multiple values
firstName = input("Enter your first name : "+"\n")
secondName = input("Enter your second name : "+"\n")

print("Your full name is : {} {}".format(firstName, secondName))

# String formatting for multiple values
firstName = input("Enter your first name : "+"\n")
secondName = input("Enter your second name : "+"\n")

print("Your full name is : {1} {0}".format(secondName, firstName))

# Another type of formatting
x = "Marvel"
y = f"{x} Avengers"
print(y)