# Print First 20 Even Number Series
""" for i in range(1,21):
   print(i*2, end=" ") """
    
#Input Any Number ( range)  and Display Even Number SEries till that number
""" print("")
num=int(input("enter the number till you need the series upto: "))
print(num)
i=1
while i*2<=num:
    print(i*2, end=" ")
    
    i=i+1 """

#Input Any Number and Display First that numberth Even Number Series

""" num=int(input("enter the number till you need the series upto: "))
print(num)
i=1
while i<=num:
    print(i*2, end=" ")
    
    i=i+1 """
    
#Generate First 15 Fibonacci SEries Elements

""" def fib(n):
    if n<0:
        print("incorrect input")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(9)) """
    
""" def print_fibonacci(n):
    f1=0
    f2=1
    if n<1:
        return
    print(f1, end=" ")
    for i in range (1,n):
        print(f2, end=" ")
        next=f1+f2
        f1=f2
        f2=next
print_fibonacci(10)
 """
 #Genereate First 15 Thibonacci Series Elements
 
"""  
def print_thibonacci(n):
    f1=0
    f2=1
    f3=1
    if n<1:
        return 
    elif n==1:
        print(f1, end=" ")
    elif n==2:
        print(f1, f2, end=" ")
    elif n>2:
        print(f1, f2, end=" ")
        for i in range (1,n-1):
            print(f3, end=" ")
            next=f1+f2+f3
            f1=f2
            f2=f3
            f3=next
    
print_thibonacci(3)
 """
 
#Input any Number and calculate its Factorial
""" 
def fact(n):
    if n<0:
        print("wrong input")
    elif n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5)) """

#Input two number and calculate their HCF and LCM

""" def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)
def lcm(a,b):
    return a*b/gcd(a,b)
    

num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
print(f"lcm of the two numbers is {lcm(num1,num2)}")    
print(f"hcf of the two numbers is {gcd(num1,num2)}")
        

     """

# Print Given Series 20 Elements

# 0	3	8	15	24	35.... 


""" for i in range(20):
    print(i*(i+2), end=" ")
 """


#Input Any Number and display its table

num=int(input("Enter the number you want the table for: "))
def table(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
table(num)
