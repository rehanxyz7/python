number =int(input("Enter a number to check \n"))
is_prime =True

if number>1:
    for i in range(2,number):
        if( number%2)==0:
            is_prime = False
            break
print(f"{number } is prime :  {is_prime} ")