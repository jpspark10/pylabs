def task_ten():
    operation_map = {
        "read": "R",
        "write": "W",
        "execute": "X"
    }

    files_count = int(input())
    permissions = {}

    for _ in range(files_count):
        line = input().strip().split()
        file_name = line[0]
        file_permissions = set(line[1:])
        permissions[file_name] = file_permissions

    request_result = []

    request_count = int(input())
    for _ in range(request_count):
        action, file_name = input().strip().split()
        if file_name in permissions and operation_map[action] in permissions[file_name]:
            request_result.append("OK")
        else:
            request_result.append("Access denied")

    for result in request_result:
        print(result)


if __name__ == "__main__":
    task_ten()
