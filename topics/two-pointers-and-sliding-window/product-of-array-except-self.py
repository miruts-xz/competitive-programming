class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr_product = [1]*(len(nums)+1)
        pr_product_rev = [1]*(len(nums)+1)
        
        for i in range(1,len(nums)+1):
            pr_product[i] = pr_product[i-1]*nums[i-1]
            
        for j in range(len(nums)-1, -1, -1):
            pr_product_rev[j] = pr_product_rev[j+1]*nums[j]
            
        answer = [0]*len(nums)
        for i in range(len(nums)):
            answer[i] = pr_product[i]*pr_product_rev[i+1]
        return answer
