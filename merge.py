def merge_sort(unsorted_list):
    if len(unsorted_list)>1:
        mid=len(unsorted_list)//2
        leftlist=unsorted_list[:mid]
        rightlist=unsorted_list[mid:]
        merge_sort(leftlist)
        merge_sort(rightlist)
        i=j=k=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                unsorted_list[k]=leftlist[i]
                i+=1
            else:
                unsorted_list[k]=rightlist[j]
                j+=1
            k+=1
        while i<len(leftlist):
            unsorted_list[k]=leftlist[i]
            i+=1
            k+=1
        while j<len(rightlist):
            unsorted_list[k]=rightlist[j]
            j+=1
            k+=1
    return unsorted_list
print(merge_sort([10,3,4,5,1,20,30]))