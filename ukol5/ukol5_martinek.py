import argparse, random, os, sys, logging
import numpy as np




class Cell_live:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print ("cell live start")
        zoom = np.random.choice(np.arange(0, 2), size = (x, y), p=[0.3, 0.7])
        self.array = np.zeros((x+2, y+2), dtype=int)
        self.array[1:-1,1:-1] = self.array[1:-1,1:-1] + zoom
        self.p('\x1b[?25l\x1b[2J\x1b[0H')

    def print_state_on_terminal(self):
        x = 0
        y = 0
        for i in self.array[1:-1,1:-1]:
            y = 0
            for j in i:
                if (x == 0 or y == 0 or x==self.x-1 or self.y-1 ==y):
                        self.set_position(x+1,y+1)
                        self.p("X")
                else:
                    if (j == 1):
                        self.set_position(x+1,y+1)
                        self.p("1")
                    if (j == 0):
                        self.set_position(x+1,y+1)
                        self.p("0")
                y += 1
            x += 1

    """Set position in terminal."""
    def set_position(self, rows, cols):
        self.p("\x1b[{row};{col}H".format(row=rows, col=cols))

    """Print for painting on terminal :D"""
    def p(self, *args):
        print(*args, end='', sep='', flush = True)

    def __del__(self):
        input("")
        self.p('\033[?25h')



parser=argparse.ArgumentParser("Cell live simulator")
parser.add_argument("-p", type=int, help='Percent cels on start.', default=10)
parser.add_argument("-o", type=int, help='How ofter print the situation.', required=True)
parser.add_argument("-m", type=int, help='Maximum generations.', required=True)
args = parser.parse_args()


rows, columns = os.popen('stty size', 'r').read().split()
live = Cell_live(int(rows),int(columns))
live.print_state_on_terminal()



import numpy as np

def iterate_2(Z):
    # Count neighbours
    N = (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +
         Z[1:-1,0:-2]                + Z[1:-1,2:] +
         Z[2:  ,0:-2] + Z[2:  ,1:-1] + Z[2:  ,2:])

    # Apply rules
    birth = (N==3) & (Z[1:-1,1:-1]==0)
    survive = ((N==2) | (N==3)) & (Z[1:-1,1:-1]==1)
    Z[...] = 0
    Z[1:-1,1:-1]= Z[1:-1,1:-1] | birth | survive
    return Z


Z = np.array([[0,0,0,0,0,0],
              [0,0,0,1,0,0],
              [0,1,0,1,0,0],
              [0,0,1,1,0,0],
              [0,0,0,0,0,0],
              [0,0,0,0,0,0]])

#print (Z)
for i in range(100): iterate_2(Z)
#print (Z)
