arr = [5,11,3,1,10]
def fnct1(arr):
    for i in range(1,len(arr)): arr[i]=arr[i-1]+1
    print(arr)

def fnct2(arr):
    for i in range(len(arr)):
        if arr[i]>5:    arr[i] = 1
        else:   arr[i] = 0
    print(arr)

#main
fnct1(arr)
fnct2(arr)