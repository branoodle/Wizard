import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument("-f","--file", help="fichier auxquelle on doit modifier le magic header", required=True)
parser.add_argument("-m", "--magic", help="magic number à choisir (jpg,png,gif)", required=True)
parser.add_argument("-o", "--output", help="output file", required=True)
args = parser.parse_args()

if args.magic == "jpg":
	magic = bytearray([
			0xFF, 
			0xD8, 
			0xFF, 
			0xE0, 
			0x00, 
			0x10, 
			0x4A, 
			0x46, 
			0x49, 
			0x46, 
			0x00, 
			0X01,
	])
	with open(args.file, "rb") as h:
		contenue = h.read()
	with open(args.output, "wb") as h:
		h.write(magic + contenue)
elif args.magic == "png":
	magic = bytearray([

			0x89, 
			0x50, 
			0x4E, 
			0x47, 
			0x0D, 
			0x0A, 
			0x1A, 
			0x0A,
		])
	with open(args.file, "rb") as h:
		contenue = h.read()
	with open(args.output, "wb") as h:
		h.write(magic + contenue)
elif args.magic == "gif":
	magic = bytearray([
		0x47, 
		0x49, 
		0x46, 
		0x38, 
		0x37, 
		0x61,
		])
	with open(args.file, "rb") as h:
		contenue = h.read()
	with open(args.output, "wb") as h:
		h.write(magic + contenue)
