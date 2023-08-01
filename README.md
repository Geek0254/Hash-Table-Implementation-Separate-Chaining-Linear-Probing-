# Hash Table Implementation

This repository contains three separate Python scripts that implement different methods for handling hash table collisions:

1. Separate Chaining
2. Linear Probing
3. Both (Separate Chaining then Linear Probing)

## Separate Chaining

The `Separate Chaining.py` script allows you to create a hash table using the Separate Chaining method. 
It prompts the user to input the size of the hash table and choose between randomly generating numbers or manually inputting numbers. 
The generated or inputted numbers will be inserted into the hash table using the Separate Chaining technique.

## Linear Probing

The `Linear Probing.py` script implements the Linear Probing method for handling collisions. 
Similar to the Separate Chaining script, it prompts the user to input the size of the hash table and choose between generating random numbers or manually inputting numbers. 
The numbers are then inserted into the hash table using Linear Probing.

## Both

The `Separate Chaining + Linear Probing.py` script combines both the Separate Chaining and Linear Probing implementations. 
It first creates a hash table using Separate Chaining, then waits for 3 seconds before displaying the same set of numbers in a new hash table using Linear Probing.

## How to Use

1. Clone the repository to your local machine using `git clone <repository-url>`.
2. Run the desired script by executing `python <script-name>.py` in your terminal.
3. Follow the prompts to input the hash table size and choose the input method for numbers.

Feel free to experiment with different inputs and observe how the hash tables are created with different collision resolution techniques.

