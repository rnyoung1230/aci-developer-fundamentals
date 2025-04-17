"""
Render an ASCII art pyramid with N levels by printing N rows of asterisks, where the top row
has a single asterisk in the center and each successive row has two additional asterisks on either side.
"""

def generate_pyramid(num_rows):
    print(f'Creating pyramid for {num_rows} rows...')
    print_char = "*"
    for i in range(num_rows):
        print(print_char.rjust(num_rows+i))
        print_char += '**'


generate_pyramid(10)