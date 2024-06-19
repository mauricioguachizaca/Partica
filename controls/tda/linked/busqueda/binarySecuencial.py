
from controls.tda.linked.ordenacion.quickSort import QuickSort

class BinarySecuencial:

    def search_BinarySecuencial(self, array, element):
        quickSort = QuickSort()

        sorted_array = quickSort.sort_primitive_ascendent(array)
        
    
    def search_binary_models(self, array, element, attribute):
        quickSort = QuickSort()
        array = quickSort.sort_models_ascendent(array, attribute)
        left = 0
        right = len(array) - 1
        arr = []
        while left <= right:
            middle = (left + right) // 2
            middle_value = getattr(array[middle], attribute)  # Retrieve the attribute's value

            if middle_value == element:
                aux = middle
                while aux >= 0 and getattr(array[aux], attribute) == element:
                    arr.append(array[aux])
                    aux -= 1
                
                aux = middle +1
                while aux < len(array) and getattr(array[aux], attribute) == element:
                    arr.append(array[aux])
                    aux += 1
                return arr
        
            else:
                if element < middle_value:
                    right = middle - 1
                else:
                    left = middle + 1

        return aux  # Return aux if the elem
        
    
        
