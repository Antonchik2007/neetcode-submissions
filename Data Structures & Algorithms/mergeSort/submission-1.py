# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return []
        if len(pairs) == 1:
            return pairs

        middle = len(pairs) // 2
        left = self.mergeSort(pairs[:middle])
        right = self.mergeSort(pairs[middle:])
        result = []
        left_pointer = 0
        right_pointer = 0
        while left_pointer<len(left) or right_pointer<len(right):
            if left_pointer == len(left):
                result.append(right[right_pointer])
                right_pointer += 1
            elif right_pointer == len(right):
                result.append(left[left_pointer])
                left_pointer += 1
            elif left[left_pointer].key > right[right_pointer].key:
                result.append(right[right_pointer])
                right_pointer += 1
            else:
                result.append(left[left_pointer])
                left_pointer += 1
        return result
