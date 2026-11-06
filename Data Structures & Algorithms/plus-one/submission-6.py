class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        print(0)
        for i in range(len(digits) -1, -1, -1):
            print(12)
            s = carry + digits[i]
            print(f"Complement: {i}")

            if s >= 10:
                carry = 1
            else:
                carry = 0

            digits[i] = s % 10
        
        if carry:
            digits.insert(0, 1)
        return digits