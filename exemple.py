import argparse
from labelizer import labelizer
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("image")
parser.add_argument("output")

args = parser.parse_args()

im = Image.open(args.image)

output = labelizer(im)

output.save(args.output)
