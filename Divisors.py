number=int(input("Enter a number for which you want to find divisors: "))
ran=list(range(1,number+1))
for i in ran:
    if(number%i == 0):
        print(i)
