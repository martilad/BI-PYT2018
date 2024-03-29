import argparse, random, os, sys, logging
import numpy as np
from time import sleep




class Cell_live:

    def __init__(self, x, y, probability_ones, file_save = 0):
        self.x = x-1
        self.y = y
        self.probability_ones = probability_ones
        print ("cell live start")
        self.gen_random_state(self.probability_ones)
        self.p('\x1b[?25l\x1b[2J\x1b[0H')
        self.write = False
        if file_save != 0:
            self.to_save = open(file_save, 'w')
            self.to_save.write(str(x) + " " + str(y) + "\n")
            self.write = True


    def gen_random_state(self, probability_ones):
        zoom = np.random.choice(np.arange(0, 2), size = (self.x, self.y), p=[1-probability_ones, probability_ones])
        self.array = np.zeros((self.x+2, self.y+2), dtype=int)
        self.array[1:-1,1:-1] = self.array[1:-1,1:-1] + zoom

    def print_state_on_terminal(self, generation_number):
        self.p('\x1b[?25l\x1b[2J\x1b[0H')
        self.p("Generation number = ", generation_number)
        self.to_save.write("Generation number = " + str(generation_number) + "\n")
        x = 1
        y = 0
        for i in self.array[1:-1,1:-1]:
            y = 0
            for j in i:
                if self.write: self.to_save.write(str(j))
                if (j == 1):
                    self.set_position(x+1,y+1)
                    self.p("\033[102m \033[0m")
                y += 1
            if self.write: self.to_save.write("\n")
            x += 1

    def iterate(self):
        # Count neighbours
        count = (self.array[0:-2,0:-2] + self.array[0:-2,1:-1] + self.array[0:-2,2:] +      #first line
                    self.array[1:-1,0:-2] + self.array[1:-1,2:] +                           #secount without the point
                    self.array[2:,0:-2] + self.array[2:,1:-1] + self.array[2:,2:])    #third bottom last all like church in carcasone :D

        # Apply rules
        birth = (count==3) & (self.array[1:-1,1:-1]==0)
        survive = ((count==2) | (count==3)) & (self.array[1:-1,1:-1]==1)
        self.array[...] = 0
        self.array[1:-1,1:-1]= self.array[1:-1,1:-1] | birth | survive

    def start_game(self, iteration, often_print):
        for i in range(iteration+1):
            if i % often_print == 0:
                sleep(0.1)
                self.print_state_on_terminal(i)
            self.iterate()
            
      

    """Set position in terminal."""
    def set_position(self, rows, cols):
        self.p("\x1b[{row};{col}H".format(row=rows, col=cols))

    """Print for painting on terminal :D"""
    def p(self, *args):
        print(*args, end='', sep='', flush = True)

    def __del__(self):
        input("")
        self.p('\033[?25h')
        if self.write: self.to_save.close()


class Load():

    def __init__(self,file):
        self.f = open(file, 'r')
        a,b = self.f.readline().split(" ")
        self.rows = a
        self.colums = b
        #a = str(int(a)+1)
        #b = str(int(b)+1)
        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=a, cols=b))
        self.clean()

    def __del__(self):
        input("")
        print('\033[?25h')

    """Print for painting on terminal :D"""
    def p(self, *args):
        print(*args, end='', sep='', flush = True)

    """Cleand terminal."""
    def clean(self):
        self.p('\x1b[?25l\x1b[2J\x1b[0H')

    """Set position in terminal."""
    def set_position(self, rows, cols):
        self.p("\x1b[{row};{col}H".format(row=rows, col=cols))

    """Start loading with speed."""
    def start(self):
        while True:
            chunk = self.f.readline()
            if chunk == '':
                break
            self.set_position(1,1)
            self.p(chunk)
            self.set_position(2,1)
            for i in range(int(self.rows)-1):
                chunk = self.f.readline()
                for i in chunk[:-1]:
                    if i == '0':
                        self.p(" ")
                    else:
                        self.p(0)
            sleep(1) 
             



parser=argparse.ArgumentParser("Cell live simulator")
parser.add_argument("-p", type=int, help='Percent cels on start.', default=10)
parser.add_argument("-o", type=int, help='How ofter print the situation.', default=1)
parser.add_argument("-m", type=int, help='Maximum generations.', default=10)
parser.add_argument("-f", help='File to save.')
parser.add_argument("-l", help='File to load.')
args = parser.parse_args()

if args.l:
    live = Load(args.l)
    live.start()
else:
    rows, columns = os.popen('stty size', 'r').read().split()
    live = Cell_live(int(rows),int(columns), int(args.p)/100,args.f if args.f else 0 )
    live.start_game(args.m, args.o)

