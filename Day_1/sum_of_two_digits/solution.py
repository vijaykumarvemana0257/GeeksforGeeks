#User function Template for python3
class Solution:
    def sumOfDigits (self, N):
        # code here
        x=str(N)
        s=0
        for i in range(len(x)):
           s=s+int(x[i])
        return (s)

