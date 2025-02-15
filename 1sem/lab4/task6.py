def is_valid_brackets(sequence):
    brackets = {')': '('}
    stack = []

    for char in sequence:
        if char in brackets:
            if stack and stack[-1] == brackets[char]:
                stack.pop()
            else:
                return "NO"
        elif char in brackets.values():
            stack.append(char)

    return "YES" if not stack else "NO"


if __name__ == "__main__":
    print(is_valid_brackets("()"))
    print(is_valid_brackets("(()(("))
