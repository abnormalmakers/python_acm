l=[233,456,2,11,56,3,43]

def quick_sort(l):
    if len(l)<2:
        return l
    else:
        temp=l[0]
        less=[i for i in l[1:] if i<=temp]
        more=[i for i in l[1:] if i>temp]
        return quick_sort(less)+[temp]+quick_sort(more)

result_l=quick_sort(l)
print(result_l)
