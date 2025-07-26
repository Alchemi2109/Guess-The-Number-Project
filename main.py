

import random 
n = random.randint (1, 100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the Number: "))
    if (a > n):
        print("Guess Lower number please :) ")
        guesses += 1
    elif(a < n):
        print("Guess Higher number please :)")    
        guesses += 1
    
if (guesses < 10):
    print(f"Congratulaions! you have guessed the Right number {n} in {guesses} attempt.... You are a Guessing Master ")

else:
    print(f"Congratulaions! you have guessed the Right number {n} in {guesses} attempt.... ")     

# print(f"Congratulaions! you have guessed the Right number{n} in {guesses} attempt.... You are a guessing Master ")
