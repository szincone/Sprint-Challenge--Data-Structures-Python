Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
I think it'd be O(1), it's basically doing the same thing each time regardless of the dataset.

2. What is the space complexity of your ring buffer's `append` function?
I think it'd also be O(1) because it's storing the same amount of data everytime.

3. What is the runtime complexity of your ring buffer's `get` method?
I believe this one is O(n). Since it would grow w/ the loop size.

4. What is the space complexity of your ring buffer's `get` method?
I think it's O(n). It has to hold the return values which will grow as the list gets bigger.

5. What is the runtime complexity of the provided code in `names.py`?
O(n ^ 2) due to the nested for loops.

6. What is the space complexity of the provided code in `names.py`?
O(n) I think because the storage would only grow w/ the duplicates array size.

7. What is the runtime complexity of your optimized code in `names.py`?
https://wiki.python.org/moin/TimeComplexity, tells me that list.sort is considered O(n log n), so right off the bat it's not looking good. The set, to list conversion should be O(n) since we have to iterate once, same for back to list, then final check involves for_loop so O(n) since it'll only be 1 pass regardless. Not really sure how to add that all up, but I think worst case total, would be O(n log n) mainly due to sort, the rest would probably avg to O(n) and this would be best case. 

8. What is the space complexity of your optimized code in `names.py`?
Up until line 24, I think it'd be pretty constant with O(n). The final check would have to store the data on 1 pass, so it'd be O(n) too. O(n) total.
