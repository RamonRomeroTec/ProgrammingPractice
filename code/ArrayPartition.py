# juntar minimo en de parejas sorteadas en arreglo
# # Usar list comprehension, solo cuando se requiera generar
# una nueva lista, no iterar sobre la misma
class Solution(object):
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])
        """
        :type nums: List[int]
        :rtype: int
        """
        