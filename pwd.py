from itertools import product
import string

def generate_combinations():
    letters = string.ascii_lowercase
    digits = string.digits
    characters = letters + digits
    
    with open('combinations.txt', 'w') as f:
        for length in range(1, 4):
            for combination in product(characters, repeat=length):
                f.write(''.join(combination) + '\n')

generate_combinations()
