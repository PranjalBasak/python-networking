#!/home/calypse/repos/python-networking/codes/bin/python3
import argparse

# First create a parser object
parser = argparse.ArgumentParser(description="ASCII Converter")
parser.add_argument("ascii", nargs=1, metavar="msg", help="Turns your string to a sequence of ascii values in decimal format")
parser.add_argument("-o", "--output", nargs=1, metavar="output file", help="Saves your output to a file specified")

# Parse the arguments 
args = parser.parse_args("ascii")

if len(args.ascii) == 1:
	s = args.ascii[0]
	#print(f"Testing: {s}")
	output_lst = [str(ord(c)) for c in s]
	#print(output_lst)
	output = " ".join(output_lst)
	if args.output:
		file_name = args.output[0]
		f = open(file_name, "w")
		f.write(f"{output}\n")
		print("Succesfully wrote to file:", file_name)
	else:
		print(output)
