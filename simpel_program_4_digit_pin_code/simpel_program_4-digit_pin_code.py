#simpel program 4_digit pin code 

import random
code_random_number=random.randint(1000,9999)

user=int(input("Enter a 4 your pin code:"))
if len (str(user))!=4:
    print("Please enter 4 diglits")
elif user==code_random_number:
    print("succes your pin cod is match")    

else:
    print (f"the computer generate pin: {code_random_number}")    
