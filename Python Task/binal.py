n= int(input("enter value :"))

if n<5 or n>20 :
    print('please enter value up to 5 and less to 20')
else :
        for i in range(1,n+1):
            for m in range(i):
                    print("*",end="")
            for j in range(2*n-i*2):
                    print(" ",end="")
            for k in range(0,i):
                    print("*",end="")
            print()
        for i in range(1,n):
            for j in range(n-i):
                    print("*",end="")
            for k in range (2*i):
                    print(" ",end="")
            for m in range(n-i):
                print("*",end="")
            print()