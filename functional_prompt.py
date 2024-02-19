def flatten_and_sort(array):
    flattened_arr = []
    for item in array:
        if isinstance(item, list):
            flattened_arr.extend(flatten_and_sort(item))
        else:
           flattened_arr.append(item)
    return sorted(flattened_arr)
    

'''
1. How does this solution ensure data immutability?
    This solution ensures immutability as it doesnt modify the "array" input, instead a new list (flattened_arr) was created and modified throughout the function
    
2. Is this solution a pure function? Why or why not?
    Yes, this function does not modify external variables and has no "side effects"
    
3. Is this solution a higher order function? Why or why not?
    No, this function doesnt take another function as an argument, nor does it return a function

4. Would it have been easier to solve this problem using a different programming style?
    I believe the solution I provided to be the easiest, however, there may be another way to solve this without using recursion. However, in my attempts to negate the use
    of recursion, I recieved errors, hence why the recursive route was taken.

5. Why is functional programming a helpful paradigm when solving this problem?
    The functional programming approach is helpful when solving this problem, as this problem purely depends on its input to produce its output and does not need mutable data.
'''

sorting = [5, 7, 8, 3, 2, 9]

print(flatten_and_sort(sorting))