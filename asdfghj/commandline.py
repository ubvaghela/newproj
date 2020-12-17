import argparse
import sys

def calc(args):
	if args.o == 'add':
		return args.x + args.y

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--x',type=float,default=1.0,help="Number 1")
	parser.add_argument('--y',type=float,default=3.0,help="Number 2")
	parser.add_argument('--o',type=str,default="Add",help="Number Calculation")

args = parser.parse_args()

sys.stdout.write(str(calc(args)))
