class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = []
        postfixProduct = []
        #pre-processing
        for index, number in enumerate(nums):
            if not prefixProduct:
                 prefixProduct.append(number)
            else:
                prefixProduct.append(number*prefixProduct[index-1])
        for index, number in enumerate(reversed(nums)):
            if not postfixProduct:
                postfixProduct.append(number)
            else:
                postfixProduct.append(number*postfixProduct[index-1])

        #compute the answer
        result = []
        for index, number in enumerate(nums):
            if index == 0:
                result.append(postfixProduct[-2])
            elif index == len(nums)-1 :
                result.append(prefixProduct[-2])
            else:
                result.append(postfixProduct[-2-index]*prefixProduct[index-1])
        return result
        print(prefixProduct)
        print(postfixProduct)
            