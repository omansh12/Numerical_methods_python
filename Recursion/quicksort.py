def quicksort(lst):
    if len(lst) <= 1:
        sorted_list = lst

    else:

        pivot = lst[0]

        bigger = []
        smaller = []
        same = []

        for i in lst:
            if i > pivot:
                bigger.append(i)
            elif i < pivot:
                smaller.append(i)
            else:
                same.append(i)
        bigger = quicksort(bigger)
        smaller = quicksort(smaller)
        
        sorted_list = smaller + same + bigger
    
    return sorted_list

print(quicksort([5, 4, 9, 64, 16]))