# Лабораторная работа № 10.
### `class Stack` - это коллекция элементов, организованная по принципу LIFO (Last-In-First-Out): последний добавленный элемент оказывается первым для извлечения. Все операции выполняются только с вершиной стека: вставка, удаление и просмотр элемента. Реализация на основе списка моделирует работу стека вызовов, где данные сохраняются и извлекаются в обратном порядке относительно их поступления.
### **Основные операции**: 
### `push` - метод добавления элемента в конец коллекции
### `pop` - метод удаления элемента с конца коллекции
### `peek` - метод, возвращающий вершинный элемент стека

**** 
### `class Queue` - это структура данных, работающая по принципу FIFO (First-In-First-Out), где элементы обрабатываются в порядке их поступления. Реализуется на основе deque, который использует связанные блоки фиксированного размера, хранящиеся в куче произвольным образом, что обеспечивает эффективность работы с обоими концами коллекции.
### Основные операции:
### `enqueue` - метод добавление элемента в начало коллекции
### `dequeue` - метод удаление получения и удаления элемента с начала коллекции
### `peek` - метод, возвращающий первого в очереди

****
### `class SingleLinkedList` - коллекция, основанная на связанных последовательно элементах Node, которые хранят в себе указатель на следующий элемент коллекции и значение текущего Node
### Основные операции: 
### `append` - метод, добавляющий элемент в конец односвязного списка
### `prepand` - метод, добавляющий элемент в начало
### `insert` - метод, добавляющий элемент на произвольную позицию, изменяя указатель предыдущего элемента

*****
# `structures.py`
<img width="1916" height="1499" alt="image" src="https://github.com/user-attachments/assets/4178c06a-f3b4-47a6-b502-ef3d21830e22" />
<img width="1124" height="581" alt="image" src="https://github.com/user-attachments/assets/c9b4f279-72ab-48df-80c9-1804d066b90a" />

```
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
```

# `linked_list.py`
<img width="2057" height="1522" alt="image" src="https://github.com/user-attachments/assets/21b66485-1573-4ed3-a2b7-263cd40a047c" />
<img width="2033" height="1496" alt="image" src="https://github.com/user-attachments/assets/34308b8c-d3b6-455c-8f04-1fbb6ae67d28" />
<img width="1854" height="1442" alt="image" src="https://github.com/user-attachments/assets/eddb895d-ed29-4578-adb8-1e899e78d2e8" />
<img width="1865" height="1446" alt="image" src="https://github.com/user-attachments/assets/3b2fccd5-ee27-4a01-b270-df9a0f99ca68" />
<img width="1093" height="549" alt="image" src="https://github.com/user-attachments/assets/d082d703-b265-4e11-bb1b-3b60ec796330" />


```
from typing import Any, Iterator, Optional


class Node:
    
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.next: Optional['Node'] = None
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
    
    def append(self, value: Any) -> None:
        new_node = Node(value)
        
        if self.head is None:
            # Если список пуст
            self.head = new_node
            self.tail = new_node
        else:
            # Если список не пуст
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        new_node = Node(value)
        
        if self.head is None:
            # Если список пуст
            self.head = new_node
            self.tail = new_node
        else:
            # Если список не пуст
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range for list of size {self._size}")
        
        if idx == 0:
            # Вставка в начало
            self.prepend(value)
            return
        elif idx == self._size:
            # Вставка в конец
            self.append(value)
            return
        
        # Вставка в середину
        new_node = Node(value)
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self._size += 1
    
    def remove_at(self, idx: int) -> None:
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range for list of size {self._size}")
        
        if idx == 0:
            # Удаление из начала
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            # Удаление из середины или конца
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            # current теперь указывает на элемент перед удаляемым
            if current.next == self.tail:
                # Если удаляем последний элемент
                self.tail = current
            
            current.next = current.next.next
        
        self._size -= 1
    
    def remove(self, value: Any) -> bool:
        if self.head is None:
            return False
        
        # Проверяем первый элемент
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        
        # Ищем в остальной части списка
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        
        return False
    
    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        return self._size
    
    def __repr__(self) -> str:
        elements = list(self)
        return f"SinglyLinkedList({elements})"
    
    def visual_repr(self) -> str:
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        parts.append("None")
        return " -> ".join(parts)
    
    def get(self, idx: int) -> Any:
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range for list of size {self._size}")
        
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value


if __name__ == "__main__":
    # Демонстрация работы односвязного списка
    print("=== Демонстрация SinglyLinkedList ===")
    lst = SinglyLinkedList()
    print(f"Пустой список: {lst}")
    print(f"Визуально: {lst.visual_repr()}")
    print(f"Длина: {len(lst)}")
    
    # Добавление элементов
    lst.append(11)
    lst.append(22)
    lst.append(33)
    print(f"\nПосле append: {lst}")
    print(f"Визуально: {lst.visual_repr()}")
    
    # Добавление в начало
    lst.prepend(5)
    print(f"\nПосле prepend(5): {lst}")
    print(f"Визуально: {lst.visual_repr()}")
    
    # Вставка по индексу
    lst.insert(2, 15)
    print(f"\nПосле insert(2, 15): {lst}")
    print(f"Визуально: {lst.visual_repr()}")
    
    # Получение элемента
    print(f"\nЭлемент по индексу 2: {lst.get(2)}")
    
    # Итерация
    print("\nИтерация по списку:")
    for item in lst:
        print(f"  {item}")
    
    # Удаление по значению
    lst.remove(20)
    print(f"\nПосле remove(20): {lst}")
    print(f"Визуально: {lst.visual_repr()}")
    
    # Удаление по индексу
    lst.remove_at(1)
    print(f"\nПосле remove_at(1): {lst}")
    print(f"Визуально: {lst.visual_repr()}")
    print(f"Длина списка: {len(lst)}")
```

# Вывод в терминале:
<img width="1241" height="1426" alt="image" src="https://github.com/user-attachments/assets/f2aadf18-f86d-437b-9fd9-617415fc5073" />
<img width="854" height="515" alt="image" src="https://github.com/user-attachments/assets/aa965bb1-f29d-43bd-90df-1a5360cf8b6b" />
