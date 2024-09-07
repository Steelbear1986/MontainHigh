class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(set(arr)) <= 2:
                   return (False)
        a1=arr[:arr.index(max(arr))+1]
        a2=arr[arr.index(max(arr))+1:][::-1]
        if len(a1)<1  or len(a2)<1: return (False)
        if len (a1)==1 and a1[0]==max(arr) or len(a2)==1 and a2[0]==max(arr): return False
        for i in range(1,len(a1)) :
            if len (a1)>1:
                if a1[i]<=a1[i-1]  :
                    return (False)
        for i in range(1,len(a2)) :
            if len (a2)>1:
                if a2[i]<=a2[i-1]  :
                     return (False)
        return True