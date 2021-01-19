#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = []
for letter in range(0,nr_letters):
  seed = random.randint(0,len(letters)-1)
  password.append(letters[seed])
for symbol in range(0,nr_symbols):
  seed = random.randint(0,len(symbols)-1)
  password.append(symbols[seed])
for number in range(0,nr_numbers):
  seed = random.randint(0,len(numbers)-1)
  password.append(numbers[seed])

#Printing the result of easy method 
pass_str = ""
for character in range(0,len(password)):
  pass_str += str(password[character])
print(password)
print(pass_str)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_hard = []
pass_str_hard = ""
total_char = nr_letters + nr_symbols + nr_numbers
for character in range(0, total_char):
  randchar = random.randint(0,2)
  print(randchar)
  if randchar == 0 and nr_letters != 0:
    seed = random.randint(0,len(letters)-1)
    password_hard.append(letters[seed])
    nr_letters -= 1
  elif randchar == 1 and nr_symbols != 0:
    seed = random.randint(0,len(symbols)-1)
    password_hard.append(symbols[seed])
    nr_symbols -= 1
  elif randchar == 2 and nr_numbers != 0:
    seed = random.randint(0,len(numbers)-1)
    password_hard.append(numbers[seed])
    nr_numbers -= 1

#Printing the result of the hard method
for character in range(0,len(password_hard)):
  pass_str_hard += str(password_hard[character])
print(password_hard)
print(pass_str_hard)
