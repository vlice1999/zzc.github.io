class Solution(object):
    def backingtrack(self,target,candidates,val,start):
        if target==0 and val not in Solution.re:
            Solution.re.append(val)
        else:
            for i in range(start,len(candidates)):
                if target<candidates[i]:
                    break
                self.backingtrack(target-candidates[i],candidates[1:],val+[candidates[i]],i)

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.re=[]
        self.backingtrack(target,candidates,[],0)
        return Solution.re
