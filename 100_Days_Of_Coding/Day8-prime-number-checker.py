def prime_checker(number):
    results = False
    
    # 1 is not prime number, and prime number cannot be negative number
    if number > 1:
        # 2 is prime number, but other even number is not
        # so to make 
        if number == 2:
            results = True
        # only check for odd numbers
        elif number%2 != 0:
            results = True
            for i in range(3,number,2):
                if number%i == 0:
                    results = False
                    break

    if results == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number")
        
n = int(input("Check this number: "))
prime_checker(number=n)
