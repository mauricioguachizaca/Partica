import sys
import random
import time

# Agrega el directorio raíz del proyecto al sys.path
sys.path.append('..')  # Ajusta esta ruta según sea necesario

from controls.tda.linked.linkedList import LinkedList


def main():
    
    random_data = [random.randint(1, 25000) for _ in range(25000)]

    
    linked_list_quick = LinkedList()
    linked_list_merge = LinkedList()
    linked_list_shell = LinkedList()

    linked_list_quick.toList(random_data)
    linked_list_merge.toList(random_data)
    linked_list_shell.toList(random_data)

    #QuickSort
    start_time = time.time()
    linked_list_quick.sort(type=1, metodo=1) 
    quicksort_asc_time = time.time() - start_time

    start_time = time.time()
    linked_list_quick.sort(type=2, metodo=1)  
    quicksort_desc_time = time.time() - start_time

    #MergeSort
    start_time = time.time()
    linked_list_merge.sort(type=1, metodo=2) 
    mergesort_asc_time = time.time() - start_time

    start_time = time.time()
    linked_list_merge.sort(type=2, metodo=2)  
    mergesort_desc_time = time.time() - start_time

    # ShellSort
    start_time = time.time()
    linked_list_shell.sort(type=1, metodo=3) 
    shellsort_asc_time = time.time() - start_time

    start_time = time.time()
    linked_list_shell.sort(type=2, metodo=3)  
    shellsort_desc_time = time.time() - start_time

    # Print results
    print(f"QuickSort Ascending Time: {quicksort_asc_time:.6f} seconds")
    print(f"QuickSort Descending Time: {quicksort_desc_time:.6f} seconds")
    print(f"MergeSort Ascending Time: {mergesort_asc_time:.6f} seconds")
    print(f"MergeSort Descending Time: {mergesort_desc_time:.6f} seconds")
    print(f"ShellSort Ascending Time: {shellsort_asc_time:.6f} seconds")
    print(f"ShellSort Descending Time: {shellsort_desc_time:.6f} seconds")

if __name__ == "__main__":
    main()
