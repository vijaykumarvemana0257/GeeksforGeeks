#User function Template for python3
class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        s1={}
        s2={}
        if len(a) == len(b):
            for char in a  :
                if char in s1:
                    s1[char]=s1[char]+1
                else:
                    s1[char]= 1
            for char in b  :
                if char in s2:
                    s2[char]=s2[char]+1
                else:
                    s2[char]= 1
            if s1==s2:
                return True 
            else:
                return False
        else:
            return False 

