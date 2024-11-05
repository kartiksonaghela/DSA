def selectionsort(unsorted_list):
    n=len(unsorted_list)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if unsorted_list[j]<unsorted_list[min_index]:
                min_index=j
        unsorted_list[i],unsorted_list[min_index]=unsorted_list[min_index],unsorted_list[i]
    return unsorted_list
final_list=selectionsort([2,1,9,4,6,3])
print("Sorted List: ",final_list)
            
