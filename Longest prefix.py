// Write a function to find the longest common prefix string amongst an array of strings.
class Solution(object):
    def longestCommonPrefix(self, strs):
        min=200
        n=len(strs)
        com=""
        cur_char=""
        for i in strs:
            if len(i)<min:
                min=len(i)
                tar=i
        for k in range(min):
            cur_char+=tar[k]
            count=0           
            for s in strs:
                if s.startswith(cur_char):
                    count+=1
            if count==n:
                com+=tar[k]
            else:
                break
        return com
                
