Time & Space Complexity Big O Notation

Input = [1, 2, 3, 4, 5]    # can have N number of values
Ouput = [1, 4, 9, 16, 25]  # return the square of input

To achieve this we need to write some sort of function.

some def square(arr):

this function will creaet a new array "Output".
loop through Input array and square each value.
need to visit all (N) values in Input. 

Time: O(N) meaning we need to loop through all N values => linear

In an alternative example we want the Output to be all possible non-repeating pairs of numbers.

Input = [1, 2, 3, 4, 5]    
Ouput = [(1,2), (1, 3), (1, 4) ...]  

In this scenario we have way more than 5 Outputs in our list. 
To solve this problem we are effectively looping through the Input array N * N times making 

Time: O(N*N) or O(N^2) => quadratic

----

Creating a new array takes up space. If its proportional to Input array that is space complexity O(N)

There are scenarios were we can do the manipulation directly in the Input array that results in a space complexity of O(1)

----

O(n^2 + 2n + 1) => O(n^2)
Big O doesn't care about constants and only cares about the strongest components