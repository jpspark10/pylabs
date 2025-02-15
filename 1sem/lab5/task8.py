def print_operation_table(operation, num_rows=9, num_columns=9):
    for row in range(1, num_rows + 1):
        table_row = [operation(row, col) for col in range(1, num_columns + 1)]
        print(*table_row)


if __name__ == "__main__":
    print_operation_table(lambda x, y: x * y)
    print("-" * 10)
    print_operation_table(lambda x, y: x * y, 5)
