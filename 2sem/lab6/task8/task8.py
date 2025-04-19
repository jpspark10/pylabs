import argparse
import sys

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('params', nargs='*')
ns = parser.parse_args()
p = ns.params

try:
    ints = [int(x) for x in p]
    if len(ints) == 0:
        print("NO PARAMS")
    elif len(ints) == 1:
        print("TOO FEW PARAMS")
    elif len(ints) > 2:
        print("TOO MANY PARAMS")
    else:
        print(ints[0] + ints[1])
except Exception as e:
    print(e.__class__.__name__)
