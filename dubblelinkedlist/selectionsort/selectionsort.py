def selectionsort(a):
  for i in range(len(a)):
    min=a[i]
    for j in range(i+1,len(a)):
      if a[j]<min:
        min=a[j]
      a[i],a[j]=a[j],a[i]
  return a


a=[20,42,45,63,31]
print(selectionsort(a))