import math
import pyfiglet as pfg
header = pfg.figlet_format("Calculator" )
print(header)
#welcome message
print('Welcome to basic math calculator')
print()
#Function selection
print("""Select the operation you want to perform 
  1: Addition
  2: Subtraction
  3: Multiplication
  4: Division
  5: Logarithm
  6: Anti log
  7: Exponents
  8: Trignometric Function
  9: Inverse trignometeric functions""" )
choice = int(input("Enter your choice[1/2/3/4/5/6/7/8/9]: "))
print()
#user input
while True:
    #addition
    if choice == 1: 
        a , b = map(int,input("Enter the numbers you want to add seperated by a space: ").split())
        summ = a + b
        print("The sum is " + str(summ))
    #difference
    elif choice == 2: #difference
        c , d = map(int,input("Enter the numbers to get the difference seperated by a space: ").split())
        diff = abs(c - d)
        print("The difference is "+ str(diff))
     #product
    elif choice == 3:
        e , f = map(int,input("enter the numbers to multiply seperated by a space: ").split())
        product = e*f
        print("The product is "+ str(product))
     #division
    elif choice == 4: #division
        g , h = map(int,input("Enter the numbers you want to divide(divident then divisor) seperated by a space: ").split())
        div = g/h
        print("The result is " + str(round(div, 4)))
    #log
    elif choice == 5:  
        base = int(input("""Select the base of the logarithm[1/2/3]
                         1:Base 10
                         2:Base e (natural log)
                         3:Base 2 """))
        i = abs(int(input("Enter the number to take log: ")))
        if base == 1:
            print(round(math.log10(i), 5))
        elif base == 2:
            print(round(math.log(i), 5))
        elif base ==3:
            print(round(math.log2(i), 5))
        else:
            print("Invalid input. Try again")
    #antilog
    elif choice == 6:  
        abase = int(input("""Select the base of antilog[1/2]:
                          1: Base 10
                          2: Base e """))
        j = abs(int(input("Enter the number: ")))
        if abase == 1:
            print(round(10**j, 5))
        elif abase == 2:
            print(round(2.7182**j, 5))
        else:
            print("Invalid input. Try again")
    #exponents
    elif choice == 7:
        k,l = map(int,input("Enter the number you want to raise power of to the power rasied, seperated by a space: ").split())
        print(round(pow(k,l), 3))
    elif choice== 8:  #trignometeric 
        tf = int(input("""Select the trignometeric function[1/2/3]:
                       1: Sine
                       2: Cosine
                       3: Tangent """))
        m = int(input("Enter the angle in degrees: "))
        n = math.radians(m)
        if tf == 1:
            print(round(math.sin(n), 2))
        elif tf == 2:
            print(round(math.cos(n), 2))
        elif tf == 3:
            print(round(math.tan(n), 2))
        else:
            print("Invalid input. Try again")
    #inverse trignometyery
    elif choice == 9:  
        itf = int(input("""Select the inverse trignometeric function[1/2/3]:
                       1: Sine inverse
                       2: Cosine inverse
                       3: Tangent inverse """))
        o = int(input("Enter the number: "))
        if itf == 1:
            print(round(math.asin(o), 2))
        elif itf ==2:
            print(round(math.acos(o), 2))
        elif itf ==3:
            print(round(math.atan(o), 2))
        else:
            print("Invalid input. Try again")
    else:
        print("Invalid input. Try again")
    break