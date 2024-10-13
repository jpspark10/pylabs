friends = {}


def add_friends(name_of_person, list_of_friends):
    if name_of_person not in friends:
        friends[name_of_person] = set()
    friends[name_of_person].update(list_of_friends)


def are_friends(name_of_person1, name_of_person2):
    return name_of_person2 in friends.get(name_of_person1, set())


def print_friends(name_of_person):
    if name_of_person in friends:
        print(", ".join(friends[name_of_person]))
    else:
        print()


if __name__ == "__main__":
    add_friends("Alice", ["Bob", "Charlie", "Dean"])
    print(are_friends("Alice", "Bob"))  # True
    print(are_friends("Alice", "Eve"))  # False
    print_friends("Alice")  # Bob, Charlie, Dean
