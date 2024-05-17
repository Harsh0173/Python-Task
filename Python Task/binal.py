n= int(input("enter value :"))

if n<10 or n>100 :
    print('please enter value up to 10 and less to 100')
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