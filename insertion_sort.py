def insertion_sort_decreasing(arr):
    """
    Sorts an array in monotonically decreasing order using insertion sort.
    
    Args:
        arr (list): The array to be sorted
        
    Returns:
        list: The sorted array in decreasing order
    """
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Store the current element to be inserted
        key = arr[i]
        
        # Find the correct position for the key in the sorted portion
        j = i - 1
        
        # Move elements that are smaller than key one position ahead
        # (for decreasing order, we move smaller elements to the right)
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key in its correct position
        arr[j + 1] = key
    
    return arr


def print_array(arr, message=""):
    """
    Helper function to print an array with an optional message.
    
    Args:
        arr (list): The array to print
        message (str): Optional message to display before the array
    """
    if message:
        print(f"{message}: {arr}")
    else:
        print(arr)


def main():
    """
    Main function to demonstrate the insertion sort algorithm.
    """
    print("Insertion Sort Algorithm - Monotonically Decreasing Order")
    print("=" * 55)
    
    # Test cases
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1],
        [],
        [3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    for i, arr in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print_array(arr, "Original array")
        
        if arr:  # Only sort if array is not empty
            sorted_arr = insertion_sort_decreasing(arr.copy())
            print_array(sorted_arr, "Sorted array (decreasing)")
        else:
            print("Empty array - no sorting needed")
        
        print("-" * 40)


if __name__ == "__main__":
    main()
