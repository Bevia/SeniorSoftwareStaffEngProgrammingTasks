def find_target(array, target):
    n = len(array)
    for i in range(n):
        if array[i] == target:
            return i
    return -1


def main():
    array = [1, 3, 5, 7, 9, 12, 21]
    target = 12

    result = find_target(array, target)

    if result != -1:
        print(f"index found of {target}: {result} ")
    else:
        print(f"not found")


if __name__ == "__main__":
    main()
