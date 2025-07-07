import random
import time
import pyfiglet as pfg
heading = pfg.figlet_format("Password Generator" , font = 'big' )
print(heading)
#creating list of each type
lowercase = list("abcdefghijklmnopqrstuvwxyz")
uppercase = list("ABCDEFGHIJKLMONPQRSTUVWXYZ")
symbols = list("!@#$%*^&?[](){}")
numbers = list("1234567890")
numbers_2 = list("345")
y = int(random.choice(numbers_2))
#password
characters = lowercase + uppercase + symbols + numbers 
#lenght of password
try:
	password_length = int(input("Enter the number of characters you want in the password: "))
	print("Generating password please wait...")
	time.sleep(y)
	#joining password
	password = ''.join(random.choices(characters , k = password_length))
	time.sleep(1)
	print("")
	print("Your password is: ", password)
	time.sleep(1)
	print("We reccomend to write down this password somewhere safe or use a password manager like bitwarden")
	print("Thanks for using our password generator")
except:
	print("Invalid input. Enter a natural number")
