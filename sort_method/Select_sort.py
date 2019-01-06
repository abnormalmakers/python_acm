def find_samll(l):
    small=min(l)
    return small

def Select_sort(l):
    new_l=[]
    for i in range(len(l)):
        temp=find_samll(l)
        new_l.append(temp)
        l.remove(temp)
    return new_l

l=[32,1,5,44,23,67,21,21,44]
result_l=Select_sort(l)
print(result_l)
