def binary_search(array, target):
    left, right = 0, len(array)-1

    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            """Returns the index of 'target' in 'arr', or None if not found."""
    return None

def main():
    array = [1, 3, 4, 7, 11, 32]
    target = 3

    result = binary_search(array, target)

    if result is not None:
        print(f"binary search index for value {target}: {result}")
    else:
        print(f"not found")


if __name__ == "__main__":
    main()



