#Tsygankov_FP_1

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node or None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_insert(self, data):
        new_node = Node(data)
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def merge_sorted_lists(self, list1, list2):
        dummy = Node()
        tail = dummy
        while True:
            if list1 is None:
                tail.next = list2
                break
            if list2 is None:
                tail.next = list1
                break
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        return dummy.next


if __name__ == "__main__":
    llist = LinkedList()

    # Запит користувача для вибору функції
    print("Оберіть операцію:")
    print("1. Вставити елемент в кінець списку")
    print("2. Реверсувати список")
    print("3. Сортувати список")
    print("4. Об'єднати два відсортованих списки")
    choice = int(input("Ваш вибір: "))

    # Виконання вибраної операції
    if choice == 1:
        llist.insert_at_end(6)
        llist.print_list()
    elif choice == 2:
        llist.insert_at_beginning(1)
        llist.insert_at_beginning(2)
        llist.insert_at_beginning(3)
        print("Початковий список:")
        llist.print_list()
        llist.reverse()
        print("Реверсований список:")
        llist.print_list()
    elif choice == 3:
        llist.insert_at_end(2)
        llist.insert_at_end(3)
        llist.insert_at_end(1)
        print("Початковий список:")
        llist.print_list()
        llist.head = None  # Очистимо список перед сортуванням
        llist.sorted_insert(2)
        llist.sorted_insert(3)
        llist.sorted_insert(1)
        print("Список після сортування:")
        llist.print_list()
    elif choice == 4:
        list1 = LinkedList()
        list1.insert_at_end(1)
        list1.insert_at_end(3)
        list1.insert_at_end(5)
        list2 = LinkedList()
        list2.insert_at_end(2)
        list2.insert_at_end(4)
        list2.insert_at_end(6)
        print("Перший відсортований список:")
        list1.print_list()
        print("Другий відсортований список:")
        list2.print_list()
        merged_list = LinkedList()
        merged_list.head = merged_list.merge_sorted_lists(list1.head, list2.head)
        print("Об'єднаний список двох відсортованих списків:")
        merged_list.print_list()

