def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Corrected variable name
    target =   4# Changed x to target for clarity
    result = binary_search(arr, target)  # Call the binary_search function
    print(result)  # Print the result

# Call the main function
main()