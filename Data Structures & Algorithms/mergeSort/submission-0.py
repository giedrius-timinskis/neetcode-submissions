# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.performMergeSort(pairs, 0, len(pairs) - 1)

    def performMergeSort(self, pairs: List[Pair], start: int, end: int) -> List[Pair]:
        if end - start + 1 <= 1:
            return pairs

        middle: int = (start + end) // 2

        self.performMergeSort(pairs, start, middle)
        self.performMergeSort(pairs, middle + 1, end)

        self.merge(pairs, start, middle, end)

        return pairs

    def merge(self, pairs, start: int, middle: int, end: int):
        L = pairs[start : middle + 1]
        R = pairs[middle + 1 : end + 1]

        idxL = 0
        idxR = 0
        pairsIdx = start

        # Merge sorted halves into original array
        while idxL < len(L) and idxR < len(R):
            if L[idxL].key <= R[idxR].key:
                pairs[pairsIdx] = L[idxL]
                idxL += 1
            else:
                pairs[pairsIdx] = R[idxR]
                idxR += 1
            pairsIdx += 1

        # Halves might still have elements left
        while idxL < len(L):
            pairs[pairsIdx] = L[idxL]
            idxL += 1
            pairsIdx += 1
        while idxR < len(R):
            pairs[pairsIdx] = R[idxR]
            idxR += 1
            pairsIdx += 1