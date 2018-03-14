import argparse, random, os, sys

def p(*args):
    print(*args, end='', sep='')

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Browns_move:
    def __init__(self,rows, cols, speed):
        self.rows = rows
        self.cols = cols
        self.speed = speed
        if self.speed < 1:
            self.speed = 1
        self.window = [[0 for x in range(int(cols))] for y in range(int(rows))]

    def start(self, row, col):
        self.clean()
        self.set_position(rows=row, cols=col)
        self.move()

    def set_position(self, rows, cols):
        p("\x1b[{row};{col}H".format(row=int(rows), col=int(cols)))

    def start_middle(self):
        self.clean()
        self.set_position(rows=int(self.rows)/2, cols=int(self.cols)/2)
        self.move()

    def clean(self):
        p('\x1b[?25l\x1b[2J\x1b[0H')

    def move(self):
        while True:
            p(self.gen_direction(), " ")
            p("Pohyb:")


            if self.check_end():
                self.save_file()
                self.end_info()

    def gen_direction(self):
        return random.randint(-1, 1)*self.gen_speed(), random.randint(-1,1)*self.gen_speed()

    def gen_speed(self):
        return random.randint(1, self.speed)

    def check_end(self):
        print("not implement")
        exit(1)

    def save_file(self):
        print("not implement")
        exit(1)

    def end_info(self):
        print("not implement")
        exit(1)

parser=argparse.ArgumentParser("Browns move")
parser.add_argument("-l", help='File name for load Browns move.')
parser.add_argument("-p", type=int, nargs=2, help='Position to start.')
parser.add_argument("-s", type=int, help='Maximum random speed.')
args = parser.parse_args()
if args.l:
    print("Read file borwns move. TO DO: later")
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=50, cols=50))
    exit(1)
else:
    rows, columns = os.popen('stty size', 'r').read().split()
    move = Browns_move(rows=rows, cols=columns, speed=args.s if args.s else 1)
    if args.p:
        move.start(args.p[0], args.p[1])
    else:
        move.start_middle()

    exit(1)


