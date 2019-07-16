import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--directory" , help="Directory Name")
parser.add_argument("--filename" , help="File Name")

#parser.add_argument("square" , help="Display the square of a given number" , type=int)

parser.add_argument("-v","--verbose", help="Increase output verbosity"  , action="count")

args = parser.parse_args()

#print(args)

if args.verbose == 1:
    print("ONE")
elif args.verbose == 2:
    print("TWO")
elif args.verbose == 3:
    print("Three")
