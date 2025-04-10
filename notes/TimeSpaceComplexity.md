# Time & Space Complexity Big O Notation

## Example 1: Squaring an Array

**Input:**  
`[1, 2, 3, 4, 5]`  # can have N number of values  

**Output:**  
`[1, 4, 9, 16, 25]`  # return the square of input  

To achieve this, we need to write some sort of function:

```python
def square(arr):
    # This function will create a new array "Output".
    # Loop through Input array and square each value.
    # Need to visit all (N) values in Input.
    pass
```

**Time Complexity:**  
`O(N)` meaning we need to loop through all N values => linear  

---

## Example 2: Generating Non-Repeating Pairs

**Input:**  
`[1, 2, 3, 4, 5]`  

**Output:**  
`[(1, 2), (1, 3), (1, 4), ...]`  

In this scenario, we have way more than 5 outputs in our list.  
To solve this problem, we are effectively looping through the Input array `N * N` times, making:

**Time Complexity:**  
`O(N*N)` or `O(N^2)` => quadratic  

---

## Space Complexity

Creating a new array takes up space. If it's proportional to the Input array, that is space complexity `O(N)`.

There are scenarios where we can do the manipulation directly in the Input array, resulting in a space complexity of `O(1)`.

---

## Simplifying Big O

For example:  
`O(n^2 + 2n + 1)` simplifies to `O(n^2)`  

Big O doesn't care about constants and only cares about the strongest components.