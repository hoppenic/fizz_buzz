import sys

print("The name of this script is {}".format(sys.argv[0]))
print("User supplied {} arguments at run time".format(len(sys.argv)))




for arg in sys.argv[1:]:
    if int(arg) % 15== 0:
      print("fizzbuzz")
    elif int(arg) % 3 ==0:
      print("fizz")
    elif int(arg) % 5==0:
      print("buzz")
    else:
      print(arg)
      



#for arg in sys.argv[1:]:
 # if arg % 15==0:
  #    print("fizzbuzz")
#  elif arg % 3 == 0:
 #     print("fizz")
#  elif arg % 5==0:
 #     print("buzz")
#  else:
 #     print(arg)
      
      
   
      
      
   