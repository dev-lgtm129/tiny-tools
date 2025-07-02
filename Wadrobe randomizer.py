import random
import pyfiglet as pfg
heading = pfg.figlet_format("Wadrobe Randomizer" , font = 'doom')
print(heading)
#welocme message
print("Welcome!")
print()
#wadrobe input from user
tops =  input("Enter the tops in your wadrobe with color(seperate the naes using comma): ").split(",")
bottoms = input("Enter the bottoms in your wadrobe with color(seperate the naes using comma): ").split(",")
accessories = input("Enter the accessories in your wadrobe(seperate the naes using comma): ").split(",")
#creating list of the items in wadrobe
top_list =list(tops)
bottom_list = list(bottoms) 
accesssories_list =list(accessories)
t = len(top_list)
b = len(bottom_list)
a = len(accesssories_list)
#generating random number to randomly pick items
tt = random.randint(0,t-1)
bb = random.randint(0,b-1)
aa = random.randint(0,a-1)
print()
print("Randomized clothes are: ")
print("Wear "+str(top_list[tt] + " with "+ str(bottom_list[bb]+ " and "+ str(accesssories_list[aa]))))
print()
#thank you message
print("Thanks for using our randomizer!!")
print("Hope you liked my project")