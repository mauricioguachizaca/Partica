class QuickSort:
    def sort_primitive_ascendent(self, array):
        if len(array) <= 1:
            return array
        else:
            pivot = array[len(array) // 2]
            items_lower = [item for item in array if item < pivot]
            items_equal = [item for item in array if item == pivot]
            items_greater = [item for item in array if item > pivot]
            return self.sort_primitive_ascendent(items_lower) + items_equal + self.sort_primitive_ascendent(items_greater)

    def sort_primitive_descendent(self, array):
        if len(array) <= 1:
            return array
        else:
            pivot = array[len(array) // 2]
            items_lower = [item for item in array if item > pivot]
            items_equal = [item for item in array if item == pivot]
            items_greater = [item for item in array if item < pivot]
            return self.sort_primitive_descendent(items_lower) + items_equal + self.sort_primitive_descendent(items_greater)
    
    def sort_models_ascendent(self, array, attribute):
        if len(array) <= 1:
            return array
        else:
            pivot = array[len(array) // 2]
            items_lower = [item for item in array if getattr(item, attribute) < getattr(pivot, attribute)]
            items_equal = [item for item in array if getattr(item, attribute) == getattr(pivot, attribute)]
            items_greater = [item for item in array if getattr(item, attribute) > getattr(pivot, attribute)]
            return self.sort_models_ascendent(items_lower, attribute) + items_equal + self.sort_models_ascendent(items_greater, attribute)
    
    def sort_models_descendent(self, array, attribute):
        if len(array) <= 1:
            return array
        else:
            pivot = array[len(array) // 2]
            items_lower = [item for item in array if getattr(item, attribute) > getattr(pivot, attribute)]
            items_equal = [item for item in array if getattr(item, attribute) == getattr(pivot, attribute)]
            items_greater = [item for item in array if getattr(item, attribute) < getattr(pivot, attribute)]
            return self.sort_models_descendent(items_lower, attribute) + items_equal + self.sort_models_descendent(items_greater, attribute)
