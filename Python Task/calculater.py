print("1= + ")
print("2= - ")
print("3= * ")
print("4= / ")
c = int(input ("enter the claculate number: "))
if c>=1 and c<=4:
    while True:

                    if c==1:
                        a = int(input("enter the value a: "))
                        b = int(input("enter the value b: "))
                        print(a+b) 
                    if c==2:
                        a = int(input("enter the value a: "))
                        b = int(input("enter the value b: "))
                        print(a-b)
                    if c==3:
                        a = int(input("enter the value a: "))
                        b = int(input("enter the value b: "))
                        print(a*b)
                    if c==4:
                        a = int(input("enter the value a: "))
                        b = int(input("enter the value b: "))
                        print(a/b)
        
                    n = input("Let's do next calculation? (yes/no): ")
                    if n == "no":
                            break
else:
    print("pleas select the 1 to 4 ")

        

