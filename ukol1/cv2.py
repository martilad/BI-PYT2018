import sys
import os

def is_prime(a):
    return all(a % i for i in range(2, a))

def up (shift = 1):
    print("\033[" + str(shift) + "A", sep='', end='')

def down (shift = 1):
    print("\033[" + str(shift) + "B", sep='', end='')

def right (shift = 1):
    print("\033[" + str(shift) + "C", sep='', end='')

def left (shift = 1):
    print("\033[" + str(shift) + "D", sep='', end='')

def print_number_pos(number, size, empty_fill = " "):
    number = str(number)
    if len(number) > size: number = number[:size]
    number = number.center(size, empty_fill)
    return number

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

def print_sift(direction, str_len, number_dash):
    if direction%4 == 1: 
        up()
        left(str_len)
    if direction%4 == 2: 
        left(str_len+number_dash)
    if direction%4 == 3: 
        down()
        left(str_len)

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
for i in range(x):
    print("\033[30m\033[106m", 
            print_number_pos(number=i+1, size=str_len),
            "\033[0m", sep='', end='') if is_prime(i+1) else print("\033[30m\033[103m",
                                                                print_number_pos(number=i+1, size=str_len),
                                                                "\033[0m", sep='', end='')
    if i==x-1:
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
