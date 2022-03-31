import argparse
import os

my_parser = argparse.ArgumentParser(description="A docker image with two different tags")
my_parser.add_argument('--image', action='store', type=str, required=True)
my_parser.add_argument('--firstTag', action='store', type=str, required=True)
my_parser.add_argument('--secondTag', action='store', type=str, required=True)

args = my_parser.parse_args()

image = str(args.image)
firstTag = str(args.firstTag)
secondTag = str(args.secondTag)

syftCommandJson = 'syft -o json ' + image
sbom = os.system(syftCommandJson)

print(sbom)
