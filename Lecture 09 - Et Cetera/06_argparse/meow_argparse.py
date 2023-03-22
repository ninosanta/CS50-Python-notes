import argparse

parser = argparse.ArgumentParser(  # constructor for the parser object
    description="Meow like a cat"
)
parser.add_argument(
    "-n",  # parameter name
    help="Number of times to meow",  # parameter description in the help
    default=1,  # default value
    type=int  # automatically convert the argument to an int
)
args = parser.parse_args()  # parser will look automatically at sys.argv

for _ in range(
    args.n  # contains the integer that the user typed afert "-n "
):
    print("meow")

# try to executre this script with:
#       python meow_argparse.py -h 
# or: 
#       python meow_argparse.py -help