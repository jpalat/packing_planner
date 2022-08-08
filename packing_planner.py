#packing_planner

import argparse
import os
import sys

#create the parser
parser = argparse.ArgumentParser()
parser.add_argument('Path', 
        metavar='path', 
        type=str, 
        help='path to list')

args = parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))
