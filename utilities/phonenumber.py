# Write a code that takes a 10 Digit number input from user and checks if it is an Atlanta number by matching the area code 404

def no_of_digits(n):
    count = 0
    while n != 0:
        n = n//10
        count +=1
    return count

try:
    PhoneNumber = int(input("Enter your Phone Number: "))
    Digits = no_of_digits(PhoneNumber)
    
    if Digits == 10: 
        AreaCode = PhoneNumber//10**7
        if AreaCode == 404:
            print("This is an Atlanta Number")
        else:
            print("This is not an Atlanta Number")
    else:
        print("Please input a valid 10 digit number")
except ValueError:
    print("Please input a Valid 10 digit Number")
