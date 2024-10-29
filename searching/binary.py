from typing import List, Optional


def binary_search(arr: List[int], target: int) -> Optional[int]:
    left, right = 0, len(arr) - 1
    while left <= right:
        # left + (right - left) // 2 is safer because it avoids the risk of exceeding integer limits.
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


def recursive_binary_search(arr: List[int], target: int, left: int, right: int) -> Optional[int]:
    if left > right:
        return None  # Base case: target not found

    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    else:
        return recursive_binary_search(arr, target, left, mid - 1)


def main():
    # arr = [1, 3, 5, 7, 9, 11]
    arr = [10, 3, 6, 15, 8]
    arr.sort()
    print("Sorted array:", arr)
    target = 8

    # result = binary_search(arr, target)
    result = recursive_binary_search(arr, target, 0, len(arr) - 1)
    if result is not None:
        print(f"Found at index: {result}")
    else:
        print("Not found")


# Run the main function only if this script is executed (not imported)
if __name__ == "__main__":
    main()
