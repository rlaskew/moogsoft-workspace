#!/usr/bin/env python3

# from https://docs.python.org/3/howto/argparse.html
import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("echo")
parser.add_argument("square", help="display a square of a given number", type=int)
parser.add_argument("cubed", help="display cubed of a given number", type=int)
args = parser.parse_args()
#print(args.echo)
#print(args.square**2)
