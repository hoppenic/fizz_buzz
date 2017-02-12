

#test script using the int function
#did this differently than what the lesson taught but it worked as I couldn't figure out the other way



user_input=input("Please enter a number 1 through 10")

    
for n in range(0,int(user_input)):
    if n % 15 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)   
    
    
    
    
    
    
    
    
    
    

        
        