## Сортировка слиянием (Merge sort)

def merge(a, p, q, r):
    n1 = q - p + 1 
    n2 = r - q
    # создадим 2 массива L[1 ... n1+1] i R[1 ... n2+1]
    L = []
    R = []
    for i in range(n1):
        L.append(a[p + i])
    for j in range(n2):
        R.append(a[q + j+1])
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    k = p 
    while k <= r:     
        if L[i] <= R[j]:
            a[k] = L[i]
            i = i + 1
            k = k + 1
        else:
            a[k] = R[j]
            j = j + 1
            k = k + 1
    return a


def merge_sort(array, start = None , end = None):
    if (start == None):
        start = 0
    if (end == None):
        end = len(array) - 1
    if start < end:
        q = (start + end)//2
        merge_sort(array, start, q)
        merge_sort(array, q+1, end)
        array = merge(array, start, q, end)  
    return array

# main
#a = [88, 67, 4, 6, 4, 9, 67, 11, 2]
# b = [1, 3, 4, 7, 0, 2, 4, 6]
#p = 0
#r = len(a) - 1 
#print(a)
#print(merge_sort(a, start=1, end=len(a)-2 )) # отсортирует подмассив
# print(merge(b, 0, (len(b)-1)//2, len(b)-1))




## Сортировка вставками (insertion sort)

def insertion_sort(array):
    for j in range(len(array) - 1):
        k = array[j+1]
        l = i = j
        while (i >= 0 and array[i] > k):
            array[l+1] = array[i]            
            array[i] = k
            i = i - 1
            l = l - 1
            

# main            
# b = [1, 6, 4, 7, 0, 2, 4, 3]
# print(str(b) + '\n')
# insertion_sort(b)
# print(b)




## Бинарный поиск (Binary search)

def binary_search(x, array, start = None, end = None):
    array = merge_sort(array, start, end)
    if (start == None):
        start = 0
    if (end == None):
        end = len(array) - 1
    while(start < end):
        q = start + (end-start)// 2
        if ( x - array[q] == 0 ):
            while q>0 and (x - array[q] == 0): # finding 1st "x" on sequence
                q = q-1
            return q+1
        if (x < array[q]):
            end = q
        else:
            start = q + 1
    if(array[end] == x): # testing last element
        return end
    return float('inf')
# main
#b = [0, 1, 2, 2, 2, 2, 2, 4, 3]
#print(a)
#merge_sort(a, start = 2, end=len(a)-2)
#print(a)
#a = [88, 67, 4, 6, 4, 9, 67, 11, 2]
#i = binary_search(2, a, start = 2, end=len(a)-2)
#print(i)




## Пирамидальная сортировка  (HEAP sORt)
def left(i):
    return 2*i

def right(i):
    return 2*i+1
    
def parent(i):
    return i//2
    
def root(i):
    return 1
    
def heap_size(array):
    return len(array)-1
    
def swap(a, b):
    return b, a
    
def sift_down(array, i):
    l = left(i)
    r = right(i)
    #print(l, ' : ', r, ' -> parent: ', i)
    if (l <= heap_size(array)) and (array[l] > array[i]):
        largest = l
    else:
        largest = i
    if (r <= heap_size(array)) and (array[r] > array[largest]):
        largest = r
        
    if largest != i:
        array[i], array[largest] = swap(array[i], array[largest])
        sift_down(array, largest)
        
def build_max_heap(array):
    for i in range(heap_size(array)//2, 0, -1):
        sift_down(array, i)
        
def heap_sort(array):
    array.insert(0, 0)
    b = []
    build_max_heap(array)
    #print("I ve end building the heap: ",array)
    for i in range(heap_size(array), 0, -1):
        array[1], array[i] = swap(array[1], array[i])
        b.insert(0, array[i]) # last element summons on returning array
        array = array[:-1]
        sift_down(array, 1)
        #print('Look at ME: ',b)
    array = b
## main
# a = [16,4,10,8,7,9,3,2,14,1]
# a = [10, 9, 8, 7, 6, 5, 4 , 3, 2, 1, 0]
# print(a)
# a = heap_sort(a)
# print(a)





## Быстрая сортировка (Quick Sort)
 
def partition(array, p=None, r=None):
    x = array[r]
    i = p-1
    for j in range(p, r-1):
        if array[j] <= x:
            i = i+1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i+1

def quicksort(array, p = None, r = None):
    if (p == None):
        p = 0
    if (r == None):
        r = len(array) - 1
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q-1)
        quicksort(array, q+1, r)
    
## main
#a = [6, 0, 7, 7, 9, 10, 20, 8, 0]
#print (a)
#quicksort(a, 0, len(a)-1)
#print(a)




## Сортировка подсчётом (Count Sort)
def find_k(arr):
    max = min = arr[0]
    for i in range(1, len(arr)):
        if(arr[i] > max):
            max = arr[i]
        if(arr[i] < min):
            min = arr[i]
    return (max - min + 1)

def count_sort(array, c = None, k = None):
    if array == []:
	    return array
	if k == None:
        k = find_k(array)
    if c == None:
        c = []
        for i in range(k):
            c.append(0)
    if (len(c) != k):
        return 'error'
    for i in range(k):
        c[i] = 0
    for j in range(0, len(array)):
        c[array[j]] += 1
    for i in range(1, k):
        c[i] += c[i-1]
    b = array.copy()
    for j in range(len(array)-1, -1, -1):
        b[c[array[j]] -1] = array[j]
        c[array[j]] -= 1
    return b

## main
# a = [1001, 0, 7, 7, 9, 10, 20, 8]
a = [1]
print (a)
a = count_sort(a)
print(a)