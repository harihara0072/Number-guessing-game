# Number-guessing-game

Program where the user and the program/computer trade
places in the number guessing game. Prompt the user for a number (between 1
and 100, inclusive) that the program/computer has to guess. The program also keeps track of the
number of iterations it takes for the computer to guess the number. 

Algorithm:

1. The program asks for the number from the user that needs to be guessed and stores in a variable 'number'
2. Then we are checking if the value is a number or not, and if that is in the given range(1-100). If either of it fails then 
    the program prints the user to enter the proper number in the given range.
3. Then creating a list of all the values in the given range and then we use this for guessing. 
4. We generate a number randomly that will be used as the index of the guess list from the previous step and if that number is 
      what we are guessing then the program will quit or else it will increase the counter, delete that number from  and then   repeat this step until it finds the number
      
Steps to Execute:

Run the next three cells to run the program.

Expected output:

One example run: When we enter 50.

Output:
You guessed 50, and it took program 34 iterations
