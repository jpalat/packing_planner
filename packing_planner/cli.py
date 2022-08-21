#packing_planner

import argparse
import os
import sys

from .inventory import Item, Inventory
# from .funcmodule import my_function

def main():
    #create the parser
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()
    parser_inv = subparsers.add_parser('inventory', help='inventory help')
    sub_inventory = parser_inv.add_subparsers()
    si_add = sub_inventory.add_parser('add', help='Add inventory')
    si_add.add_argument('item')


    parser_plan = subparsers.add_parser('plan', help='plan help')
    parser_plan.add_argument('--name', type=str, help='name of the plan')

    parser_trip = subparsers.add_parser('trip', help='trip help')
    parser_trip.add_argument('--destination', help='trip destination.')
    parser_trip.add_argument('--start_date', help='trip start.')



    args = parser.parse_args()


    print(args)

if __name__ == '__main__':
    main()


