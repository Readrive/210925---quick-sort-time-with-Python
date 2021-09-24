import time
import random

#퀵 정렬
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    less_array, equal_array, greater_array = [], [], []
    
    for num in array:
        if num < pivot:
            less_array.append(num)
        elif num > pivot:
            greater_array.append(num)
        else:
            equal_array.append(num)
    return quick_sort(less_array) + equal_array + quick_sort(greater_array)

def quick_sort(array_b):
    if len(array_b) <= 1:
        return array_b

    pivot = array_b[len(array_b) // 2]
    less_array_b, equal_array_b, greater_array_b = [], [], []
    
    for num in array_b:
        if num < pivot:
            less_array_b.append(num)
        elif num > pivot:
            greater_array_b.append(num)
        else:
            equal_array_b.append(num)
    return quick_sort(less_array_b) + equal_array_b + quick_sort(greater_array_b)


#최악
array_b = []
for i in range(1000000, 1, -1):
    array_b.append(i)
array2_b = array_b[:]

start_time = time.time()
quick_sort(array2_b) #퀵정렬
end_time = time.time()
print("퀵 정렬 최악 성능 측정:", end_time - start_time) # 수행 시간 출력


#최선
array = []

for i in range(1, 1000000):
    array.append(i)

#array = [x for x in range(1001)]
#random.shuffle(array)
array2 = array[:]

start_time = time.time()
quick_sort(array2) #퀵정렬
end_time = time.time()
print("퀵 정렬 최선 성능 측정:", end_time - start_time) # 수행 시간 출력
