# fishy_python_sort

JavaScript version of this repository [https://github.com/sergemoskalenko/fishy_javascript_sort](https://github.com/sergemoskalenko/fishy_javascript_sort)

This is a Python code written for a quirky contest of inefficient coding, designed to be deliberately very suboptimal, fishy, and one-liner, yet somehow manages to do seemingly useful things in a bizarre, roundabout way...

So, what do we have here? We’ve created a random number generator that loves to do bit shifts and called it R9. Then we use this generator to pick two random indices of an array and swap them if they are out of order. All this happens in the srt_f function, which is called in a loop inside the shit_sort function until the array is sorted.
And yes, the name shit_sort hints that this is not the most efficient way to sort, but it’s fun! 😄

```python
import time  # Import time to make our code move slowly but surely forward.

# R9 function is our random number generator that loves to do bit shifts.
R9 = lambda s, c: int(abs((s := int(s)) ^ (s << 13) ^ (s >> 17) ^ (s << 5)) % c)

# ij function is our magical way to pick two random indices of an array.
ij = lambda a, s, i, j: (j, i) if (i := R9(s, len(a))) > (j := R9(s + 731, len(a))) else (i, j)

# pr function is our way to nicely print arrays before and after sorting.
pr = lambda arr, src_arr: (print("\nSRC (in):", src_arr), print("\nWRK (out):", arr))

# srt_f function is our sorting algorithm that swaps elements if they are out of order.
def srt_f(arr):
    global seed
    seed += int(time.time())  # Update seed to have something new each time.
    i, j = ij(arr, seed, 0, 0)  # Get two random indices.
    print(i, "<-->", j) if arr[i] > arr[j] else None  # Print indices if elements are out of order.
    (arr[i], arr[j]) = (arr[j], arr[i]) if arr[i] > arr[j] else (arr[i], arr[j])  # Swap elements if needed.

# shit_sort function is our main sorting algorithm that uses srt_f to sort the array.
def shit_sort(arr, src_arr, t):
    [srt_f(arr) for _ in iter(lambda: not all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)), False)]

# Start by generating a random seed based on the current time.
seed = int(time.time())

# Generate an array WRK of 100 random numbers.
WRK = [int(R9(seed + i, 1000)) for i in range(100)]

# Copy WRK to SRC to keep the original array.
SRC = WRK.copy()

# Print a message about starting the sorting.
print("\nSorting WRK...")

# Start sorting the WRK array.
shit_sort(WRK, SRC, True)

# Print arrays before and after sorting.
pr(WRK, SRC)
```
