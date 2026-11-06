class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_p = 0
        r_p = len(nums) - 1 

        while l_p <= r_p:
            m_p = (l_p + r_p) // 2

            if nums[m_p] == target:
                return m_p
            elif nums[m_p] < target:
                l_p = m_p + 1
            else:
                r_p = m_p -1

        return -1

        