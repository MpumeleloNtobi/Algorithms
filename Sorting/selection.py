class List:
    def __init__(self):
        self.list = []

    # Append to list
    def append(self, data):
        self.list.append(data)

    # Clear list
    def clear(self):
        self.list.clear()

    # Sort list using the selection sort method
    def selection_sort(self):
        for i in range(len(self.list)-1):
            smallest_value_index = i
            for j in range(i+1, len(self.list)):
                if self.list[j] < self.list[smallest_value_index]:
                    smallest_value_index = j
            self.list[i], self.list[smallest_value_index] = self.list[smallest_value_index], self.list[i]
            print(self.list)

# Testing 
list_to_sort = List()
arr = [5, 2, 7, 4, 1, 6, 3, 0]
for element in arr:
    list_to_sort.append(element)

list_to_sort.selection_sort()