import sys
import os
__author__ = "Ladislav Martínek"
""" Check if is number is a prime number."""
def is_prime(a):
    return all(a % i for i in range(2, a))

""" Moves the cursor one position up."""
def up (shift = 1):
    print("\033[" + str(shift) + "A", sep='', end='')

""" Moves the cursor one position down."""
def down (shift = 1):
    print("\033[" + str(shift) + "B", sep='', end='')

""" Moves the cursor one position right."""
def right (shift = 1):
    print("\033[" + str(shift) + "C", sep='', end='')

""" Moves the cursor one position left."""
def left (shift = 1):
    print("\033[" + str(shift) + "D", sep='', end='')

""" Return string number on given size fill by given character."""
def print_number_pos(number, size, empty_fill = " "):
    number = str(number)
    if len(number) > size: number = number[:size]
    number = number.center(size, empty_fill)
    return number

""" Print character between numbers on given size."""
def print_special(direction, str_len, number_dash):
    if direction%4 == 0:
        print("-"*number_dash, sep='', end='')
    elif direction%4 == 1: 
        print("|".center(str_len), sep='', end='')
    elif direction%4 == 2:
        print("-"*number_dash, sep='', end='')
        left(str_len+number_dash)
        return
    elif direction%4 == 3:
        print("|".center(str_len), sep='', end='')
    print_sift(direction=direction, str_len=str_len, number_dash=number_dash)

""" Print specific move after print some number. """
def print_sift(direction, str_len, number_dash):
    if direction%4 == 1: 
        up()
        left(str_len)
    if direction%4 == 2: 
        left(str_len+number_dash)
    if direction%4 == 3: 
        down()
        left(str_len)

""" Count the maximum count of number to terminal.
    TO DO: remake accurately and clearly."""
def max_number(rows, cols, str_len, number_dash = 2):
    numbers = 1
    r=1
    s=3
    c=1
    while True:
        numbers += 2*s + 2*s - 4
        r += 4
        c += str_len*2 + number_dash*2
        if r > rows-3 or c > cols-3:
            numbers -= 2*s + 2*s - 4
            return numbers
        s += 2
""" Parse argumnets, size of numbers, move cursor and clear terminal."""
try:
    script, x = sys.argv
except:
    exit(1)
cols, rows = os.get_terminal_size()
x = int(x)
print ('\x1b[2J\x1b[0H\033[' +  str(rows//2+1) + 'B\033[' +  str(cols//2) + 'C', end='')
direction = 0
step = 1
decrement = 1
increment_step = False
str_len = len(str(x))
if str_len <= 2: number_dash = 2
else: number_dash = 1
if x > max_number(rows, cols, str_len):
    x = max_number(rows, cols, str_len)
""" Heres the magic :D
The direction of the rendering is changed after exactly given steps that grow linearly.
The number of numbers required must be plotted in each direction.
Decrement is number witch represents the number of print numbers.

5-4-3       
|   |       If i print the line of number of number in one direction.
6 1-2       <number_in_one_direction>:<direction>_... (Direction chars use same as in ANSII escape chars)
|           1:C_1:A_2:D_2:B_3:C_3:A...
7-8-9-...   I incremet step every two iteration help incremnt_step which has boolean values.
            I set decrement to step and decrement in every iteration. While decrement != 1 only print numbers
if decrement is 1 I am in the end of line. Deckrement is set to step. And if is odd round increment_step = True, 
else increment step and set increment_step = False.
"""
for i in range(x):
    print("\033[30m\033[106m",
          print_number_pos(number=i+1, size=str_len),
          "\033[0m", sep='', end='') if is_prime(i+1) else print("\033[30m\033[103m",
                                                                 print_number_pos(number=i+1, size=str_len),
                                                                 "\033[0m", sep='', end='')
    if i == x-1:
        print('\x1b[0H\033[' +  str(rows) + 'B')
        break
    print_sift(direction=direction, str_len=str_len, number_dash=number_dash)
    if decrement > 1:
        print_special(direction=direction, str_len=str_len, number_dash=number_dash)
        decrement -= 1
        continue
    if decrement == 1:
        print_special(direction=direction, str_len=str_len, number_dash=number_dash)
        direction += 1
        if not increment_step:
            increment_step = True
            decrement = step
            continue
        step += 1
        decrement = step
        increment_step = False
