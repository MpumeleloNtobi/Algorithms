class List:
    def __init__(self):
        self.list = []

    # Append to list
    def append(self, data):
        self.list.append(data)

    # Clear list
    def clear(self):
        self.list.clear()

    # Sort list using the bubble sort method
    def bubble_sort(self):
        def sort(arr):
            # Base case
            if len(arr) == 1:
                return

            # Recursive case
            for i in range(len(arr)-1):
                if arr[i+1] < arr[i]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    self.list[:len(arr)] = arr
                    print(self.list)
            
            sort(arr[:-1])

        # Call the sort function
        sort(self.list)

# Testing 
list_to_sort = List()
arr = [5, 2, 7, 4, 1, 6, 3, 0]
for element in arr:
    list_to_sort.append(element)

list_to_sort.bubble_sort()