n= int(input("enter value :"))

if n<5 or n>20 :
    print('please enter value up to 5 and less to 20')
else :
        for i in range(n):
                print("*",end="")
        print()
        for k in range(1,n):
            print("*",end="")
            for j in range(2,n):
                print(" ",end="")
            print("*")
        for m in range(n):
                print("*",end="")
