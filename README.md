# ex04hashing

Python program for exercise 4 for database application development. 

Allows you to enter a password and will take the password, add a random 16 bit salt and then hash using argon2 it. 
Then it will print out the hash and allow you to enter other passwords that will validate it agaist the first one entered

## Instructions 
1. Clone the  repo 
2. install the argon2-cffi 20.1.0 by running `pip install argon2-cffi` or a different way https://pypi.org/project/argon2-cffi/
3. run hashing.py with python 3
4. Enter a password and it will print the hash of the password
