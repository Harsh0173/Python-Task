n= int(input("enter value :"))

if n<5 or n>50 :
    print('please enter value up to 5 and less to 50')
else :
    for i in range(0,n+1):
        for j in range(i):
            print ("*" ,end="")
        print(" ")
        
        

