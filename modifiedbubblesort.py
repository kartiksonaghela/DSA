def modifiedsort(unsorted_list):
    
    for i  in range(1,len(unsorted_list)):
        flag=False
        for j in range(len(unsorted_list)-1):
            if unsorted_list[j]>unsorted_list[j+1]:
                unsorted_list[j],unsorted_list[j+1]=unsorted_list[j+1],unsorted_list[j]
                flag=True
        if flag==False:
            break
    return unsorted_list
final_list=modifiedsort([2,1,9,4,6,3])
print("Sorted List: ",final_list)