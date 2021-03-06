# Hashing exercise
# Avery Nutting-Hartman
# 10/28/2020
# Instructions for use in README

from argon2 import PasswordHasher, exceptions
ph = PasswordHasher()


def setup(password):
    # hash initial password
    # uses a 16 bit random salt and has a time cost to prevent brute force
    return ph.hash(password)


def check_password(hash_obj, password):
    # check the entered password based on first hash
    try:
        return ph.verify(hash_obj, password)
    except exceptions.VerifyMismatchError:
        return False


def prompt_loop():
    # loop that gets the user input
    first_pass = input("Enter initial password:")
    hash_obj = setup(first_pass)
    del first_pass
    print("Hash value: " + hash_obj)
    flag = False
    while not flag:
        flag = check_password(hash_obj, input("Enter your password:"))
        if flag:
            print("Successful Authentication!")
        else:
            print("Password incorrect! ")


if __name__ == '__main__':
    prompt_loop()
