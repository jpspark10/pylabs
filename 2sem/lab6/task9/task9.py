import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--sort', action='store_true')
parser.add_argument('pairs', nargs='*', help='ключ=значение')
ns = parser.parse_args()

items = []
for p in ns.pairs:
    if '=' in p:
        k, v = p.split('=', 1)
        items.append((k, v))
if ns.sort:
    items.sort(key=lambda x: x[0])
for k, v in items:
    print(f"Key: {k} Value: {v}")
