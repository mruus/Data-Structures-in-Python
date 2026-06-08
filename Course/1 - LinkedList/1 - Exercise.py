class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_nodes(self):
        current_node = self.head
        if not current_node:
            print("No available nodes. Create new nodes to print!")
            return
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    def insert_at_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        current_node = self.head
        if current_node is None:
            self.head = new_node
            return
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def count_even_numbers(self):
        current_node = self.head
        count = 0
        while current_node:
            if current_node.value % 2 == 0:
                count += 1
            current_node = current_node.next
        return count

    def find_largest_value(self):
        current_node = self.head
        largest = current_node.value
        while current_node:
            if current_node.value > largest:
                largest = current_node.value
            current_node = current_node.next
        return largest

    def find_smallest_value(self):
        current_node = self.head
        smallest = current_node.value
        while current_node:
            if current_node.value < smallest:
                smallest = current_node.value
            current_node = current_node.next
        return smallest

    def sum_values(self):
        current_node = self.head
        total = 0
        while current_node:
            total += current_node.value
            current_node = current_node.next
        return total


# 1 - Count even numbers
print("1 - Count even numbers")
even_list = LinkedList()
even_list.insert_at_start(10)
even_list.insert_at_end(21)
even_list.insert_at_end(30)
even_list.insert_at_end(45)
even_list.insert_at_end(50)
even_list.print_nodes()
print(even_list.count_even_numbers(), end="\n\n")

# 2 - Find the largest value
print("2 - Find the largest value")
largest_list = LinkedList()
largest_list.insert_at_start(10)
largest_list.insert_at_end(90)
largest_list.insert_at_end(5)
largest_list.insert_at_end(40)
largest_list.print_nodes()
print(largest_list.find_largest_value(), end="\n\n")

# 3 - Find the smallest value
print("3 - Find the smallest value")
smallest_list = LinkedList()
smallest_list.insert_at_start(10)
smallest_list.insert_at_end(90)
smallest_list.insert_at_end(5)
smallest_list.insert_at_end(40)
smallest_list.print_nodes()
print(smallest_list.find_smallest_value(), end="\n\n")

# 4 - Sum all values
print("4 - Sum all values")
sum_list = LinkedList()
sum_list.insert_at_start(10)
sum_list.insert_at_end(20)
sum_list.insert_at_end(30)
sum_list.print_nodes()
print(sum_list.sum_values())
