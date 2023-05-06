from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # return list(map(int,list(str(int("".join(map(str,digits)))+1))))
        s = 0
        for n in digits:
            s = s * 10 + n
        s += 1
        nums = []
        while s > 0:
            nums.append(s % 10)
            s //= 10
        return nums[::-1]
