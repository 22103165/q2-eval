def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def reverse_string(s):
    return s[::-1]

def main():
    user_input = input("Enter a sorted list of integers separated by spaces: ")
    arr = list(map(int, user_input.split()))
    
    target = int(input("Enter the target value to search for: "))
    
    index = binary_search(arr, target)
    
    if index == -1:
        print("The target value was not found in the list.")
    else:
        print(f"Target value found at index: {index}")
        
        reversed_index = reverse_string(str(index))
        print(f"Reversed index value: {reversed_index}")

if __name__ == "__main__":
    main()



