def quick_sort(unsorted_list):
    if len(unsorted_list)<=1:
        return unsorted_list
    else:
        pivot=unsorted_list[0]
        lesser_values=[x for x in unsorted_list[1:] if x<=pivot]
        greater_values=[x for x in unsorted_list[1:] if x>pivot]
        return quick_sort(lesser_values)+[pivot]+quick_sort(greater_values)
print(quick_sort([10,5,2,3,25,15]))