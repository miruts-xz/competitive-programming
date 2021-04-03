class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s = 0
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                s += i + num//i
        return s == num-1 if num > 1 else False
