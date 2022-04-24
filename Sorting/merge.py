class List:
    def __init__(self):
        self.list = []

    # Append to list
    def append(self, data):
        self.list.append(data)

    # Clear list
    def clear(self):
        self.list.clear()

    # Sort list using the merge sort method
    def merge_sort(self):
        def sort(arr):
            # Base case
            if len(arr) == 1:
                return

            # Recursive case
            middle_index = len(arr)//2

            # Split the list into half
            left = arr[:middle_index]
            right = arr[middle_index:]

            # Sort both halves separately
            sort(left)
            sort(right)
  
            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
  
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
  
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        # Call the sort function
        sort(self.list)
        print(self.list)

# Testing 
list_to_sort = List()
arr = [5, 2, 7, 4, 1, 6, 3, 0]
for element in arr:
    list_to_sort.append(element)

list_to_sort.merge_sort()