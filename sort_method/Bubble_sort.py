def bubble_sort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

    return l

l=[32,1,5,44,23,67,21]
result_l=bubble_sort(l)
print(result_l)
