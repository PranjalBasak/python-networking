#!/home/calypse/repos/python-networking/codes/bin/python3

import argparse

# Create A Parser Object
parser = argparse.ArgumentParser(description = "A Basic Echo Program")

# Add an argument
parser.add_argument("echo", nargs="*", metavar="msg", help="You will get an echo")
args = parser.parse_args()

# Check if the echo argument has any input data
if len(args.echo):
	output = "$$".join(args.echo)
	print(output)