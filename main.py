#Importing the random library to generate a random library. 
import random

#Propting to enter a number that needs to be guessed. 
number = input("Enter number to be guessed:")

#Checking if the value is integer of not
try:
    
    #checking if the number is in range or not
    if 0< int(number) < 101:
        
        #creating a count variable to count the number of iterations.
        count = 0
        
        #creating the list of the numbers in the given range
        guess = list(range(1, 101))
        
        #while the list becomes empty
        while len(guess) > 0:
            rand_int = random.randint(0, len(guess)-1)
            
            #if the number is correct then print the iterations and breaking
            if guess[rand_int] == int(number):
                print(f'You guessed {number}, and it took program {count} iterations')
                break
                
            #if the number is not correct then we are deleting and incrementing the counter.
            else:
                count += 1
                guess.remove(guess[rand_int])
            
    else:
        print("Please enter a number between 1 and 100")
except:
    print("Please enter a valid number between 1 and 100")
