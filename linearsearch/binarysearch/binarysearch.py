

def binarysearch(arr,target):
    l=0
    r=len(a)-1
    m=(l+r)//2
    while l<r:
        
        if a[m]==target:
            print(f'{target}is found at index{m}')
            return
        elif a[m]<target:
            l=m
            m=(l+r)//2
        else:
            r=m
            m=(l+r)//2



a=[10,20,30,40,50]
binarysearch(a,40)

