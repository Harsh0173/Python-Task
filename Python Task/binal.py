n= int(input("enter value :"))

if n<5 or n>50 :
    print('please enter value up to 5 and less to 50')
else :
       for i in range(1,n+1):
            for m in range(i):
                    print("*",end="")
            for j in range(2*n-i*2):
                    print(" ",end="")
            for k in range(0,i):
                    print("*",end="")
            print()