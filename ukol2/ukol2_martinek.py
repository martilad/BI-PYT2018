import argparse, random, os, sys, logging

from time import sleep

def p(*args):
    print(*args, end='', sep='', flush = True)

class color:
   PURPLE = '\033[105m'
   CYAN = '\033[106m'
   BLUE = '\033[104m'
   GREEN = '\033[102m'
   YELLOW = '\033[103m'
   RED = '\033[101m'
   END = '\033[0m'

def get_color_for_count(X):
    if X <= 2:
        return color.YELLOW
    if X <= 4:
        return color.CYAN
    if X <= 6:
        return color.GREEN
    if X <= 10:
        return color.RED
    if X <= 20:
        return color.PURPLE
    else:
        return color.BLUE

class Browns_move:
    def __init__(self,rows, cols, speed, wait):
        self.history = []
        if wait <= 0.1 or wait > 200 :
            wait = 50;
        self.wait = 1 / wait
        self.rows = rows
        self.cols = cols
        self.speed = speed
        self.history.append((rows, cols))
        self.kill = False
        if self.speed < 1:
            self.speed = 1
        self.window = [[0 for x in range(int(cols))] for y in range(int(rows))]

    def start(self, row, col):
        if row < 5 or row > int(self.rows)-5 or col < 5 or col > int(self.cols)-5:
            self.start_middle()
        self.clean()
        self.set_position(rows=row, cols=col)
        self.move()

    def set_position(self, rows, cols):
        self.possitionX = int(cols)
        self.possitionY = int(rows)
        p("\x1b[{row};{col}H".format(row=self.possitionY, col=self.possitionX))

    def start_middle(self):
        self.clean()
        self.set_position(rows=int(self.rows)/2, cols=int(self.cols)/2)
        self.move()

    def clean(self):
        p('\x1b[?25l\x1b[2J\x1b[0H')

    def move(self):
        while True:
            if self.kill:
                break
            self.window[self.possitionY][self.possitionX] += 1
            self.history.append((self.possitionY,self.possitionX))
            p(get_color_for_count(self.window[self.possitionY][self.possitionX])," \033[1D",color.END)
            sleep(self.wait)
            x,y = self.gen_direction()
            self.possitionY += y
            self.possitionX += x
            if self.check_end():
                self.save_file()
                self.end_info()
            self.set_position(self.possitionY, self.possitionX)

    def gen_direction(self):
        return random.randint(-1, 1)*self.gen_speed(), random.randint(-1,1)*self.gen_speed()

    def gen_speed(self):
        return random.randint(1, self.speed)

    def check_end(self):
        if self.possitionY <= 1:
            self.set_position(rows=0, cols=self.possitionX)
            self.history.append((0, self.possitionX))
            p(color.YELLOW, " \033[1D")
            p(color.END)
            return True

        if self.possitionY >= int(self.rows):
            self.set_position(rows=self.rows, cols=self.possitionX)
            self.history.append((self.rows, self.possitionX))
            p(color.YELLOW, " \033[1D")
            p(color.END)
            return True

        if self.possitionX <= 1:
            self.set_position(rows=self.possitionY, cols=0)
            self.history.append((self.possitionY, 0))
            p(color.YELLOW, " \033[1D")
            p(color.END)
            return True

        if self.possitionX >= int(self.cols):
            self.set_position(rows=self.possitionY, cols=self.cols)
            self.history.append((self.possitionY, self.cols))
            p(color.YELLOW, " \033[1D")
            p(color.END)
            return True
        return False

    def save_file(self):
        f = open('save.txt', 'w')
        for i in self.history:
            x,y = i
            f.write(str(x))
            f.write(",")
            f.write(str(y))
            f.write("\n")
        f.close()

    def end_info(self):
        input("")
        self.kill = True
        return

class Browns_read:
    def __init__(self,file, wait):
        self.f = open(file, 'r')
        if wait <= 0.1 or wait > 200 :
            wait = 50;
        self.wait = 1 / wait
        a,b = self.f.readline().split(",")
        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=a, cols=b))

    def start(self, row, col):

        p("hovno")



parser=argparse.ArgumentParser("Browns move")
parser.add_argument("-l", help='File name for load Browns move.')
parser.add_argument("-p", type=int, nargs=2, help='Position to start.')
parser.add_argument("-s", type=int, help='Maximum random step.')
parser.add_argument("-t", type=float, help='How fast do steps. 1 for one step for one second.')
args = parser.parse_args()
logging.basicConfig(filename='example.log',level=logging.DEBUG)
if args.l:
    move = Browns_read(file = args.l, wait=args.t if args.t else 50)


else:
    rows, columns = os.popen('stty size', 'r').read().split()
    move = Browns_move(rows=rows, cols=columns, speed=args.s if args.s else 1, wait=args.t if args.t else 50)
    if args.p:
        move.start(args.p[0], args.p[1])
    else:
        move.start_middle()
exit(1)


