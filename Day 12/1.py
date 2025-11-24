class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=j=0

        res=[]
        flag=True
        while i < len(word1) and j < len(word2):
            if flag:
                res.append(word1[i])
                flag=False
                i+=1
            else:
                res.append(word2[j])
                flag=True
                j+=1
        
        res.extend(word1[i:])
        res.extend(word2[j:])

        print(res)
        return "".join(res)



        