class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []

        def backtrack(i, e, arr, total):
            if total == target:
                result.append(arr.copy())
                return
            elif i >= len(candidates) or total > target:
                return
            elif candidates[i] == e:
                backtrack(i+1, e, arr, total)
                return
            

            arr.append(candidates[i])
            backtrack(i+1, e, arr, total+ candidates[i])

            arr.pop()
            backtrack(i+1, candidates[i], arr, total)

        backtrack(0,0,[], 0)       
        return result
        