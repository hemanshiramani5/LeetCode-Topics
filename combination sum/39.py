class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]

        def make_comb(idx,comb,total):
            if total==target:
                res.append(comb[:])
                return
            if total>target or idx>=len(candidates):
                return
            comb.append(candidates[idx])
            make_comb(idx,comb,total+candidates[idx])
            comb.pop()
            make_comb(idx+1,comb,total)

            return res
        return make_comb(0,[],0)    
