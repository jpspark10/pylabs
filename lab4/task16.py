def continue_fibonacci_sequence(sequence, n):
    if len(sequence) < 2:
        raise ValueError("err")

    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)


if __name__ == "__main__":
    sequence = [1, 1]
    continue_fibonacci_sequence(sequence, 1)
    print(*sequence)

    sequence = [1, 1, 2, 3, 5]
    continue_fibonacci_sequence(sequence, 0)
    print(*sequence)
