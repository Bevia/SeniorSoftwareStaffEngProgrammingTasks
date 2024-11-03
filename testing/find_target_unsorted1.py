def find_target(array, target):
    for index, value in enumerate(array):
        if value == target:
            return index
    return -1


def main():
    array = [6, 1, 7, 3, 8, 4, 12]
    target = 7

    result = find_target(array, target)

    if target != -1:
        print(f"value for {target}: {result}")
    else:
        print(f"not found")


if __name__ == "__main__":
    main()
