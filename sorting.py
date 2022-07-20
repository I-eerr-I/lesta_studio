import random

def merge(array: list, low: int, mid: int, high: int, asc=True):
    """ 
    Объединяет два массива (а именно, две части одного массива) в один в отсортированном порядке.
    Здесь используется индексация левой и правой частей массива таким образом, что данная часть массива стала отсортированной.
    """
    nleft  = mid  - low + 1
    nright = high - mid
    
    left   = []
    right  = []
    for i in range(nleft):
        left.append(array[low + i])
    for j in range(nright):
        right.append(array[mid + j + 1])
    left  += ([float('inf')] if asc else [-float('inf')])
    right += ([float('inf')] if asc else [-float('inf')])

    i_left = i_right = 0
    for i in range(low, high+1):
        leftkey  = left[i_left]
        rightkey = right[i_right]
        if (leftkey <= rightkey and asc) or (leftkey > rightkey and not asc):
            array[i] = left[i_left]
            i_left += 1
        else:
            array[i] = right[i_right]
            i_right += 1


def mergesort(array: list, low: int = 0, high: int = None, reverse=False):
    """
    Разбивает массив на две половины и сортирует их по-отдельности рекурсивно.
    Сортировка частей массива происходит их объединением уже в отсортированном виде.
    Например,
    array = [3 2 1 0]

           [3 2 1 0]
           /        \
      [3 2]         [1 0]
      /   \         /    \
    [3]   [2]     [1]   [0]
     \     /       \     /
      [2 3]         [0 1]
          \          /
           [0 1 2 3]

    В худшем случае такой алгоритм сортирует массив чисел за O(n log(n)).
    Объединение двух массивов происходит за O(n), при этом используется дополнительная память S(n) для хранения
    левой и правой части массива при их объединении.

    Хороший и простой алгоритм, который довольно быстро отрабатывает на больших массивах. 
    Однако, работает не быстрее когда массив уже отсортирован.
    """
    asc = not reverse
    if high is None:
        high = len(array)-1

    if low < high:
        mid  = (low + high)//2
        mergesort(array, low,   mid,  reverse)
        mergesort(array, mid+1, high, reverse)
        merge(array, low, mid, high, asc)



if __name__=='__main__':
    arr = list(range(-10, 10))
    random.shuffle(arr)

    mergesort(arr)
    assert arr == list(range(-10, 10))