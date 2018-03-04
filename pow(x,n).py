class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans=1
        if x==1 or n==0:return 1
        if n>0:
            while n>0:
                j=1
                temp=x
                while 2*j<n:
                    temp*=temp
                    j*=2
                ans*=temp
                n-=j
        if n<0:
            while n<0:
                j=1
                temp=1/x
                while 2*j<-n:
                    temp*=temp
                    j*=2
                ans*=temp
                n+=j
        return ans
