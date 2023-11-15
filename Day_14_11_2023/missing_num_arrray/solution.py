#User function Template for python3

import math


class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        ##Your code here
        x=0
        i=1
        while x<=n:
            if n==1 :
                return 1
            elif  x==math.pow(2,i):
                    return 1
            else:
                x=math.pow(2,i)
                i=i+1
        return 0       
            
            
            

