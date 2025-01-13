#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # On décrémente n pour éviter une boucle infinie
    return result

if len(sys.argv) > 1:  # Vérification qu'un argument est passé
    try:
        number = int(sys.argv[1])
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            f = factorial(number)
            print(f)
    except ValueError:
        print("Please provide a valid integer.")
else:
    print("Usage: ./script_name <integer>")
