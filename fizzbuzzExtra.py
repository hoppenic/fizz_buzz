# making a more advanced fizzbuzz program 
# if user supplies inputs on command line, use that, else use the input function to obtain their input and run through the fizzbuzz loop
# have to switch the user input from a string to integer
# Converting str to int gave me trouble, it didn't seem to work like the thinkful text said it would

import sys

print("The name of this script is {}".format(sys.argv[0]))
print("User supplied {} arguments at run time".format(len(sys.argv)))



for arg in sys.argv[1:]:
    if int(arg) % 15 == 0:
      print("fizzbuzz")
    elif int(arg) % 3 == 0:
      print("fizz")
    elif int(arg) % 5 == 0:
      print("buzz")
    else:
      print(arg)
  

    
user_input=input("Please enter a number between 1 and 50")



for n in range(0,int(user_input)):
    if n % 15 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)
        
        
        
        
        
        
        
            


        
    
