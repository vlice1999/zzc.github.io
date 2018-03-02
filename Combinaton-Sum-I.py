class Solution(object):
    def backtracking(self,candidates,target,start,val):
        if target==0:
            Solution.result.append(val)
        else:
            for i in range(start,len(candidates)):
                if target<0:
                    break
                self.backtracking(candidates,target-candidates[i],i,val+[candidates[i]])
                
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Solution.result=[]
        self.backtracking(candidates,target,0,[])
        return Solution.result
