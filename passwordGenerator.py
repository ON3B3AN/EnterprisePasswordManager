import passwordStrengthTest as test
from termcolor import colored
import encryptDecrypt as crypt
import random


def generate_passwords():
    crypt.generate_key()
    uppercase_letters = "ABCDEFGHIJKLNMOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    ambiguous_characters = "{}[]()/\\\'\"`~,;:.<> "
    symbols = "@#$%!&*"

    upper, lower, nums = True, True, True

    length = int(input("Enter your desired password length (min: 8): "))
    number = int(input("Enter the number of passwords to generate: "))

    def add_symbols(answer):
        if answer.upper() == "Y" or answer.lower() == "y":
            syms = True
        elif answer.upper() == "N" or answer.lower() == "n":
            syms = False
        else:
            print("Input not recognized")
            syms = add_symbols(input("Use symbols? (y/n): "))
        return syms

    def add_ambiguous_characters(answer):
        if answer.upper() == "Y" or answer.lower() == "y":
            chars = True
        elif answer.upper() == "N" or answer.lower() == "n":
            chars = False
        else:
            print("Input not recognized")
            chars = add_ambiguous_characters(input("Use ambiguous characters? (y/n): "))
        return chars

    def generate_password(syms, chars, count=0):
        password = ""
        if upper:
            password += uppercase_letters
        if lower:
            password += lowercase_letters
        if nums:
            password += digits
        if syms:
            password += symbols
        if chars:
            password += ambiguous_characters

        print(" ")

        i = 1
        while i <= number:
            i += 1
            pwd = "".join(random.sample(password, length))
            if test.validate_password_strength(pwd):
                crypt.encrypt_password(pwd)
                count += 1
            else:
                i -= 1
        print("\nPasswords successfully generated " + "{" + colored(str(count), "green", attrs=['bold']) + "}\n")

    generate_password(add_symbols(input("Use symbols? (y/n): ")),
                      add_ambiguous_characters(input("Use ambiguous characters? (y/n): ")))