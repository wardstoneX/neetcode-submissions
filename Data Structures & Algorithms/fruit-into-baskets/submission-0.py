class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        maxFruits = 0
        for i, n in enumerate(fruits):
            
            basket = []
            j = i
            count = 0
            while j < len(fruits) and (len(basket) < 2 or (len(basket) == 2 and fruits[j] in basket)):
                if fruits[j] in basket:
                    count +=1
                else:
                    basket.append(fruits[j])
                    count += 1
                j += 1
            maxFruits = max(maxFruits, count)
        
        return maxFruits