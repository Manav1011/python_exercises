number=int(input("Enter a number:"))
list=list(range(2,number))
for i in list:
    if number%i==0:
        print("Number is not prime")
        break
else:
    print("number is  prime")