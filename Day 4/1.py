class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        s = []
        for n in words:
            lower = n.lower()
            # Check which row the first letter belongs to
            if set(lower).issubset(set(row1)):
                s.append(n)
            elif set(lower).issubset(set(row2)):
                s.append(n)
            elif set(lower).issubset(set(row3)):
                s.append(n)
        return s