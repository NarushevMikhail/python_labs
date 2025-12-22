from collections import deque

class Stack:
    def __init__(self):
        # внутреннее хранилище стека
        self._data = []

    def push(self, item):
        # корректно: добавление в конец списка O(1) амортизированно
        self._data.append(item)

    def pop(self):
        # TODO: добавить обработку случая пустого стека (сейчас IndexError от list)
        if self.is_empty(): #проверка, что список пуст
            raise IndexError('Пустой Stack')
        return self._data.pop() #удаляет последний элемент списка (вершину стека).

    def peek(self):
        # ошибка: при пустом стеке будет IndexError — желательно вернуть None
        if self.is_empty:
            return None
        return self._data[-1]
    
    def __len__(self):
        return len(self._data) #возвращает длину списка 

    @property #из метода -> свойство (не нужны скобки)
    def is_empty(self):
        # TODO: улучшить реализацию
        return not self._data

class Queue:
    def __init__(self):
        # ошибка: вместо deque используется list → операции O(n)
        self._data = deque() #deque взять элемент из начала

    @property #из метода -> свойство (не нужны скобки)
    def is_empty(self):
        return not self._data #вернет True, if empty 

    def enqueue(self, item):
        # ошибка: вставка в начало, а не в конец
        self._data.append(item) #добавляет эллемент в правый конец

    def dequeue(self):
        # ошибка: удаление с конца, а не с начала
        if self.is_empty:
            raise IndexError('Пустая Queue')
        return self._data.popleft() #удаляет элемент с левого конца

    def peek(self):
        # TODO: корректное поведение при пустой очереди
        if not self.is_empty:
            return None
        return self._data[0]

    def __len__(self):
        return len(self._data)