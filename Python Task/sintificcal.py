import math
print("1= tan ")
print("2= sin ")
print("3= cos ")
c = int(input ("enter the claculate number: "))
if c>=1 and c<=3:
    while True:

                    if c==1:
                        a = int(input("enter the tan value : "))
                        print(math.tan(a)) 
                    if c==2:
                        b = int(input("enter the sin value : "))
                        print(math.sin(b)) 
                    if c==3:
                        m = int(input("enter the cos value : "))
                        print(math.cos(m)) 
                    
        
                    n = input("Let's do next calculation? (yes/no): ")
                    if n == "no":
                            break
else:
    print("pleas select the 1 to 3 ")

        
