def partial_sums(*args):
    result = [0]
    for i in range(len(args)):
        result.append(result[-1] + args[i])
    return result


if __name__ == "__main__":
    print(partial_sums(1, 0.5, 0.25, 0.125))
