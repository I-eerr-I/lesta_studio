class FIFO1:
    """
    Циклический буфер FIFO с использованием списка и указателей на начало и конец  списка.
    При переполнении буфера данные перезаписываются.
    Плюсом такого буфера можно назвать простой доступ к любому элементу очереди по индексу, используя индекс head: (head + index) % maxsize или (head + index) % size
    Минусом может быть использование списка, как дополнительной памяти, для реализации такой очереди.

    При этом добавление и удаление элементов проходит за О(1).
    В таком случае и получение элемента по произвольному индексу проходит за О(1).
    """
    def __init__(self, size):
        self.maxsize = size
        self.array   = [None for _ in range(self.maxsize)]
        self.head    = 0
        self.tail    = -1
    
    def put(self, value):
        self.tail += 1
        self.tail %= self.maxsize
        self.array[self.tail] = value
    
    def pop(self):
        value = self.array[self.head]
        self.array[self.head] = None
        self.head += 1
        if self.head == self.maxsize:
            self.head = 0
        return value
    
    def __str__(self):
        return str(self.array)

class Node:
    """Реализация узла связанного списка"""
    def __init__(self, value=None, next=None):
        self.value = value
        self.next  = next
    
    def __str__(self):
        return f"{self.value}"

class FIFO2:
    """
    Циклический буфер FIFO с использованием связанного списка.
    Указатель pointer требуется для перезаписи элементов при добавлении новых в переполненную очередь.
    Плюсом такой реализации является использование лишь указателей на элементы, но не отдельного списка с элементами.
    Минусом является то, что реализация получения элемента очереди по произвольному индексу будет выполняться за O(n) в худшем случае, так как
    понадобится перебрать все элементы.

    Аналогично, добавление и удаление элементов из очереди происходит за О(1).
    """
    def __init__(self, size):
        self.maxsize = size
        self.head    = None
        self.tail    = None
        self.pointer = None
        self.size    = 0
    
    def put(self, value):
        if self.size == self.maxsize:
            if self.pointer.next is None:
                self.pointer = self.head
            self.pointer.value = value
            self.pointer = self.pointer.next
        else:
            element  = Node(value)
            if self.tail is None:
                self.head = self.pointer = self.tail = element
            else:
                self.tail.next = element
                self.tail      = element
                self.pointer   = element
            self.size += 1
    
    def pop(self):
        if self.head is None:
            return None
        element = self.head
        self.head = element.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        self.pointer = self.tail
    
    def __str__(self):
        node = self.head
        s    = ''
        while node is not None:
            s += str(node.value) + ' -> '
            node = node.next
        return s

