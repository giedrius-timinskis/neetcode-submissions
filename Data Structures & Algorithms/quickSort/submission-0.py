# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.performQuickSort(pairs, 0, len(pairs) - 1)

    def performQuickSort(self, pairs: List[Pair], start: int, end: int) -> List[Pair]:
        if end - start + 1 <= 1:
            return pairs

        # In quick sort we choose the end of the array as the pivot
        pivot = pairs[end]
        partition_index = start

        for i in range(start, end):
            # We only swap elements that are less than the pivot
            # This will guarantee that all elements to the left of the pivot
            # are less than the pivot and all elementsto the right
            # are greater than or equal to the pivot
            if pairs[i].key < pivot.key:
                temp = pairs[partition_index]
                pairs[partition_index] = pairs[i]
                pairs[i] = temp
                # After swapping we can guarantee that all elements to the left of the pivot
                # are less than the pivot, so we can increment the partition index
                partition_index += 1

        # After looping through the array we have to swap the pivot with the element at the partition index
        # This will guarantee that the pivot is in the correct position
        # and all elements to the left of the pivot are less than the pivot
        # and all elements to the right of the pivot are greater than or equal to the pivot
        pairs[end] = pairs[partition_index]
        pairs[partition_index] = pivot

        # Now we can recursively sort the left and right halves of the array
        # We know that the pivot is in the correct position so we can skip it
        self.performQuickSort(pairs, start, partition_index - 1)  # left
        self.performQuickSort(pairs, partition_index + 1, end)  # right

        return pairs
        