import argparse

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('args', nargs='*')
ns = parser.parse_args()
if not ns.args:
    print("no args")
else:
    for a in ns.args:
        print(a)
