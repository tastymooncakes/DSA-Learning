# Singly & Doubly Linked List

## Representation

A linked list is represented as:
```
1 => 2 => 3 => 4 => (None)
```

- Each number is referred to as a **Linked List Node** or **Node**.
- A node is like an object with the following properties:
  - `Node.value`: The value of the node.
  - `Node.next`: A reference to the next node (e.g., `2` if the current node is `1`).

### Traversing the Linked List
We are typically given the `head` of the list and need to traverse it to access a specific node.

---

## Operations on Singly Linked List

### Add Node at a Position
- Traverse the list to the desired position and update the `next` reference.
- **Time Complexity**: **O(N)**

### Delete Node at a Position
- Traverse the list from the `head` to the desired position and adjust the `next` reference.
- **Time Complexity**: **O(N)**

### Access a Node
- Accessing a node requires traversal.
- **Time Complexity**: **O(N)**

### Lookup
- Searching for a value in the list requires traversal.
- **Time Complexity**: **O(N)**

### Special Cases
- **Remove node from the beginning**: **O(1)**
- **Add node at the beginning**: **O(1)**

---

## Doubly Linked List

A doubly linked list is an extension of a singly linked list with reverse connections as well. It allows traversal in both forward and backward directions.

### Node Properties
- `Node.value`: The value of the node.
- `Node.next`: A reference to the next node.
- `Node.prev`: A reference to the previous node.

### Advantages
- Allows for deletion at a specific position more efficiently.

---

## Python Implementation

### Singly Linked List

```python
class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

# Creating a linked list
Head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)

Head.next = A
A.next = B
B.next = C
```

#### Traverse the List - **O(N)**
```python
curr = Head
while curr:
    print(curr)
    curr = curr.next
```

#### Display Linked List - **O(N)**
```python
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))  # Example: 1 -> 2 -> 3 -> 4
```

#### Search for a Node - **O(N)**
```python
def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False
```

---

### Doubly Linked List

```python
class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

# Creating a doubly linked list
head = tail = DoublyNode(1)
```

#### Display Doubly Linked List - **O(N)**
```python
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))  # Example: 1 -> 2 -> 3 -> 4
```

#### Insert at the Beginning
```python
def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return new_node, tail
```