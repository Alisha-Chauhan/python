print("Hello")
print('Hello')

#Assign String to a Variable
a = "Hello"
print(a)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#looping through a string
for x in "banana":
  print(x)

#String Length
a = "Hello, World!"
print(len(a))


# Check String
txt = "The best things in life are free!"
print("free" in txt)


#Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)



#Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")