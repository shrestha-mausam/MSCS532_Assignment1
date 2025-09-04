# Insertion Sort Algorithm Implementation

## Project Overview
This project implements the Insertion Sort algorithm in Python, specifically designed to sort arrays in **monotonically decreasing order** (largest to smallest).

## Algorithm Description
Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

### How It Works
1. **Divide the array**: The algorithm divides the array into a sorted and unsorted region
2. **Iterate**: Starting from the second element, iterate through the unsorted region
3. **Compare and Shift**: For each element, compare it with elements in the sorted region
4. **Insert**: Place the element in its correct position within the sorted region

### Time Complexity
- **Best Case**: O(n) - when the array is already sorted in decreasing order
- **Average Case**: O(n²) - for random data
- **Worst Case**: O(n²) - when the array is sorted in ascending order

### Space Complexity
- **Space Complexity**: O(1) - in-place sorting algorithm

## Files in the Project

### `insertion_sort.py`
The main implementation file containing:
- `insertion_sort_decreasing(arr)`: Core sorting function
- `print_array(arr, message)`: Helper function for displaying arrays
- `main()`: Demonstration function with multiple test cases

## Usage

### Running the Program
```bash
python insertion_sort.py
```

### Example Output
```
Insertion Sort Algorithm - Monotonically Decreasing Order
=======================================================

Test Case 1:
Original array: [64, 34, 25, 12, 22, 11, 90]
Sorted array (decreasing): [90, 64, 34, 25, 22, 12, 11]
----------------------------------------

Test Case 2:
Original array: [5, 2, 4, 6, 1, 3]
Sorted array (decreasing): [6, 5, 4, 3, 2, 1]
----------------------------------------
```

### Using the Function in Your Code
```python
from insertion_sort import insertion_sort_decreasing

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = insertion_sort_decreasing(arr)
print(sorted_arr)  # Output: [90, 64, 34, 25, 22, 12, 11]
```

## Test Cases Included
The program includes comprehensive test cases covering:
1. **Mixed arrays** with various element orders
2. **Small arrays** for basic functionality verification
3. **Single element arrays** to test edge cases
4. **Empty arrays** to ensure proper handling
5. **Arrays with duplicate elements** to test stability
6. **Already sorted arrays** to test best-case performance

## Algorithm Implementation Details

### Key Features of the Decreasing Sort
- **Comparison Logic**: Uses `arr[j] < key` to maintain decreasing order
- **Shifting Strategy**: Shifts smaller elements to the right
- **In-place Sorting**: Modifies the original array without extra space
- **Stable Sorting**: Maintains relative order of equal elements

### Code Structure
```python
def insertion_sort_decreasing(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move smaller elements to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr
```

## Requirements
- Python 3.x
- No external dependencies required

## Author
Mausam Shrestha

## License
This project is part of an academic assignment for MSCS 532.
