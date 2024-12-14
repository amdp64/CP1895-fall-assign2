def GCD(a, b):

    GCD = 0

    if a > b:
        min = b
        GCD = a
    else:  
        min = a
        GCD = b 


    for i in range(1, min + 1):  
        if (( a % i == 0) and (b % i == 0 )):  
            GCD = i  

    return GCD

if __name__ == '__main__':
    while True:
        print("\nGreatest Common Divisor\n")
        a = int(input("Number 1: "))
        b = int(input("Number 2: "))
        
        print("Greatest common divisor: " + str(GCD(a, b)))

        if GCD(a,b) >=1:
            print("\nNumber 1 must be greater than Number 2. Try again!")
 
        continue_program = input("\nContinue? (y/n): ").strip().lower()
        if continue_program not in ('yes', 'y'):
            print("\nBye!")
            break