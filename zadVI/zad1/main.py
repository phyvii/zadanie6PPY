class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.nextE
        return '  '.join(elements)

    def get(self, e):
        current = self.head
        while current:
            if current.data == e:
                return current.data
            current = current.nextE
        return None

    def delete(self, e):
        if self.head.data == e:
            self.head = self.head.nextE
            if self.head is None:
                self.tail = None
            self.size -= 1
            return

        current = self.head
        while current.nextE:
            if current.nextE.data == e:
                if current.nextE == self.tail:
                    self.tail = current
                current.nextE = current.nextE.nextE
                self.size -= 1
                return
            current = current.nextE

    def append(self, e, func=None):
        new_element = Element(e)

        if self.head is None:
            self.head = new_element
            self.tail = new_element
        elif func is None:
            if e >= self.tail.data:
                self.tail.nextE = new_element
                self.tail = new_element
            elif e <= self.head.data:
                new_element.nextE = self.head
                self.head = new_element
            else:
                current = self.head
                while current.nextE and e > current.nextE.data:
                    current = current.nextE
                new_element.nextE = current.nextE
                current.nextE = new_element
        else:
            if func(e, self.tail.data):
                self.tail.nextE = new_element
                self.tail = new_element
            elif func(self.head.data, e):
                new_element.nextE = self.head
                self.head = new_element
            else:
                current = self.head
                while current.nextE and not func(e, current.nextE.data):
                    current = current.nextE
                new_element.nextE = current.nextE
                current.nextE = new_element

        self.size += 1


def main():
    list = MyLinkedList()


    list.append(41)
    list.append(12)
    list.append(62)
    list.append(3)
    list.append(121)


    print(list)


    element = list.get(3)
    print(element)


    list.delete(3)
    print(list)

main()