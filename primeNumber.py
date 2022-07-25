def prime_checker(number):
    n = number
    for i in range(2,n):
        if n%i==0 :
            print("It is not prime number")
            return
    print("It is prime number")
n = int(input("Check this number: "))
prime_checker(number=n)