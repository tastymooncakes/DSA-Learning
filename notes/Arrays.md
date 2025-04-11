# Static Arrays, Dynamic Arrays & Strings

## Static Array

- A static array is a continuous block of memory with a fixed size.
- Arrays have positions called indices.

Example:
```
A = [1, 2, 3, 4, 5]
    0  1  2  3  4  (indices)
```

- Most common operation: Accessing an element at a certain position in **O(1)** time.
  - Example: `A[2] = 3`
- Arrays are mutable objects, meaning their values can be changed, but their size cannot.
  - Example: `A[2] = 4` replaces the value at index 2 with 4.
- Checking if a value exists in the array takes **O(N)** time.
  - Example:  
    - `5 in A => False`  
    - `1 in A => True`

### Limitations of Static Arrays
- **Insertion**: Takes **O(N)** time due to shifting elements.
- **Deletion**: Takes **O(N)** time due to shifting elements.

---

## Dynamic Array (List in Python)

- A dynamic array can change its size.
- Supports operations like insertion (append).

### How It Works
- Under the hood, dynamic arrays use static arrays.
- When the array is full, a new static array (2x the size) is created, and the contents are copied over.
  - Example:
    ```
    [1, 5, 2, 3, 7, 8] -> [1, 5, 2, 3, 7, 8, _, _, _]
    ```
- Copying contents takes **O(N)** time, but insertion into the empty space is **O(1)**.

### Time Complexity
- **Insertion at the end**: **O(1)** (amortized).
- **Insertion in the middle or deletion**: **O(N)** due to potential data shifting.

---

## Data Structures (Array & Strings)

### Array / List Operations

| Operation                  | Time Complexity |
|----------------------------|-----------------|
| Popping from end           | O(1)           |
| Appending to end           | O(1)           |
| Insertion (not at the end) | O(N)           |
| Deletion (not at the end)  | O(N)           |
| Modifying an element       | O(1)           |
| Random Access              | O(1)           |
| Checking if element exists | O(N)           |

---

## Strings

- Strings are written in quotes (e.g., `'abc'`).
- Strings are **immutable**.
  - To insert or modify, a new string is created, making most operations **O(N)**.

### Time Complexity

| Operation                  | Time Complexity |
|----------------------------|-----------------|
| Popping from end           | O(N)           |
| Appending to end           | O(N)           |
| Insertion (not at the end) | O(N)           |
| Deletion (not at the end)  | O(N)           |
| Modifying an element       | O(N)           |
| Random Access              | O(1)           |
| Checking if element exists | O(N)           |

---

## Python Usage of Arrays, Dynamic Arrays, and Strings

### Arrays / Lists

```python
A = [1, 2, 3]

# Appending - Insert element at the end of the array (O(1) on average)
A.append(4)
# A = [1, 2, 3, 4]

# Pop - Delete element at the end of the array (O(1))
A.pop()
# A = [1, 2, 3]

# Insert - Not at the end of the array (O(N))
A.insert(2, 5)
# A = [1, 2, 5, 3]

# Modify an element (O(1))
A[1] = 7
# A = [1, 7, 5, 3]

# Access an element (O(1))
print(A[0])  # Output: 1

# Check if an element exists in the array (O(N))
if 6 in A:  # False
    pass
```

### Strings

```python
s = 'hello'

# Append to the end of a string (O(N))
b = s + 'z'
# b = 'helloz'

# Check if something is in the string (O(N))
if 'e' in s:  # True
    pass

# Access positions (O(1))
print(s[1])  # Output: 'e'

# Length of anything in Python (O(1))
print(len(s))  # Output: 5
```

Note: Python stores the length of objects as a property, so `len()` is a constant-time operation.