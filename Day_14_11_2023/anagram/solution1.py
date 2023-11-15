class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        
        if sorted(a) == sorted(b):
            return True
        else:
            return False 
