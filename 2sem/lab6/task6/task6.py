import sys


def parse_args(args):
    sort = False
    if '--sort' in args:
        sort = True
        args.remove('--sort')

    key_value_pairs = []
    for arg in args:
        if '=' in arg:
            key, value = arg.split('=', 1)
            key_value_pairs.append((key, value))

    if sort:
        key_value_pairs.sort(key=lambda x: x[0])

    return key_value_pairs


def print_key_values(pairs):
    for key, value in pairs:
        print(f"Key: {key} Value: {value}")


def main():
    args = sys.argv[1:]
    parsed_pairs = parse_args(args)
    print_key_values(parsed_pairs)


if __name__ == '__main__':
    main()
