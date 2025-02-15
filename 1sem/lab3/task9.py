def task_nine():
    n = int(input())
    candidates = {}

    for _ in range(n):
        candidate, votes_count = input().split()
        votes_count = int(votes_count)

        if candidate in candidates:
            candidates[candidate] += votes_count
        else:
            candidates[candidate] = votes_count

    for _candidate in candidates:
        print(_candidate, candidates[_candidate])


if __name__ == "__main__":
    task_nine()
