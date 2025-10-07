def find_missing_numbers(arr):
    listprint=[]
    arr.sort()
    print(arr)
    li = list(range(1,max(arr) + 1))
    print(li)
    for i in range(0,len(li)):
        if li[i] not in arr:
            listprint.append(i + 1)
    return print(listprint)
